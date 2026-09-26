---
name: apim-db-explorer
description: Explore and explain the database schema of a WSO2 API Manager distribution (works for both the 3.x line, e.g. wso2am-3.2.0, and the 4.x line, e.g. wso2am-4.7.0). Maps every table, groups core tables into domains, works out explicit and implicit entity relationships, and walks through the core user flows (API design → revision → gateway deployment → lifecycle/publish → subscribe → key generation → token → invocation → throttling → revocation) table by table. Use whenever the user asks to understand, document, compare or trace the APIM database, entity relationships, "which tables are written when X happens", ER diagrams for API Manager, or migration differences between two APIM versions.
---

# WSO2 API Manager — Database Explorer

The goal is a **plain-language picture of the whole APIM data model**. That means:
- what each core table is *for*,
- how the tables connect, including relationships the DDL never declares,
- which rows get written, and in what order, during each core user flow.

Nothing core may be dropped. Every table has to show up somewhere in the output, even if only as a one-line entry in the peripheral appendix.

Treat the DDL in the target distribution as the source of truth. The "landmarks" in this file are there to help you get your bearings. If they disagree with the scripts, the scripts win. Say so in the report.

---

## 0. Inputs and where things live

Ask for (or infer) the **product directory**, e.g. `wso2am-3.2.0` or `wso2am-4.7.0`. If there are several `wso2am-*` folders in the working directory and the user didn't pick one, document each one, then add a comparison section (step 7).

| What | Path (relative to the product home) | Notes |
|---|---|---|
| **APIM DB DDL** (`apim_db`, `WSO2AM_DB`) | `dbscripts/apimgt/<vendor>.sql` | AM_*, IDN_*, IDP_*, SP_*, CM_*, WF_*, FIDO*, and GOV_* (4.x). This is the main one. |
| **Shared DB DDL** (`shared_db`, `WSO2SHARED_DB`) | `dbscripts/<vendor>.sql` | REG_* (registry) and UM_* (users, roles, tenants, and in 4.x organizations). |
| Other DDL (supporting only) | `dbscripts/mb-store/`, `dbscripts/metrics/`, `dbscripts/multi-dc/` | Message-broker store, metrics, multi-DC variants. Mention them briefly. |
| Migration scripts (3.x only) | `dbscripts/migration-*` | Very old history. Skip unless asked. |
| Sample data | `dbscripts/apimgt/h2-sample-data.sql` | Handy for showing example rows. |
| Datasource config | `repository/conf/deployment.toml` → `[database.apim_db]`, `[database.shared_db]` | Tells you which physical DB each logical DB points to. |
| Live embedded DBs | `repository/database/*.mv.db` | H2 files: WSO2AM_DB, WSO2SHARED_DB, WSO2CARBON_DB (local registry), WSO2MB_DB, WSO2METRICS_DB. |
| H2 driver | `repository/components/plugins/h2*.jar` | 3.x ships H2 1.4.x and 4.x ships H2 2.x. Use the jar from **the same product**, because the file formats are incompatible. |

**Always parse `mysql.sql`.** Its FK/PK/UNIQUE syntax is the cleanest, and every vendor script defines the same logical schema. Only open another vendor's script if the user asks about vendor-specific details such as Oracle sequences and triggers, or MSSQL `IF NOT EXISTS` blocks.

## 1. Build the raw schema map (mechanical, complete)

Run the bundled parser. It lives next to this file at `scripts/schema_map.py`:

```bash
P=<product-dir>
python3 .claude/skills/apim-db-explorer/scripts/schema_map.py $P/dbscripts/apimgt/mysql.sql $P/dbscripts/mysql.sql > <scratchpad>/map-$(basename $P).txt
# add --json for machine-readable output
```

The output includes:
- a count of tables per prefix family,
- every table with its columns, PK, UNIQUE keys and declared FKs (including the ON DELETE behaviour),
- a list of **implicit relationship candidates**: columns that clearly join to another table but have no FK.

If the script is missing, rebuild the same information yourself with grep/awk over the `CREATE TABLE` blocks. Don't skip this step. Everything later depends on having the full inventory.

