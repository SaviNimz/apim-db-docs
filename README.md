# WSO2 API Manager: Database Guide

A plain-language guide to the WSO2 API Manager database, covering the **4.x** series (from 4.7.0) and the **3.x** series (from 3.2.0). It explains what each table is for, how the tables relate, and which tables each core user flow touches, with simple diagrams.

📖 **Read it online:** https://SaviNimz.github.io/apim-db-docs/

## Run locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve        # http://127.0.0.1:8000
```

## How it's built

| Piece | Where |
|---|---|
| Site config and navigation | `mkdocs.yml` |
| Hand-written pages (overviews, domains, flows) | `docs/` |
| Generated table reference (every table and column) | `docs/apim-*/reference/`, created by `.claude/skills/apim-mkdocs-publisher/scripts/gen_reference.py` |
| DDL parser | `.claude/skills/apim-db-explorer/scripts/schema_map.py` |
| Claude Code skills that research and regenerate the docs | `.claude/skills/apim-db-explorer`, `.claude/skills/apim-mkdocs-publisher` |
| Live verification (snapshot and diff the DB while running each flow) | `.claude/skills/apim-mkdocs-publisher/scripts/verify/`, with the procedure in that skill |
| Deployment | `.github/workflows/docs.yml`: builds with `--strict` and publishes to GitHub Pages on every push to `main` |

To regenerate the reference pages, put the product distributions (e.g. `wso2am-4.7.0/`, `wso2am-3.2.0/`) in the repo root. They're git-ignored. Then run:

```bash
.venv/bin/python .claude/skills/apim-mkdocs-publisher/scripts/gen_reference.py wso2am-4.7.0 docs/apim-4/reference
.venv/bin/python .claude/skills/apim-mkdocs-publisher/scripts/gen_reference.py wso2am-3.2.0 docs/apim-3/reference
```

WSO2 and WSO2 API Manager are trademarks of WSO2 LLC. This is an independent community guide derived from the database scripts shipped with the Apache-2.0-licensed product.
