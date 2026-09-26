---
name: apim-mkdocs-publisher
description: Build, update and publish the MkDocs (Material) documentation site that explains the WSO2 API Manager database: one section for the 4.x series and one for the 3.x series, plus a comparison. Written in simple terms, with small easy-to-follow Mermaid diagrams, and published to GitHub Pages via GitHub Actions. Use when the user asks to create, regenerate, extend, fix, preview or publish the APIM DB docs site, add a new APIM version or series to it, or document a new domain or flow there.
---

# APIM DB docs: MkDocs site builder & publisher

This skill turns what the **`apim-db-explorer`** skill finds into a published documentation site. The explorer is the research step and this skill is the writing and publishing step. Read `.claude/skills/apim-db-explorer/SKILL.md` first: it defines the domains, the relationship rules and the core flows used below.

## Repository layout

```
.                              ← git repo root (the wso2am-* product folders are git-ignored)
├── mkdocs.yml                 ← site config + the explicit nav (source of truth for page list)
├── requirements.txt           ← pinned mkdocs / mkdocs-material
├── .github/workflows/docs.yml ← builds with --strict and deploys to GitHub Pages on push to main
├── .claude/skills/
│   ├── apim-db-explorer/      ← research skill + scripts/schema_map.py (DDL parser)
│   └── apim-mkdocs-publisher/ ← this skill + scripts/gen_reference.py
└── docs/
    ├── index.md, how-to-read.md, glossary.md, comparison.md
    ├── assets/extra.css
    ├── apim-4/                ← 4.x series (currently documented from wso2am-4.7.0)
    │   ├── index.md  databases.md  gotchas.md  identity-tables.md
    │   ├── domains/*.md       ← one page per domain (hand-written)
    │   ├── flows/*.md         ← one page per core flow (hand-written)
    │   └── reference/*.md     ← GENERATED: every table, every column
    └── apim-3/                ← 3.x series (currently documented from wso2am-3.2.0), same shape
```

A series folder is named after its major version line (`apim-4`, `apim-3`). Its `index.md` must say which exact product version it was generated from.

## Environment

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve          # live preview at http://127.0.0.1:8000
.venv/bin/mkdocs build --strict # must pass before any commit: it catches broken links and missing nav pages
```

## Workflow

1. **Research.** Run the `apim-db-explorer` steps 1–5 for each product folder, e.g. `wso2am-4.7.0` → `apim-4` and `wso2am-3.2.0` → `apim-3`. Keep the maps in the scratchpad.
2. **Regenerate the reference pages.** Never hand-edit these:
   ```bash
   .venv/bin/python .claude/skills/apim-mkdocs-publisher/scripts/gen_reference.py wso2am-4.7.0 docs/apim-4/reference
   .venv/bin/python .claude/skills/apim-mkdocs-publisher/scripts/gen_reference.py wso2am-3.2.0 docs/apim-3/reference
   ```
3. **Write or update the hand-written pages** using the page templates and writing rules below. The nav in `mkdocs.yml` lists every page. If you add or remove a page, update the nav in the same change.
4. **Check completeness.** Every core table (as defined by the explorer's classification) must be explained on exactly one domain page, under a `### TABLE_NAME` heading. Peripheral tables go on `identity-tables.md` with one line each. Run the coverage check below and fix any gaps.
5. **Build with `--strict`.** Fix every warning.
6. **Publish.** Commit, then push to `main`. The workflow deploys to Pages. For first-time setup, see "Publishing" below.

### Coverage check

```bash
for s in apim-4 apim-3; do
  comm -23 <(grep -h '^## ' docs/$s/reference/*.md | sed 's/## //' | sort -u) \
           <(grep -rhoE '^### `?[A-Z0-9_]+' docs/$s/domains docs/$s/identity-tables.md | sed -E 's/### `?//' | sort -u) \
    | sed "s/^/$s missing: /"
done
```
When the check is clean it prints nothing. `identity-tables.md` lists tables as `### TABLE` headings grouped under `##` family headings, or else as bullets that start with a `### ` heading per group. Whichever you choose, make sure the grep above can see each table name.

## Writing rules (the most important part)

The audience is a developer or support engineer who is new to APIM. Explain things so they understand them after one read.

- **Official, neutral tone.** Write the site like product documentation: present tense, stating how APIM behaves. **Never describe how the content was produced.** That rules out:
  - "verified", "confirmed", "observed", "on a running server" and "in our tests";
  - "inferred", "not tested", "evidence", "snapshot" and "diff";
  - "this site was generated from...".

  If a fact is uncertain, leave it out, or state the genuine configuration condition ("only when database artifact synchronization is enabled"). Never hedge by describing the research. Use "you" and "APIM", not "we" or "I", and call example rows "Example".