Check that the table count in the map matches `grep -ciE "CREATE TABLE" <file>`, and that the FK count matches `grep -ci "FOREIGN KEY"` (the parser also reads `ALTER TABLE ... ADD CONSTRAINT` FKs and named `CONSTRAINT x PRIMARY KEY` clauses). Explain any difference: MSSQL-style `IF NOT EXISTS` wrappers, or tables created twice.

## 2. Classify every table

Put **every** table in exactly one bucket.

It's worth checking whether a table is actually used. Some are defined in the DDL but never used by the shipped code. In 3.2 these include `AM_SCOPE`, `AM_SCOPE_BINDING`, `AM_POLICY_HARD_THROTTLING`, `AM_API_LC_PUBLISH_EVENTS` and `AM_USAGE_UPLOADED_FILES`. To confirm, grep the product jars under `repository/components/plugins/` for the table name (`unzip -p <jar> | grep -c TABLE`), and label these tables "defined but unused".

**Core (full treatment).** These are the tables APIM's own flows read and write:
- all `AM_*` tables,
- all `GOV_*` tables (4.x),
- the OAuth tables APIM relies on: `IDN_OAUTH_CONSUMER_APPS`, `IDN_OAUTH2_ACCESS_TOKEN`, `IDN_OAUTH2_ACCESS_TOKEN_SCOPE`, `IDN_OAUTH2_AUTHORIZATION_CODE`, `IDN_OAUTH2_SCOPE`, `IDN_OAUTH2_SCOPE_BINDING`, `IDN_OAUTH2_RESOURCE_SCOPE`, `IDN_OAUTH_CONSUMER_SECRETS` (4.x), `IDN_INVALID_TOKENS` (4.x), and the `*_REVOKED_EVENT` tables,
- the workflow tables `AM_WORKFLOWS` and `WF_*`,
- the identity/registry anchors: `UM_TENANT`, `UM_USER`, `UM_ROLE`, `UM_USER_ROLE`, `UM_HYBRID_ROLE`, `UM_HYBRID_USER_ROLE`, `REG_RESOURCE`, `REG_PATH`, `REG_CONTENT`, `REG_PROPERTY`, `REG_RESOURCE_PROPERTY`, `REG_ASSOCIATION`, and `UM_ORG*` (4.x).

**Peripheral (appendix, one line each).** These come from the embedded Identity Server and aren't central to APIM flows: `SP_*`, `IDP_*`, `CM_*`, `FIDO*`, `IDN_UMA_*`, `IDN_SAML2_*`, `IDN_OPENID_*`, `IDN_AUTH_*` sessions, `IDN_CLAIM*`, `IDN_RECOVERY_DATA`, `IDN_PASSWORD_HISTORY_DATA`, `IDN_CONFIG_*`, `IDN_REMOTE_FETCH_*`, `IDN_SECRET*`, `IDN_OIDC_*`, CIBA/device-flow tables, and the remaining `REG_*` and `UM_*` tables.
- Keep one exception in mind: **`SP_APP` becomes core** when explaining key generation. On 3.x and on 4.x with the Resident Key Manager, every OAuth app generated for an APIM application also creates a service provider.

Then split the core tables into **domains**. Use the list below as a starting point, and add a domain if a version introduces a new family.

