# Gotchas

These are the things that most often lead to wrong queries or wrong conclusions about the APIM 4.x database. Read them before you write any SQL.

## 1. There are two kinds of "API ID"

| Column | Holds |
|---|---|
| `AM_API.API_ID` | An **integer** (auto-increment). |
| `AM_API.API_UUID` | A **UUID string**. It's the same value as the registry's `REG_UUID`. |

- Older tables point to the **integer**: `AM_SUBSCRIPTION`, `AM_API_URL_MAPPING`, `AM_API_LC_EVENT`, `AM_API_COMMENTS`, `AM_API_PRODUCT_MAPPING`, `AM_GRAPHQL_COMPLEXITY`.
- Newer tables point to the **UUID**: `AM_REVISION`, `AM_API_ENDPOINTS`, `AM_API_POLICY_MAPPING`, `AM_API_LABEL_MAPPING`, `AM_API_AI_CONFIGURATION`.
- Some columns are **named `API_ID` but hold the UUID**: every `AM_GW_*` table, `AM_API_EXTERNAL_API_MAPPING.API_ID` and `AM_GW_REVISION_DEPLOYMENT.API_ID`.

Always check which one a column holds before you join.

## 2. "Current API" has three different markers

Rows that belong to the editable API (not a revision) are marked in different ways, depending on the table:

| Table | Marker for the current API |
|---|---|
| `AM_API_URL_MAPPING` | `REVISION_UUID IS NULL` |
| `AM_API_AI_CONFIGURATION` | `API_REVISION_UUID IS NULL` |
| `AM_API_PRODUCT_MAPPING`, `AM_API_PRIMARY_EP_MAPPING` | `REVISION_UUID = 'Current API'` |
| `AM_API_ENDPOINTS`, `AM_API_METADATA`, `AM_API_CLIENT_CERTIFICATE`, `AM_BACKEND` | `REVISION_UUID = 'Current API'` |
| `AM_API_SEQUENCE_BACKEND` | `REVISION_UUID = '0'` |

!!! warning "API products overload `REVISION_UUID`"
    When you add a resource to an API product, APIM **copies** the resource's `AM_API_URL_MAPPING` row. The copy keeps the *source API's* `API_ID`, and puts the **product's `API_ID`** (e.g. `'3'`) in `REVISION_UUID`. A query like "all resources of API 1" that ignores `REVISION_UUID` will also count the product copies.

If you forget the filter, you'll see each resource once for the current API **plus once per revision**.

## 3. Policies are joined by name, not by ID

Subscriptions, applications and resources store the policy **name**:

- `AM_SUBSCRIPTION.TIER_ID = 'Gold'` → `AM_POLICY_SUBSCRIPTION.NAME`
- `AM_APPLICATION.APPLICATION_TIER` → `AM_POLICY_APPLICATION.NAME`
- `AM_API_URL_MAPPING.THROTTLING_TIER` and `AM_API.API_TIER` → `AM_API_THROTTLE_POLICY.NAME`

Policy names are unique only **per tenant**, so in a multi-tenant deployment you also have to match the tenant.

## 4. The key manager column may hold a UUID or a name

`AM_APPLICATION_KEY_MAPPING.KEY_MANAGER` and `AM_APPLICATION_REGISTRATION.KEY_MANAGER` normally hold `AM_KEY_MANAGER.UUID` in 4.x. Data migrated from 3.x may still hold the key manager's **name** (e.g. `Resident Key Manager`). A defensive join is:

```sql
LEFT JOIN AM_KEY_MANAGER km
  ON km.UUID = akm.KEY_MANAGER OR km.NAME = akm.KEY_MANAGER
```

## 5. The APIM-to-OAuth bridge isn't a foreign key

`AM_APPLICATION_KEY_MAPPING.CONSUMER_KEY` = `IDN_OAUTH_CONSUMER_APPS.CONSUMER_KEY` is only a logical link. With an **external** key manager, the `IDN_*` row doesn't exist at all. Tokens point to the client by `IDN_OAUTH2_ACCESS_TOKEN.CONSUMER_KEY_ID` = `IDN_OAUTH_CONSUMER_APPS.ID`, which is the *number*, not the key.

## 6. Much of the API lives in the registry

The description, tags, visibility, business owner, API definition (OpenAPI and so on), documents and thumbnail are **not** in `AM_*` tables. They're in the shared database's `REG_*` tables, found through `REG_RESOURCE.REG_UUID = AM_API.API_UUID`. Because the two tables live in different databases, you usually can't join them in one query.

## 7. `ORGANIZATION` and `TENANT_ID` are two ways of scoping

- Newer 4.x tables scope rows by `ORGANIZATION`, usually a tenant domain such as `carbon.super`.
- Older tables still use the numeric `TENANT_ID` (e.g. `-1234`).
- A few tables use `TENANT_DOMAIN`.

