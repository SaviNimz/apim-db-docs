# Create an API

!!! abstract "What happens"
    An API creator designs an API in the Publisher: its name, version, context, resources (verb + path), scopes, endpoints and policies. APIM stores the searchable core in `AM_API` and one row per resource in `AM_API_URL_MAPPING`, and keeps the full API description (including the endpoint URLs) in the registry.

**Who:** API creator (Publisher portal or REST API) · **Tables written:** [`AM_API`](../reference/am.md#am_api), [`AM_API_LC_EVENT`](../reference/am.md#am_api_lc_event), [`AM_API_URL_MAPPING`](../reference/am.md#am_api_url_mapping), [`AM_SCOPE`](../reference/am.md#am_scope), [`AM_SCOPE_BINDING`](../reference/am.md#am_scope_binding), [`IDN_OAUTH2_SCOPE`](../reference/idn.md#idn_oauth2_scope), [`IDN_OAUTH2_SCOPE_BINDING`](../reference/idn.md#idn_oauth2_scope_binding), [`AM_API_RESOURCE_SCOPE_MAPPING`](../reference/am.md#am_api_resource_scope_mapping), `GOV_ARTIFACT` / `GOV_REQUEST*`, `REG_*`, `UM_PERMISSION` · **Tables read:** [`AM_API_THROTTLE_POLICY`](../reference/am.md#am_api_throttle_policy), [`AM_SHARED_SCOPE`](../reference/am.md#am_shared_scope), [`AM_OPERATION_POLICY`](../reference/am.md#am_operation_policy)

## The flow at a glance

This diagram shows what gets saved when a creator clicks **Create**.

```mermaid
sequenceDiagram
    actor Creator as API creator
    participant Pub as Publisher
    participant DB as APIM DB
    participant Reg as Registry (shared DB)
    Creator->>Pub: Create PizzaShack 1.0.0
    Pub->>DB: insert AM_API + AM_API_LC_EVENT
    Pub->>Reg: store API artifact incl. endpoints (REG_*)
    Pub->>DB: insert AM_API_URL_MAPPING (one per resource)
    Pub->>DB: insert AM_SCOPE, IDN_OAUTH2_SCOPE, scope mapping
    Pub->>DB: queue governance check (GOV_REQUEST)
    Pub-->>Creator: API created (status CREATED)
```

- The API isn't live yet. Nothing reaches a gateway until you [deploy a revision](04-deploy-revision.md).
- All these rows describe the **working copy** of the API (the "current API"), not a revision.

## Step by step

1. **The API row.** One row goes into [`AM_API`](../reference/am.md#am_api).
    - The API gets a numeric `API_ID` (used by older tables) and a string `API_UUID` (used by newer ones).
    - `API_PROVIDER`, `API_NAME`, `API_VERSION` and `ORGANIZATION` together must be unique.
    - `CONTEXT` holds the full context including the version (`/pizzashack/1.0.0`), and `CONTEXT_TEMPLATE` holds the context as entered, without the version (`/pizzashack`).
    - `API_TYPE` is `HTTP`, `WS`, `GRAPHQL`, `SOAP`, `WEBSUB`, `SSE`, `ASYNC` … or `APIProduct`. `API_SUBTYPE` is `DEFAULT` for a normal API (`AIAPI` for an [AI API](15-ai-api.md)). `STATUS` starts as `CREATED`.

    | API_ID | API_UUID | API_NAME | API_VERSION | CONTEXT | API_TYPE | API_SUBTYPE | STATUS | ORGANIZATION |
    |---|---|---|---|---|---|---|---|---|
    | 1 | `b41b…` | PizzaShackAPI | 1.0.0 | /pizzashack/1.0.0 | HTTP | DEFAULT | CREATED | carbon.super |

    A first lifecycle event is logged in [`AM_API_LC_EVENT`](../reference/am.md#am_api_lc_event): `PREVIOUS_STATE = NULL`, `NEW_STATE = 'CREATED'`.

2. **The registry artifact.** The rest of the API goes to the registry, in the `REG_*` tables of the shared DB: description, tags, visibility, business owner, the endpoint configuration, the OpenAPI definition and so on. APIM also adds `UM_PERMISSION` / `UM_ROLE_PERMISSION` rows so the right roles can read the artifact. See the [Registry](../domains/registry.md) domain.

    !!! warning "Logical link (no foreign key)"
        The registry artifact and the `AM_API` row are tied together by the API UUID. There is no database constraint between the APIM DB and the shared DB.

3. **Resources.** Each verb + path becomes one row in [`AM_API_URL_MAPPING`](../reference/am.md#am_api_url_mapping), linked by `API_ID`. Each row carries:
    - the resource-level rate limit in `THROTTLING_TIER`, e.g. `Unlimited`, which matches [`AM_API_THROTTLE_POLICY`](../reference/am.md#am_api_throttle_policy)`.NAME`,
    - `AUTH_SCHEME`. Resources created with "Application & Application User" security are stored as `Any`,
    - `REVISION_UUID`, which is `NULL` for the working copy.

    | URL_MAPPING_ID | API_ID | HTTP_METHOD | URL_PATTERN | AUTH_SCHEME | THROTTLING_TIER | REVISION_UUID |
    |---|---|---|---|---|---|---|
    | 1 | 1 | GET | /menu | Any | Unlimited | *(null)* |
    | 2 | 1 | POST | /order | Any | Unlimited | *(null)* |

    !!! warning "Logical link (no foreign key)"
        `AM_API_URL_MAPPING.API_ID` → `AM_API.API_ID` has **no FK** in 4.7.0. Deleting an API relies on APIM's code to remove these rows.

4. **Scopes.**
    - A local scope such as `order:write` is saved in [`AM_SCOPE`](../reference/am.md#am_scope) (`SCOPE_ID`, `NAME`, `DISPLAY_NAME`, `DESCRIPTION`, `TENANT_ID`, `SCOPE_TYPE = 'OAUTH2'`). Its role bindings go in [`AM_SCOPE_BINDING`](../reference/am.md#am_scope_binding) (`SCOPE_ID`, `SCOPE_BINDING = 'admin'`, `BINDING_TYPE = 'DEFAULT'`).
    - With the Resident Key Manager, the same scope is also registered in [`IDN_OAUTH2_SCOPE`](../reference/idn.md#idn_oauth2_scope), with its role in [`IDN_OAUTH2_SCOPE_BINDING`](../reference/idn.md#idn_oauth2_scope_binding).
    - Each resource that needs the scope gets a row in [`AM_API_RESOURCE_SCOPE_MAPPING`](../reference/am.md#am_api_resource_scope_mapping), which links `SCOPE_NAME` to `URL_MAPPING_ID`. This FK cascades on delete.
    - Scopes shared between APIs are defined once in [`AM_SHARED_SCOPE`](../reference/am.md#am_shared_scope) and are only *referenced* by name here.

    | SCOPE_NAME | URL_MAPPING_ID | TENANT_ID |
    |---|---|---|
    | order:write | 2 | -1234 |

    !!! warning "Logical link (no foreign key)"
        The mapping points to the scope by **name**. `AM_SCOPE.NAME` ↔ `IDN_OAUTH2_SCOPE.NAME` is also a name match. See [Scopes](../domains/scopes.md).

5. **Governance check queued.** Because the default governance policy applies on `API_CREATE`, APIM registers the API in [`GOV_ARTIFACT`](../reference/gov.md#gov_artifact) (`ARTIFACT_REF_ID` = the API UUID, `ARTIFACT_TYPE = 'API'`) and queues a [`GOV_REQUEST`](../reference/gov.md#gov_request) (`STATUS = 'PENDING'`) with one [`GOV_REQUEST_POLICY`](../reference/gov.md#gov_request_policy) row. A background task processes it later. See [Governance check](14-governance.md).

6. **Endpoints.** For a normal API, the production and sandbox URLs are kept **in the registry artifact**. In the test, no [`AM_API_ENDPOINTS`](../reference/am.md#am_api_endpoints) row was written. That table (`API_UUID`, `ENDPOINT_UUID`, `ENDPOINT_NAME`, `KEY_TYPE`, `ENDPOINT_CONFIG`, with `REVISION_UUID = 'Current API'` for the working copy) holds *named* endpoints, which AI APIs and MCP servers use. [`AM_API_PRIMARY_EP_MAPPING`](../reference/am.md#am_api_primary_ep_mapping) records which endpoint is the primary one (see [Create an AI API](15-ai-api.md)).

7. **Optional extras**, all linked to the API, written only when you use the feature:
    - **Operation policies** (e.g. "add header") attached to a resource go into [`AM_API_OPERATION_POLICY_MAPPING`](../reference/am.md#am_api_operation_policy_mapping) (`URL_MAPPING_ID`, `POLICY_UUID`, `DIRECTION`, `POLICY_ORDER`). API-level policies go into [`AM_API_POLICY_MAPPING`](../reference/am.md#am_api_policy_mapping). See [Operation policies](../domains/operation-policies.md).
    - **Labels:** [`AM_API_LABEL_MAPPING`](../reference/am.md#am_api_label_mapping) (`API_UUID`, `LABEL_UUID`).
    - **GraphQL** query-complexity values: [`AM_GRAPHQL_COMPLEXITY`](../reference/am.md#am_graphql_complexity).
    - **Mutual-TLS client certificates:** [`AM_API_CLIENT_CERTIFICATE`](../reference/am.md#am_api_client_certificate).
    - **Created from the Service Catalog:** [`AM_API_SERVICE_MAPPING`](../reference/am.md#am_api_service_mapping) (`API_ID`, `SERVICE_KEY`).
    - **Extra key/value metadata:** [`AM_API_METADATA`](../reference/am.md#am_api_metadata).

## What gets cleaned up

When an API is deleted, many child tables clean themselves up through `ON DELETE CASCADE`. These include:
- [`AM_REVISION`](../reference/am.md#am_revision)
- [`AM_API_ENDPOINTS`](../reference/am.md#am_api_endpoints)
- [`AM_API_LABEL_MAPPING`](../reference/am.md#am_api_label_mapping)
- [`AM_API_POLICY_MAPPING`](../reference/am.md#am_api_policy_mapping)
- [`AM_GRAPHQL_COMPLEXITY`](../reference/am.md#am_graphql_complexity)
- [`AM_API_CLIENT_CERTIFICATE`](../reference/am.md#am_api_client_certificate)
- [`AM_API_LC_EVENT`](../reference/am.md#am_api_lc_event)
- [`AM_SUBSCRIPTION`](../reference/am.md#am_subscription)

The URL mappings have no FK, so APIM's code deletes them. That delete then cascades on to the scope and operation-policy mappings. APIM's code also deletes the API's `GOV_ARTIFACT` and governance results.

Two tables **block** the delete until their rows are removed first: [`AM_EXTERNAL_STORES`](../reference/am.md#am_external_stores) (`RESTRICT`) and [`AM_API_METADATA`](../reference/am.md#am_api_metadata), which has no ON DELETE rule. And even though `AM_SUBSCRIPTION` would cascade, **APIM's code refuses to delete an API that still has subscriptions** (HTTP 409). For the full picture, see [Revoke & delete](12-revocation-and-delete.md).

## Try it

This query shows an API's resources with the scope each one needs.

```sql
SELECT a.API_NAME, a.API_VERSION, u.HTTP_METHOD, u.URL_PATTERN,
       u.THROTTLING_TIER, s.SCOPE_NAME
FROM AM_API a
JOIN AM_API_URL_MAPPING u ON u.API_ID = a.API_ID AND u.REVISION_UUID IS NULL
LEFT JOIN AM_API_RESOURCE_SCOPE_MAPPING s ON s.URL_MAPPING_ID = u.URL_MAPPING_ID
WHERE a.API_NAME = 'PizzaShackAPI'
ORDER BY u.URL_PATTERN, u.HTTP_METHOD;
```

!!! note "Different in 3.x"
    In 3.x, `AM_API` has **no `API_UUID`** column (the UUID lives only in the registry), no `ORGANIZATION`, `STATUS` or `REVISION_UUID` columns, and no endpoint or operation-policy tables. The scope is written only to `IDN_OAUTH2_SCOPE`, and there's no governance. See [3.x: Create an API](../../apim-3/flows/02-create-api.md).

**Related domains:** [API definition](../domains/api-definition.md) · [Scopes](../domains/scopes.md) · [Operation policies](../domains/operation-policies.md) · [Registry](../domains/registry.md)