| Domain | Typical tables (check they exist in this version) |
|---|---|
| Tenancy, users & orgs | UM_TENANT, UM_USER, roles, UM_ORG* (4.x), AM_ORGANIZATION_MAPPING (4.x), AM_USER, AM_SYSTEM_CONFIGS (4.x), AM_TENANT_THEMES |
| API definition | AM_API, AM_API_URL_MAPPING, AM_API_DEFAULT_VERSION, AM_API_CATEGORIES, AM_GRAPHQL_COMPLEXITY, AM_API_CLIENT_CERTIFICATE, AM_CERTIFICATE_METADATA, AM_API_ENDPOINTS / AM_API_PRIMARY_EP_MAPPING (4.x), AM_API_METADATA (4.x), AM_API_SERVICE_MAPPING + AM_SERVICE_CATALOG (4.x), AM_API_EXTERNAL_API_MAPPING, AM_API_AI_CONFIGURATION + AM_LLM_PROVIDER* (4.x), AM_API_SEQUENCE_BACKEND (4.x) |
| MCP servers & AI (4.x) | AM_API_AI_CONFIGURATION, AM_LLM_PROVIDER, AM_LLM_PROVIDER_MODEL, AM_API_OPERATION_MAPPING (MCP tool → API operation), AM_BACKEND, AM_BACKEND_OPERATION_MAPPING (MCP servers have API_TYPE `MCP`) |
| Scopes & resource security | AM_SCOPE, AM_SCOPE_BINDING, AM_SHARED_SCOPE, AM_API_RESOURCE_SCOPE_MAPPING, IDN_OAUTH2_SCOPE, IDN_OAUTH2_SCOPE_BINDING, IDN_OAUTH2_RESOURCE_SCOPE |
| Mediation / operation policies (4.x) | AM_OPERATION_POLICY, AM_OPERATION_POLICY_DEFINITION, AM_COMMON_OPERATION_POLICY, AM_API_OPERATION_POLICY, AM_API_OPERATION_POLICY_MAPPING, AM_API_POLICY_MAPPING, AM_GATEWAY_POLICY_* |
| API products | AM_API_PRODUCT_MAPPING (an API product is a row in AM_API whose API_TYPE is `'APIProduct'`; the casing matters in SQL) |
| Revisions & deployment (4.x) | AM_REVISION, AM_API_REVISION_METADATA, AM_DEPLOYMENT_REVISION_MAPPING, AM_DEPLOYED_REVISION, AM_GATEWAY_ENVIRONMENT, AM_GW_VHOST, AM_GATEWAY_PERMISSIONS, AM_GW_INSTANCES, AM_GW_INSTANCE_ENV_MAPPING, AM_GW_REVISION_DEPLOYMENT, AM_GW_API_DEPLOYMENTS, AM_GATEWAY_TOKEN, AM_GW_PLATFORM_* |
| Gateway artifact sync | AM_GW_PUBLISHED_API_DETAILS, AM_GW_API_ARTIFACTS (3.x uses GATEWAY_LABEL + GATEWAY_INSTRUCTION; 4.x uses REVISION_ID), AM_ARTIFACT (4.x) |
| Lifecycle & labels | AM_API_LC_EVENT, AM_API_LC_PUBLISH_EVENTS, AM_LABELS + AM_LABEL_URLS (3.x: microgateway labels) vs AM_LABEL + AM_API_LABEL_MAPPING (4.x: API labels) |
| Developer portal / consumers | AM_SUBSCRIBER, AM_APPLICATION, AM_APPLICATION_ATTRIBUTES, AM_APPLICATION_GROUP_MAPPING, AM_SUBSCRIPTION, AM_API_COMMENTS, AM_API_RATINGS, AM_DEVPORTAL_* (4.x), AM_WEBHOOKS_* (4.x) |
| Keys, key managers & tokens | AM_KEY_MANAGER, AM_KEY_MANAGER_PERMISSIONS / ALLOWED_ORGS (4.x), AM_APPLICATION_REGISTRATION, AM_APPLICATION_KEY_MAPPING, AM_APP_KEY_DOMAIN_MAPPING, AM_SUBSCRIPTION_KEY_MAPPING (3.x), AM_API_KEY* (4.x), AM_SYSTEM_APPS, IDN_OAUTH_CONSUMER_APPS, IDN_OAUTH2_ACCESS_TOKEN(+_SCOPE, _AUDIT), IDN_OAUTH_CONSUMER_SECRETS |
| Revocation | AM_REVOKED_JWT, AM_APP_REVOKED_EVENT, AM_SUBJECT_ENTITY_REVOKED_EVENT, IDN_*_REVOKED_EVENT, IDN_INVALID_TOKENS |
| Throttling / rate-limit policies | AM_POLICY_SUBSCRIPTION, AM_POLICY_APPLICATION, AM_API_THROTTLE_POLICY, AM_CONDITION_GROUP, AM_HEADER_FIELD_CONDITION, AM_QUERY_PARAMETER_CONDITION, AM_JWT_CLAIM_CONDITION, AM_IP_CONDITION, AM_POLICY_GLOBAL, AM_POLICY_HARD_THROTTLING, AM_BLOCK_CONDITIONS, AM_THROTTLE_TIER_PERMISSIONS, AM_TIER_PERMISSIONS |
| Workflows / approvals | AM_WORKFLOWS, WF_* |
| Governance (4.x) | GOV_RULESET*, GOV_POLICY*, GOV_ARTIFACT, GOV_REQUEST*, GOV_*_RUN, GOV_RULE_VIOLATION |
| Monetization, analytics, alerts, misc | AM_MONETIZATION*, AM_USAGE_UPLOADED_FILES, AM_ALERT_*, AM_NOTIFICATION_SUBSCRIBER, AM_SECURITY_AUDIT_UUID_MAPPING, AM_EXTERNAL_STORES, AM_CORRELATION_*, AM_TASK_LOCK, AM_TRANSACTION_RECORDS |

