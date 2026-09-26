#!/usr/bin/env python3
"""Parse a WSO2 APIM MySQL DDL script -> tables, columns, PKs, uniques, explicit FKs, implicit join candidates."""
import re, sys, json
from collections import defaultdict

def cols(s):
    return [c.strip(" `").upper() for c in s.split(",")]

def add_constraint(t, p):
    """Record a PK/UNIQUE/FK clause (optionally prefixed by CONSTRAINT <name>). Returns False if p is not one."""
    body = re.sub(r"^CONSTRAINT\s+`?\w+`?\s+", "", p.strip(), flags=re.I)
    u = body.upper()
    if u.startswith("PRIMARY KEY"):
        t["pk"] = cols(re.search(r"\((.*?)\)", body).group(1))
    elif u.startswith("FOREIGN KEY"):
        fm = re.search(r"FOREIGN\s+KEY\s*\((.*?)\)\s*REFERENCES\s+`?(\w+)`?\s*\((.*?)\)(.*)", body, re.I | re.S)
        if fm:
            od = re.search(r"ON\s+DELETE\s+(NO\s+ACTION|SET\s+NULL|SET\s+DEFAULT|\w+)", fm.group(4), re.I)
            t["fks"].append({"cols": cols(fm.group(1)), "ref_table": fm.group(2).upper(),
                             "ref_cols": cols(fm.group(3)), "on_delete": " ".join(od.group(1).upper().split()) if od else None})
    elif u.startswith("UNIQUE"):
        um = re.search(r"\((.*?)\)", body)
        if um: t["unique"].append(cols(um.group(1)))
    else:
        return False
    return True

def parse(path):
    sql = open(path, encoding="utf-8", errors="ignore").read()
    sql = re.sub(r"--[^\n]*", "", sql)
    sql = re.sub(r"/\*.*?\*/", "", sql, flags=re.S)
    tables = {}
    for m in re.finditer(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?`?(\w+)`?\s*\(", sql, re.I):
        name, i, depth = m.group(1).upper(), m.end(), 1
        j = i
        while depth and j < len(sql):
            depth += {"(": 1, ")": -1}.get(sql[j], 0); j += 1
        body = sql[i:j-1]
        parts, buf, d = [], "", 0
        for ch in body:
            if ch == "(": d += 1
            if ch == ")": d -= 1
            if ch == "," and d == 0: parts.append(buf.strip()); buf = ""
            else: buf += ch
        if buf.strip(): parts.append(buf.strip())
        t = {"columns": [], "pk": [], "unique": [], "fks": []}
        for p in parts:
            if not add_constraint(t, p):
                u = p.upper()
                if re.match(r"(KEY|INDEX|CHECK)\b", u):
                    continue
                cm = re.match(r"`?(\w+)`?\s+([\w]+(?:\s*\([^)]*\))?)(.*)", p, re.S)
                if cm:
                    col = cm.group(1).upper()
                    t["columns"].append({"name": col, "type": cm.group(2).upper(), "extra": " ".join(cm.group(3).split())[:80]})
                    if "PRIMARY KEY" in cm.group(3).upper(): t["pk"] = [col]
        tables[name] = t
    # Constraints added after the fact: ALTER TABLE X ADD [CONSTRAINT n] FOREIGN KEY/UNIQUE/PRIMARY KEY ...
    for m in re.finditer(r"ALTER\s+TABLE\s+`?(\w+)`?\s+ADD\s+(.*?);", sql, re.I | re.S):
        if m.group(1).upper() in tables:
            add_constraint(tables[m.group(1).upper()], m.group(2).strip())
    return tables

def implicit(tables):
    """Columns that look like joins but have no declared FK (logical relationships)."""
    owners = defaultdict(set)  # column name -> tables where it is (part of) PK or UNIQUE
    for n, t in tables.items():
        for c in t["pk"] + [c for u in t["unique"] for c in u]:
            owners[c].add(n)
    # (table-prefix, column) -> target table. Prefix "" matches any table.
    hints = {("", "API_UUID"): "AM_API", ("", "REVISION_UUID"): "AM_REVISION", ("", "CONSUMER_KEY"): "IDN_OAUTH_CONSUMER_APPS",
             ("AM_", "KEY_MANAGER"): "AM_KEY_MANAGER", ("", "KEY_MANAGER_UUID"): "AM_KEY_MANAGER", ("", "LABEL_UUID"): "AM_LABEL",
             ("", "APPLICATION_UUID"): "AM_APPLICATION", ("AM_", "SUBSCRIBER_ID"): "AM_SUBSCRIBER", ("AM_", "APPLICATION_ID"): "AM_APPLICATION",
             ("AM_", "API_ID"): "AM_API", ("AM_", "APP_ID"): "AM_APPLICATION", ("SP_", "APP_ID"): "SP_APP", ("", "URL_MAPPING_ID"): "AM_API_URL_MAPPING",
             ("IDN_OAUTH2_", "TOKEN_ID"): "IDN_OAUTH2_ACCESS_TOKEN", ("", "SCOPE_ID"): "IDN_OAUTH2_SCOPE", ("GOV_", "POLICY_ID"): "GOV_POLICY",
             ("GOV_", "RULESET_ID"): "GOV_RULESET", ("", "LLM_PROVIDER_UUID"): "AM_LLM_PROVIDER"}
    def hint(n, cn):
        best = None
        for (pre, col), tgt in hints.items():
            if col == cn and n.startswith(pre) and (best is None or len(pre) > len(best[0])):
                best = (pre, tgt)
        return best[1] if best else None
    out = []
    for n, t in tables.items():
        declared = {c for fk in t["fks"] for c in fk["cols"]}
        for c in t["columns"]:
            cn = c["name"]
            target = hint(n, cn)
            if cn in declared or target == n:
                continue
            if target and target != n and target in tables:
                out.append((n, cn, target, "name-hint"))
            elif cn.endswith(("_ID", "_UUID")) and cn != "TENANT_ID" and cn not in t["pk"]:
                cands = sorted(owners.get(cn, set()) - {n})
                if len(cands) == 1:
                    out.append((n, cn, cands[0], "same-name key"))
    return out

if __name__ == "__main__":
    tables = {}
    for p in sys.argv[1:]:
        if p.startswith("--"): continue
        tables.update(parse(p))
    if "--json" in sys.argv:
        print(json.dumps(tables, indent=1)); sys.exit()
    fam = defaultdict(list)
    for n in sorted(tables): fam[n.split("_")[0]].append(n)
    print(f"# {len(tables)} tables")
    for f, ns in sorted(fam.items()): print(f"- {f}_*: {len(ns)}")
    print()
    for n in sorted(tables):
        t = tables[n]
        print(f"## {n}")
        print("  cols: " + ", ".join(f"{c['name']}:{c['type']}" for c in t["columns"]))
        print(f"  pk: {t['pk']}  unique: {t['unique']}")
        for fk in t["fks"]:
            print(f"  FK {fk['cols']} -> {fk['ref_table']}{fk['ref_cols']} on_delete={fk['on_delete']}")
    print("\n# Implicit (undeclared) relationship candidates — verify before trusting")
    for n, c, tgt, why in implicit(tables):
        print(f"- {n}.{c} ~> {tgt}  ({why})")
