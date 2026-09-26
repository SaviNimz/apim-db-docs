#!/usr/bin/env python3
"""Generate the complete MkDocs table reference for one APIM product.

Usage: gen_reference.py <product-dir> <out-dir>
  e.g. gen_reference.py wso2am-4.7.0 docs/apim-4/reference

Writes one page per table family (AM, IDN, UM, REG, ...) plus an index page.
Every table in the product's MySQL DDL gets a section with its columns, keys,
declared foreign keys, reverse references and likely (undeclared) joins.
Re-running overwrites the generated pages; never hand-edit them.
"""
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "apim-db-explorer", "scripts"))
from schema_map import parse, implicit  # noqa: E402

FAMILY_TITLES = {
    "AM": "AM_* — API Manager core",
    "GOV": "GOV_* — API governance",
    "IDN": "IDN_* — Identity & OAuth",
    "UM": "UM_* — Users, roles, tenants",
    "REG": "REG_* — Registry",
    "SP": "SP_* — Service providers",
    "IDP": "IDP_* — Identity providers",
    "CM": "CM_* — Consent management",
    "WF": "WF_* — Workflow engine",
    "FIDO": "FIDO_* — FIDO devices",
    "FIDO2": "FIDO2_* — FIDO2 devices",
}


def family(table):
    return table.split("_")[0]


def anchor(table):
    # MkDocs' default toc slugify lower-cases and keeps underscores.
    return table.lower()


def link(table, from_family):
    fam = family(table)
    page = "" if fam == from_family else f"{fam.lower()}.md"
    return f"[`{table}`]({page}#{anchor(table)})"


def main(product, out):
    apim = os.path.join(product, "dbscripts", "apimgt", "mysql.sql")
    shared = os.path.join(product, "dbscripts", "mysql.sql")
    tables, db_of = {}, {}
    for path, db in ((apim, "APIM DB (WSO2AM_DB)"), (shared, "Shared DB (WSO2SHARED_DB)")):
        parsed = parse(path)
        tables.update(parsed)
        db_of.update({t: db for t in parsed})

    referenced_by = defaultdict(list)
    for name, t in tables.items():
        for fk in t["fks"]:
            referenced_by[fk["ref_table"]].append((name, fk))
    logical = defaultdict(list)
    for src, col, tgt, why in implicit(tables):
        logical[src].append((col, tgt, why))

    fams = defaultdict(list)
    for name in sorted(tables):
        fams[family(name)].append(name)

    os.makedirs(out, exist_ok=True)
    version = os.path.basename(os.path.normpath(product)).replace("wso2am-", "")

    with open(os.path.join(out, "index.md"), "w") as f:
        f.write("# Table reference\n\n")
        f.write(f"Every table defined in the APIM **{version}** database scripts, grouped by name prefix. ")
        f.write("These pages are generated from `dbscripts/**/mysql.sql`, so they list every column and key. ")
        f.write("Each table's purpose is explained on the domain pages.\n\n")
        f.write('!!! info "How to read a table entry"\n')
        f.write("    - **PK** is the primary key. **Unique** lists other column sets that must be unique.\n")
        f.write("    - **Foreign keys** are relationships the database enforces.\n")
        f.write("    - **Likely links (no FK)** are joins the application makes in code but the database does not enforce. ")
        f.write("They're inferred from column names, so treat them as hints.\n\n")
        f.write(f"**{len(tables)} tables** in total.\n\n| Prefix | Tables | Database |\n|---|---|---|\n")
        for fam, names in sorted(fams.items()):
            dbs = ", ".join(sorted({db_of[n] for n in names}))
            f.write(f"| [{FAMILY_TITLES.get(fam, fam + '_*')}]({fam.lower()}.md) | {len(names)} | {dbs} |\n")

    for fam, names in sorted(fams.items()):
        with open(os.path.join(out, f"{fam.lower()}.md"), "w") as f:
            f.write(f"# {FAMILY_TITLES.get(fam, fam + '_*')}\n\n")
            f.write(f"{len(names)} tables. Generated from the {version} DDL.\n\n")
            for name in names:
                t = tables[name]
                f.write(f"## {name}\n\n")
                f.write(f"*{db_of[name]}* · PK: `{', '.join(t['pk']) or '—'}`")
                if t["unique"]:
                    f.write(" · Unique: " + "; ".join(f"`{', '.join(u)}`" for u in t["unique"]))
                f.write("\n\n| Column | Type | Notes |\n|---|---|---|\n")
                fk_cols = {c: fk for fk in t["fks"] for c in fk["cols"]}
                for c in t["columns"]:
                    notes = []
                    if c["name"] in t["pk"]:
                        notes.append("PK")
                    if c["name"] in fk_cols:
                        notes.append("FK → " + fk_cols[c["name"]]["ref_table"])
                    extra = c["extra"].replace("|", "\\|")
                    if extra:
                        notes.append(extra)
                    f.write(f"| `{c['name']}` | `{c['type']}` | {' · '.join(notes)} |\n")
                if t["fks"]:
                    f.write("\n**Foreign keys**\n\n")
                    for fk in t["fks"]:
                        od = f" (on delete: {fk['on_delete']})" if fk["on_delete"] else ""
                        f.write(f"- `{', '.join(fk['cols'])}` → {link(fk['ref_table'], fam)}"
                                f" `{', '.join(fk['ref_cols'])}`{od}\n")
                if referenced_by.get(name):
                    f.write("\n**Referenced by**\n\n")
                    for src, fk in sorted(referenced_by[name], key=lambda x: x[0]):
                        f.write(f"- {link(src, fam)} via `{', '.join(fk['cols'])}`\n")
                if logical.get(name):
                    f.write("\n**Likely links (no FK)**\n\n")
                    for col, tgt, why in logical[name]:
                        f.write(f"- `{col}` → {link(tgt, fam)} *({why})*\n")
                f.write("\n")
    print(f"{version}: {len(tables)} tables across {len(fams)} families → {out}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