At the end, list any core table you haven't placed and place it. **Zero leftovers.**

## 3. Resolve relationships (explicit + implicit)

For each domain, write out its relationships in three kinds:

1. **Declared FKs**, taken from the map. Record the cardinality (look at whether the FK column is part of a PK or UNIQUE) and the ON DELETE behaviour. The behaviour matters: CASCADE means the child rows disappear, RESTRICT means the parent can't be deleted while children exist.
2. **Logical joins with no FK.** APIM leans on these heavily. Start from the parser's candidate list, then check each candidate by eye. The joins that always matter:
   - `AM_APPLICATION_KEY_MAPPING.CONSUMER_KEY` ↔ `IDN_OAUTH_CONSUMER_APPS.CONSUMER_KEY`. This is the bridge from an APIM application to an OAuth client.
   - `IDN_OAUTH2_ACCESS_TOKEN.CONSUMER_KEY_ID` → `IDN_OAUTH_CONSUMER_APPS.ID`, which leads to `IDN_OAUTH2_ACCESS_TOKEN_SCOPE`.
   - `AM_APPLICATION_KEY_MAPPING.KEY_MANAGER` / `AM_APPLICATION_REGISTRATION.KEY_MANAGER` → `AM_KEY_MANAGER`. In 3.x it stores the key manager's **name** (e.g. `Resident Key Manager`). In 4.x it stores the UUID, though migrated data may still hold names. Check which one you have.
   - `REVISION_UUID` columns → `AM_REVISION.REVISION_UUID`. How the working copy ("current API") is marked differs by table:
     - `AM_API_URL_MAPPING` uses `REVISION_UUID IS NULL`.
     - `AM_API_ENDPOINTS` and `AM_BACKEND` use `'Current API'`.
     - `AM_API_SEQUENCE_BACKEND` uses `'0'`.
     Check each table.
   - `AM_API_URL_MAPPING.API_ID` → `AM_API.API_ID`. There's no FK in either 3.x or 4.x.
   - `AM_GW_PUBLISHED_API_DETAILS.API_ID`, `AM_GW_API_ARTIFACTS.API_ID`, `AM_GW_REVISION_DEPLOYMENT.API_ID` and `AM_API_EXTERNAL_API_MAPPING.API_ID` hold the **API UUID string**, not the integer `AM_API.API_ID`. Don't trust the `_ID` suffix.
   - `AM_SCOPE.NAME` ↔ `IDN_OAUTH2_SCOPE.NAME`. In 3.2, `AM_SCOPE` and `AM_SCOPE_BINDING` are defined but never used, and the real scopes live in `IDN_OAUTH2_SCOPE`. In 4.x `AM_SCOPE` is used. and `AM_API_RESOURCE_SCOPE_MAPPING.SCOPE_NAME` ↔ scope name.
   - `AM_SUBSCRIPTION.TIER_ID` → `AM_POLICY_SUBSCRIPTION.NAME`, `AM_APPLICATION.APPLICATION_TIER` → `AM_POLICY_APPLICATION.NAME`, and `AM_API_URL_MAPPING.THROTTLING_TIER` → `AM_API_THROTTLE_POLICY.NAME`. These join by policy **name** plus tenant or organization.
   - `AM_SUBSCRIBER.USER_ID` → a user in the user store (`UM_USER.UM_USER_NAME`, or LDAP). `TENANT_ID` columns → `UM_TENANT.UM_ID`. `ORGANIZATION` columns (4.x) → a tenant domain or organization id.
   - `AM_WORKFLOWS.WF_REFERENCE` → the id of whatever the workflow is gating: a subscription, an application, an application registration, an API, and so on, depending on `WF_TYPE`.
   - `AM_API` ↔ `REG_RESOURCE`: the full API metadata lives in the registry. Think description, tags, visibility, endpoints on 3.x, business owner, lifecycle state. In **3.x** the API UUID is the registry artifact id (`REG_RESOURCE.REG_UUID`) and `AM_API` has no UUID column at all. In **4.x** `AM_API.API_UUID` carries it.