When you join across them, convert between the two. `UM_TENANT` maps `UM_ID` ↔ `UM_DOMAIN_NAME`, but the super tenant has **no row** there.

## 8. Users are text, not foreign keys

`AM_SUBSCRIBER.USER_ID`, `AM_API.API_PROVIDER`, `AM_API_LC_EVENT.USER_ID`, `IDN_OAUTH2_ACCESS_TOKEN.AUTHZ_USER` and many more store a **user name**. If the user store is LDAP or AD, the user isn't in `UM_USER` at all.

## 9. What gets deleted automatically, and what blocks deletion

| Delete this… | …and the database automatically deletes | …but it's **blocked** if |
|---|---|---|
| `AM_API` row | subscriptions, product mappings, lifecycle events, comments, ratings, revisions (→ deployment rows), endpoints, labels, API-level policy mappings. Not its URL mappings (see below). | it's listed in `AM_EXTERNAL_STORES` (RESTRICT), or has rows in `AM_API_METADATA`, `AM_API_AI_CONFIGURATION`, `AM_API_KEY_API_MAPPING` or `AM_BACKEND` (no ON DELETE rule). **APIM's code also refuses** while the API has subscriptions (HTTP 409) |
| `AM_APPLICATION` row | subscriptions, key mappings, registrations, attributes, group mappings | — |
| `AM_SUBSCRIBER` row | — | the subscriber still owns applications, registrations or ratings (RESTRICT) |
| `IDN_OAUTH_CONSUMER_APPS` row | access tokens, authorization codes, consumer secrets | — |
| `AM_OPERATION_POLICY` row | definitions and API/resource attachments | a global gateway policy set uses it (RESTRICT) |

!!! warning "URL mappings aren't cascaded from the API"
    `AM_API_URL_MAPPING.API_ID` has **no FK**, so deleting an `AM_API` row does *not* delete its URL mappings at database level. APIM's code deletes them explicitly. If you delete rows by hand, delete the URL mappings too. Their own children (scope, policy and product mappings) then cascade.

## 10. Not everything is in the database

- Gateway environments defined in `deployment.toml` have **no** `AM_GATEWAY_ENVIRONMENT` row.
- **JWT access tokens aren't stored by default.** A JWT issued to a JWT-type application (for example with `client_credentials`) has no `IDN_OAUTH2_ACCESS_TOKEN` row. The gateway validates it by its signature. Only opaque tokens are stored. Revoking a JWT writes `AM_REVOKED_JWT` + `IDN_INVALID_TOKENS`.
- **Calling an API writes nothing.** `AM_SUBSCRIPTION.LAST_ACCESSED` stays `NULL`.
- **API keys are stored only as a hash.** `AM_API_KEY.API_KEY_HASH` looks like `$sha256$…`.
- **`AM_SYSTEM_APPS` is empty** until a user first signs in to the Publisher, Developer Portal or Admin Portal web UI. Using only the REST APIs doesn't create these rows.
- **The super tenant has no `UM_TENANT` row.**
- **Workflow configuration lives in the registry** (`/_system/governance/apimgt/applicationdata/workflow-extensions.xml`), not in `AM_SYSTEM_CONFIGS` or tenant config.
- Analytics and usage data goes to the analytics platform, not to these tables.

## 11. Deployment state isn't where the table names suggest

- `AM_GW_API_ARTIFACTS` and `AM_GW_PUBLISHED_API_DETAILS` are written when a **revision is created**, before anything is deployed. An artifact row doesn't mean the API is live.
- `AM_DEPLOYED_REVISION` stays **empty** after a successful deployment to the built-in gateway. The gateway's confirmation is in `AM_GW_REVISION_DEPLOYMENT` (`STATUS = 'SUCCESS'`, `ACTION = 'DEPLOY'`).
- For the built-in `Default` environment, `AM_DEPLOYMENT_REVISION_MAPPING.VHOST` is stored as `NULL`.

## 12. Status flags that don't change

- `IS_DEPLOYED` stays `0` on throttling policies created through the Admin API, even while the policies are in use.
- `AM_APPLICATION_REGISTRATION` gets a row on every key generation, even with no approval workflow. Don't read its rows as "pending".

## 13. Some "unique" rules are enforced only in code

For example, `AM_SUBSCRIPTION` has no UNIQUE constraint on (`APPLICATION_ID`, `API_ID`), and `AM_SCOPE` has none on (`NAME`, `TENANT_ID`). The application prevents duplicates. Hand-written inserts won't.

!!! note "Different in 3.x"
    Most of these apply to 3.x as well, but there are fewer ID styles (no `API_UUID` at all) and there are no revision markers. See the [3.x Gotchas](../apim-3/gotchas.md).