- **Plain language first, then details.** Start each concept with what it means in real life ("An *application* is how a developer's app identifies itself to APIM"), then name the table, then list the columns.
- **Use one everyday analogy per domain at most**, and only where it genuinely helps.
- Keep sentences short and use active voice. Define an acronym the first time you use it on a page (KM, JWT, VHost, LC and so on), or link to the glossary.
- **Put the table name in backticks and link it to its reference entry**: `` [`AM_API`](../reference/am.md#am_api) ``. Anchors are the lower-cased table name.
- **Never lose information.** For every core table, say what one row represents, list its important columns with their meaning, show how it connects to other tables (cardinality, FK or logical, what happens on delete), and add any gotchas. Leave the full column list to the reference page.
- Call out undeclared joins explicitly with a `!!! warning "Logical link (no foreign key)"` admonition or an inline "*(logical link, no FK)*".
- Mark version-specific facts with admonitions: `!!! note "Different in 3.x"` / `!!! note "New in 4.x"`, and link across to the other series.
- Show **example rows** with realistic values in small Markdown tables, for example the PizzaShack API, a DefaultApplication, and the Gold tier. Examples make the relationships concrete.
- Add a **"Try it"** read-only SQL query where it helps, e.g. the join that answers "which apps are subscribed to API X?". Only use `SELECT`s, and only columns that exist in that version.
- Don't paste raw DDL.

## Diagram rules (keep them easy)

Every diagram is Mermaid in a fenced ` ```mermaid ` block. Material renders it and themes it for light and dark mode.

- **One idea per diagram.** If a diagram needs a paragraph to explain it, split it.
- **Size limits:** a flowchart has at most about 8 nodes, a sequenceDiagram at most 5 participants and about 10 messages, and an erDiagram at most about 6 entities.
- ER entities show **only key columns**: the PK, the FKs and at most one or two identifying columns. You can also show no attributes at all. Put the full columns in the reference.
- Use a solid line for a declared FK. Use a dashed line (`..` in erDiagram, `-.->` in flowchart) labelled "logical" for joins that aren't FKs.
- Put **one sentence before** each diagram saying what it shows. After it, add at most three bullets on how to read it.
- Use plain labels ("Developer creates app") rather than method names. Participants are roles or components (Publisher, Dev Portal, Key Manager, Gateway, Database), not Java classes.
- Don't use custom colours, `classDef` or `style` lines, or HTML in labels. The theme handles the look.
- Choose the type that fits: `flowchart LR` for "what connects to what" and step order, `sequenceDiagram` for "who talks to whom, and which tables get written", and `erDiagram` for table relationships.

## Page templates

### Domain page (`<series>/domains/<domain>.md`)

```markdown
# <Domain name>

!!! abstract "In one sentence"
    <what this domain stores and why APIM needs it>

## The idea
<2–4 short paragraphs in plain language. Optional single analogy.>

## How the tables connect
<one sentence> + small erDiagram (split into two if > ~6 tables) + ≤3 bullets

## The tables
### AM_EXAMPLE
**One row =** <plain meaning>.
| Column | What it means |   ← only the important columns (5–8)
**Connects to:** <table> — <cardinality>, <FK / logical>, <on delete>.
**Watch out:** <gotchas, if any>
[Full column list](../reference/am.md#am_example)

(repeat for every core table of the domain)

## Example
<small example rows across 2–3 tables showing one real relationship>

## Try it
<read-only SQL>

## Related flows
- [<flow>](../flows/<flow>.md)
```

### Flow page (`<series>/flows/<nn>-<flow>.md`)

```markdown
# <Flow name>

!!! abstract "What happens"
    <who does what, in one or two sentences>

**Who:** <portal/component> · **Tables written:** `A`, `B`, `C` · **Tables read:** `D`

## The flow at a glance
small sequenceDiagram (roles → Database), ≤10 messages

## Step by step
1. **<Step>** → writes [`TABLE`](../reference/..) — <which columns, which link to the previous step>
   (example row)
...

## What gets cleaned up
<what happens on delete: cascade vs restrict>

## Try it
<SELECT that shows the result of the flow>

!!! note "Different in 3.x/4.x"
    <link to the equivalent page in the other series>
```

## Site-level pages

- `docs/index.md`: what the site is, who it's for, the two series (as cards linking to each), and how to use the site.
- `docs/how-to-read.md`: the diagram legend (solid vs dashed lines, crow's-foot notation explained in plain words), how the pages are organised, and what "logical link" means.
- `docs/glossary.md`: APIM terms (API, API product, revision, gateway environment, VHost, application, subscription, key manager, consumer key, tier/policy, scope, lifecycle, tenant, organization, registry, and so on), each in one or two plain sentences.
- `docs/comparison.md`: 3.x vs 4.x. Cover the added, removed and renamed tables, the changes to the core tables, how each flow changed, and one simple before/after diagram per big change.

## Live verification (run the flows on a real server)

The schema alone can't show write order or which tables really get touched. To confirm the flow pages, run each flow once against a running server and diff the database after every step. The scripts are in `scripts/verify/`:
- `snap.sh` dumps both DBs with H2 `SCRIPT SIMPLE`;
- `diff.py` reports the rows inserted, deleted or updated per table;
- `step.sh` takes a snapshot and diffs it against the previous one.

1. **Back up first.** Copy `repository/database/*.mv.db` and `repository/conf/deployment.toml` to the scratchpad. Restore both when you're done, and confirm nothing is left in the product folder.
2. **Let the snapshot tool read the live DB.** Append `;AUTO_SERVER=TRUE` to the `apim_db` and `shared_db` H2 URLs.
   - H2 2.x (APIM 4.x) rejects `AUTO_SERVER` together with `DB_CLOSE_ON_EXIT=FALSE`, so drop that flag there.
   - H2 1.4 (APIM 3.x) accepts both.
3. **Use the right Java.**
   - 4.7.0 needs **Java 21** (class version 65), and fails on 17.
   - 3.2.0 needs **Java 8** (or 11).
   - If the JDK is missing, download a Temurin JDK archive into the scratchpad rather than installing it system-wide.
   - Start the server with `bin/api-manager.sh` (4.x) or `bin/wso2server.sh` (3.x), run it in the background, and wait for `WSO2 Carbon started in`.
4. **Take the baseline snapshots.**
   ```bash
   export VERIFY_OUT=<scratchpad>/verify JAVA=<jdk>/bin/java
   S=.claude/skills/apim-mkdocs-publisher/scripts/verify
   $S/snap.sh wso2am-X 00-pristine <dir with the backed-up .mv.db copies>   # shipped state
   $S/step.sh wso2am-X 01-after-startup                                      # what startup seeds
   ```
   To diff 00 against 01, run `diff.py` by hand. Use a new label for every step: `step.sh` refuses to reuse one.
5. **Drive each flow over REST**, then run `step.sh` after every action. Register a DCR client and get the admin token **before** the flow snapshots, so they don't show up in the flow diffs.

   | | 4.x | 3.x |
   |---|---|---|
   | Publisher | `/api/am/publisher/v4` | `/api/am/publisher/v1` |
   | Dev Portal | `/api/am/devportal/v3` | `/api/am/store/v1` |
   | Admin | `/api/am/admin/v4` | `/api/am/admin/v1` |

   For the flow calls, run a tiny local backend (e.g. `python3 -m http.server`) as the API endpoint.
6. **Read the diffs, and ignore the noise.** The noise is:
   - `REG_LOG`;
   - `AM_GW_INSTANCES` heartbeats (4.x);
   - background governance re-runs (4.x);
   - the REST client's own OAuth rows.

   A table showing both `+N` and `-N` is an update. Then correct the flow and domain pages. The verification only informs the content: **don't mention it in the docs**, and state the resulting facts in the neutral documentation tone.

Things that trip up the REST calls:
- **Approval workflows** are set in the registry file `/_system/governance/apimgt/applicationdata/workflow-extensions.xml`, not in tenant-config. Read and update it through the `ResourceAdminService` SOAP endpoint (`getTextContent` / `updateTextContent`, basic auth). Swap `*SimpleWorkflowExecutor` for `*ApprovalWorkflowExecutor`, then approve through the Admin API's `workflows/update-workflow-status?workflowReferenceId=<WF_EXTERNAL_REFERENCE>`.
- **API keys (4.x):** the generate call needs a `keyName`.
- **Gateway environments (3.x):** an API created without `gatewayEnvironments` is published but not deployed, so the gateway returns 404. Set `["Production and Sandbox"]`.
- **Admin v1 (3.x):** limit types are upper-case (`REQUESTCOUNTLIMIT`), and block conditions go to `/throttling/blacklist` with `{"fixedIp": ...}`.
- **Portal-only rows:** `AM_SYSTEM_APPS` and similar rows are only created when someone logs into the portals in a browser, so REST-only runs won't show them.

## Publishing (GitHub Pages)

The first-time setup needs `gh` to be logged in (`gh auth status`). If it isn't, ask the user to run `! gh auth login`.

```bash
git init -b main   # if not already a repo
git add -A && git commit -m "..."
gh repo create <name> --public --source . --remote origin --push
gh api -X POST repos/{owner}/<name>/pages -f build_type=workflow   # enable Pages via Actions (once)
gh run watch    # wait for the "docs" workflow
```

Set `site_url` and `repo_url` in `mkdocs.yml` to the real owner and repo name. The site ends up at `https://<owner>.github.io/<name>/`.

After that, every push to `main` redeploys the site. Never commit the `wso2am-*` product folders, `.venv/` or `site/`. Before committing, check that `.gitignore` covers them (`git status --ignored`).

## Adding a new APIM version

- **Same series** (e.g. 4.8.0 replacing 4.7.0): regenerate that series' reference pages from the new product. Diff the old and new maps and update the affected domain and flow pages. Update the version stated in the series `index.md`, and add a line to `comparison.md` if something notable changed.
- **New series** (e.g. 5.x): copy the page structure of the nearest series into `docs/apim-5/` and add it to the nav and the home page cards. Then write the content against the new maps and extend `comparison.md`.