3. **Delete behaviour differs by version.** 3.x mostly uses `ON DELETE RESTRICT`, so the code must delete child rows first. 4.x changed many of these, such as subscriptions, key mappings, registrations and LC events, to `CASCADE`. Many newer 4.x FKs (GOV_*, AI/LLM, API-key mappings, backends) declare **no** ON DELETE clause, which means NO ACTION: they block the parent delete just like RESTRICT. Always read the ON DELETE clause from the actual DDL.
4. **Polymorphic / typed references.** For example: `AM_POLICY_*` rows chosen by `QUOTA_TYPE`, and `AM_WORKFLOWS` by `WF_TYPE`. Say which column acts as the type discriminator.

If a relationship is inferred rather than declared, label it that way ("logical, no FK"). If you checked it in code or in live data, say that too.

## 4. (Optional but valuable) Check against live data

Only do this if the user wants examples or you need to confirm a logical join. **Never open the live H2 files directly**, because a running server holds a lock on them and you risk corrupting them. Copy them first:

```bash
P=<product-dir>; S=<scratchpad>
cp $P/repository/database/WSO2AM_DB.mv.db $S/AM.mv.db
JAR=$(ls $P/repository/components/plugins/h2*.jar | head -1)   # use this product's own H2 version
java -cp "$JAR" org.h2.tools.Shell -url "jdbc:h2:$S/AM;IFEXISTS=TRUE" \
     -user wso2carbon -password wso2carbon -sql "SELECT API_NAME, API_VERSION FROM AM_API"
```

The default credentials are `wso2carbon`/`wso2carbon`; if these don't work, check `deployment.toml`. If the DB points at MySQL, Postgres or similar, ask before connecting, and only run read-only `SELECT`s. A fresh install is mostly empty. The DDL seeds almost nothing into `AM_*`, only lookups such as `AM_ALERT_TYPES`. The following rows are **created by server startup code, not SQL**: the default throttling policies, the Resident Key Manager, `AM_SYSTEM_APPS`, and the default application in `AM_APPLICATION`. You can also load `h2-sample-data.sql` into a **scratch copy** for richer examples.

## 5. Trace the core user flows

For each flow, give:
- **who** triggers it (Publisher, Dev Portal, Admin portal, Gateway, Key Manager, or a REST/CLI call),
- the **ordered list of tables written or read**, with the key columns that link each step to the next,
- a Mermaid `sequenceDiagram` or `flowchart`,
- what changes between 3.x and 4.x.

Cover **at least** the flows below. Adjust for the version you're looking at. For example, skip the revision flow on 3.x and explain what replaces it.

1. **Tenant / user bootstrap.** UM_TENANT and UM_USER/roles, then AM_SUBSCRIBER, created lazily on the user's first Dev Portal action. Also AM_SYSTEM_APPS and the seeded default policies and key manager.
2. **API design (Publisher).** The AM_API row, then the registry artifact in REG_*. Then AM_API_URL_MAPPING (one row per verb + path). Then scopes: AM_SCOPE / IDN_OAUTH2_SCOPE → AM_API_RESOURCE_SCOPE_MAPPING, with shared scopes via AM_SHARED_SCOPE. Also categories, labels, GraphQL complexity, client certificates, endpoints (4.x), operation policies (4.x), service catalog link (4.x) and AI/LLM config (4.x).
3. **Versioning & default version.** A new AM_API row with the same name and provider, plus AM_API_DEFAULT_VERSION.
4. **Revision & gateway deployment.**
   - **4.x:** creating a revision writes AM_REVISION, which copies the URL mappings, scope mappings, endpoints and policies tagged with REVISION_UUID, plus AM_API_REVISION_METADATA. It **also** writes AM_GW_PUBLISHED_API_DETAILS and AM_GW_API_ARTIFACTS right away. Deploying then writes AM_DEPLOYMENT_REVISION_MAPPING (the request), AM_GW_API_DEPLOYMENTS, and AM_GW_REVISION_DEPLOYMENT (the gateway's SUCCESS acknowledgement). This was verified on a running 4.7.0 server, where AM_DEPLOYED_REVISION was never written and the `deployment.toml` Default environment isn't in AM_GATEWAY_ENVIRONMENT or AM_GW_VHOST. Also cover the APK / federated gateway tables.
   - **3.x:** publishing writes AM_GW_PUBLISHED_API_DETAILS and AM_GW_API_ARTIFACTS, keyed by GATEWAY_LABEL, with GATEWAY_INSTRUCTION set to PUBLISH or REMOVE. This DB-backed artifact sync is **opt-in** (`[apim.sync_runtime_artifacts.*]`). By default the Publisher pushes straight to the gateway environments defined in `deployment.toml`, so these tables are often empty. 3.x has no environment table, and an API's gateway labels live only in its registry artifact.
5. **Lifecycle change / publish.** AM_API_LC_EVENT. The state lives in the registry lifecycle, and in 4.x also in `AM_API.STATUS`. Optionally a workflow via AM_WORKFLOWS (WF_TYPE = API state change).
6. **API products.** An AM_API row with API_TYPE `'APIProduct'`, plus AM_API_PRODUCT_MAPPING pointing at the URL mappings of the underlying APIs.
7. **Application creation (Dev Portal).** AM_SUBSCRIBER, then AM_APPLICATION (APPLICATION_TIER → AM_POLICY_APPLICATION), plus attributes and group sharing. Optional approval workflow.
8. **Subscription.** AM_SUBSCRIPTION (APPLICATION_ID × API_ID, TIER_ID → AM_POLICY_SUBSCRIPTION, SUB_STATUS, SUBS_CREATE_STATE). Also workflow status and tier-change requests (TIER_ID_PENDING).
9. **Key generation / OAuth app.** AM_APPLICATION_REGISTRATION (always written, with or without a workflow; verified on 3.2.0 and 4.7.0), then the key manager creates the OAuth client. With the Resident KM this is IDN_OAUTH_CONSUMER_APPS, plus SP_APP and SP_INBOUND_AUTH, plus IDN_OAUTH_CONSUMER_SECRETS (4.x). Then AM_APPLICATION_KEY_MAPPING (PRODUCTION/SANDBOX × KEY_MANAGER). With a third-party KM, only the mapping row is stored locally.
10. **Token issue & API invocation.**
    - IDN_OAUTH2_ACCESS_TOKEN and _SCOPE. Verified on running servers: 3.2.0 persists every token (and generating keys issues a first token), and revoked tokens move to IDN_OAUTH2_ACCESS_TOKEN_AUDIT. 4.7.0 does **not** persist application JWTs, and revocation writes AM_REVOKED_JWT + IDN_INVALID_TOKENS. Calling an API writes nothing in either version.
    - At the gateway: validation of subscription, scopes and throttling. The gateway reads these through the internal data APIs, not direct DB access, but the data behind them is AM_SUBSCRIPTION, AM_APPLICATION_KEY_MAPPING, AM_API_URL_MAPPING, the scope mappings and the policies.
    - API keys (4.x AM_API_KEY*), and 3.x AM_SUBSCRIPTION_KEY_MAPPING.
11. **Throttling policy administration (Admin portal).** Each policy type and its condition-group tree (AM_API_THROTTLE_POLICY → AM_CONDITION_GROUP → header / query / JWT-claim / IP conditions), plus global (custom) policies, block conditions and tier permissions.
12. **Revocation & cleanup.** AM_REVOKED_JWT, the app / subject revoked-event tables, IDN_INVALID_TOKENS, and token state changes. Also what cascades when an API, application or subscription is deleted, based on the ON DELETE rules.
13. **Workflows / approvals.** AM_WORKFLOWS (WF_TYPE, WF_REFERENCE, WF_STATUS, WF_EXTERNAL_REFERENCE) and the WF_* BPS tables.
14. **Version-specific flows.** Governance compliance runs (GOV_*, 4.x), AI/LLM APIs (4.x), service catalog → API (4.x), Dev Portal content and webhooks (4.x), monetization, comments and ratings, alerts.

Use the domain knowledge above as a guide. Before you describe a column, check that it actually exists in this version's map.

## 6. Write the report

Unless the user asks for something else, write one Markdown file per version:
`APIM-DB-<version>.md`, e.g. `APIM-DB-4.7.0.md`, in the working directory. Offer to publish it as an Artifact page as well.

Structure:

1. **The big picture.** Five to ten sentences in plain language covering:
   - the two logical DBs and what each holds,
   - the registry vs. RDBMS split,
   - the Identity-Server-inherited tables,
   - the headline numbers (tables per family, declared FKs, logical joins).
2. **A one-screen "hub" diagram.** A Mermaid `flowchart LR` showing only the core entities: Tenant/Org → Subscriber → Application → Subscription ← API → URL Mapping/Scopes/Policies → Revision → Gateway Env. Add Application → Key Mapping → OAuth Consumer App → Access Token, and Throttle policies attached to Subscription, Application and URL mapping.
3. **Per-domain sections.** For each domain:
   - a short intro ("what problem this domain solves"),
   - a Mermaid `erDiagram` containing *every* core table in that domain. Show PK/FK/key columns only; use a dotted relation (`..`) with the label `"logical"` for non-FK joins,
   - a **table catalog** with columns `Table | What it represents (plain English) | Key columns | Relates to (how, cardinality, FK or logical, ON DELETE)`. Every core table appears exactly once across all catalogs.
4. **Core flows.** One subsection per flow from step 5.
5. **Gotchas.** Things that trip people up:
   - string vs. integer API ids,
   - `'Current API'` revision sentinel,
   - name-based policy joins,
   - KM name vs. UUID,
   - registry-held metadata,
   - `ORGANIZATION` vs `TENANT_ID` scoping,
   - where cascading deletes happen and where they're blocked.
6. **Appendix A: peripheral tables.** Grouped by family, one line each, so the inventory is complete.
7. **Appendix B: inventory check.** Total tables parsed = core count + peripheral count, and a statement that nothing was left out.

Style: explain the *why* in plain language before listing columns. Don't paste raw DDL. Keep the Mermaid diagrams readable, and split any domain with more than about 15 tables into sub-diagrams.

## 7. Cross-version comparison (when two versions are present)

Diff the two maps and add `APIM-DB-comparison.md` (or a section in the report) covering:
- tables added, removed or renamed. Known examples: `AM_LABELS` → `AM_LABEL`, and `AM_SUBSCRIPTION_KEY_MAPPING` removed.
- column changes on the core tables: AM_API, AM_APPLICATION, AM_SUBSCRIPTION, AM_API_URL_MAPPING, AM_APPLICATION_KEY_MAPPING, AM_KEY_MANAGER, and the AM_POLICY_* tables. Look especially at the `ORGANIZATION`, `*_UUID` and `REVISION_UUID` columns.
- new FKs, and FKs that were removed.
- how each core flow changed. The big ones:
  - gateway labels → revisions + environments,
  - registry-only API UUID → `AM_API.API_UUID`,
  - tenant → organization scoping,
  - API-level operation policies,
  - service catalog, governance and AI APIs.

```bash
diff <(grep '^## ' map-3.2.0.txt) <(grep '^## ' map-4.7.0.txt)
```

## 8. Finish

Tell the user:
- where the report(s) are,
- the headline counts,
- the three to five most surprising or important relationships,
- anything you couldn't verify, such as logical joins that only the code can confirm.

If they want to go deeper on a flow, offer to trace it in the APIM source, the `org.wso2.carbon.apimgt.impl.dao.*` DAOs and SQL constants, or to confirm it with live-data queries.
