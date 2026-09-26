# Get a token & call the API

!!! abstract "What happens"
    The client app swaps its consumer key and secret for an **access token** from the Key Manager, then calls the API through the **Gateway**. The Gateway checks four things: that the token is valid, that the application is subscribed, that the token has the scopes the resource needs, and that the rate limits aren't exceeded. Then it forwards the request to the backend.

!!! success "Verified on a running server"
    Confirmed on WSO2 APIM 4.7.0 (embedded H2, default config) by getting a `client_credentials` token for `PizzaApp` (a JWT-type application) and calling `GET /pizzashack/1.0.0/menu` three times through the gateway (HTTP 200). Surprises:

    - **The JWT access token was not stored anywhere.** No [`IDN_OAUTH2_ACCESS_TOKEN`](../reference/idn.md#idn_oauth2_access_token) row was written. By contrast, the **opaque** token issued to the test's own REST client (a password grant) *was* stored, with a UUID in `ACCESS_TOKEN`.
    - **Calling the API wrote nothing** to either database.
    - **An API key is stored only as a hash.** Generating one wrote [`AM_API_KEY`](../reference/am.md#am_api_key) (`API_KEY_HASH = '$sha256$…'`) and [`AM_API_KEY_APPLICATION_MAPPING`](../reference/am.md#am_api_key_application_mapping), which is linked by the application's **UUID**.

**Who:** Client app, Key Manager, Gateway · **Tables written:** none for a JWT token or an API call. [`IDN_OAUTH2_ACCESS_TOKEN`](../reference/idn.md#idn_oauth2_access_token) and [`IDN_OAUTH2_ACCESS_TOKEN_SCOPE`](../reference/idn.md#idn_oauth2_access_token_scope) only for opaque (non-JWT) tokens. [`AM_API_KEY`](../reference/am.md#am_api_key) and [`AM_API_KEY_APPLICATION_MAPPING`](../reference/am.md#am_api_key_application_mapping) for API keys · **Tables read (via the control plane):** [`AM_APPLICATION_KEY_MAPPING`](../reference/am.md#am_application_key_mapping), [`AM_SUBSCRIPTION`](../reference/am.md#am_subscription), [`AM_API_URL_MAPPING`](../reference/am.md#am_api_url_mapping), [`AM_API_RESOURCE_SCOPE_MAPPING`](../reference/am.md#am_api_resource_scope_mapping), `AM_POLICY_*`

## The flow at a glance

This diagram shows one token request followed by one API call.

```mermaid
sequenceDiagram
    participant App as Client app
    participant KM as Key Manager
    participant DB as Database
    participant GW as Gateway
    participant BE as Backend
    App->>KM: POST /oauth2/token (key + secret)
    KM->>DB: read IDN_OAUTH_CONSUMER_APPS
    KM-->>App: JWT access token (not stored)
    App->>GW: GET /pizzashack/1.0.0/menu (Bearer JWT)
    GW->>GW: check signature, subscription, scope, limits (in memory)
    GW->>BE: forward request
    BE-->>App: response (via Gateway)
```

- The Gateway **doesn't query the database per request**. At startup it loads subscriptions, applications, key mappings, API resources and policies from the control plane's internal APIs, which read the tables listed above. After that, events keep its in-memory copy up to date.
- Rate limits are counted by the **Traffic Manager** in memory, not in the database.

## Step by step

1. **Token request.** The Key Manager finds the client in [`IDN_OAUTH_CONSUMER_APPS`](../reference/idn.md#idn_oauth_consumer_apps) by `CONSUMER_KEY` and checks the secret and grant type.

2. **Token stored? Only if it's opaque.** In 4.7.0's default setup, **JWT access tokens are not persisted**: the test's client_credentials JWT left no row. Opaque tokens, such as those for applications with token type `DEFAULT` or the REST client used in the test, are recorded in [`IDN_OAUTH2_ACCESS_TOKEN`](../reference/idn.md#idn_oauth2_access_token), with their scopes in [`IDN_OAUTH2_ACCESS_TOKEN_SCOPE`](../reference/idn.md#idn_oauth2_access_token_scope) (`TOKEN_ID`, `TOKEN_SCOPE`, FK with cascade). The important token columns are:
    - `CONSUMER_KEY_ID` → `IDN_OAUTH_CONSUMER_APPS.ID` (a real FK, cascade)
    - `AUTHZ_USER`, `GRANT_TYPE`, `TOKEN_STATE` (`ACTIVE`, `REVOKED`, `EXPIRED` …)
    - `TIME_CREATED`, `VALIDITY_PERIOD`
    - `ACCESS_TOKEN` / `ACCESS_TOKEN_HASH`. For an opaque token, `ACCESS_TOKEN` is the token value itself (a UUID).

    The opaque token issued to the test's REST client looked like this:

    | TOKEN_ID | CONSUMER_KEY_ID | AUTHZ_USER | USER_TYPE | GRANT_TYPE | TOKEN_STATE | VALIDITY_PERIOD |
    |---|---|---|---|---|---|---|
    | `a109…` | 1 *(REST client)* | admin | APPLICATION_USER | password | ACTIVE | 3600000 |

    !!! info "Where do JWTs go, then?"
        - Because JWTs aren't stored, revoking one is tracked through [`AM_REVOKED_JWT`](../reference/am.md#am_revoked_jwt) and [`IDN_INVALID_TOKENS`](../reference/idn.md#idn_invalid_tokens) instead (verified, see [Revoke & delete](12-revocation-and-delete.md)).
        - Third-party Key Managers keep their tokens in their own systems.

3. **Gateway validates the JWT.** It checks the signature and expiry locally, using the Key Manager's certificate/JWKS. It also checks the token isn't in the revoked list, which is loaded from [`AM_REVOKED_JWT`](../reference/am.md#am_revoked_jwt).

4. **Subscription check.** The token's client id, `azp`/consumer key, leads to the application through [`AM_APPLICATION_KEY_MAPPING`](../reference/am.md#am_application_key_mapping) and on to an [`AM_SUBSCRIPTION`](../reference/am.md#am_subscription) for this API.
    - The subscription must exist with `SUB_STATUS = 'UNBLOCKED'`. `PROD_ONLY_BLOCKED` blocks production keys only.
    - An API with `AM_API.SUB_VALIDATION = 'DISABLED'` skips this check.

5. **Resource and scope check.** The request path and verb are matched against the deployed revision's [`AM_API_URL_MAPPING`](../reference/am.md#am_api_url_mapping) rows. The token must contain the scope in [`AM_API_RESOURCE_SCOPE_MAPPING`](../reference/am.md#am_api_resource_scope_mapping) for that resource.

6. **Rate limits.** The Gateway applies each level in turn:

    | Level | Limit comes from |
    |---|---|
    | Subscription | `AM_SUBSCRIPTION.TIER_ID` → [`AM_POLICY_SUBSCRIPTION`](../reference/am.md#am_policy_subscription) |
    | Application | `AM_APPLICATION.APPLICATION_TIER` → [`AM_POLICY_APPLICATION`](../reference/am.md#am_policy_application) |
    | Resource | `AM_API_URL_MAPPING.THROTTLING_TIER` → [`AM_API_THROTTLE_POLICY`](../reference/am.md#am_api_throttle_policy) |
    | Custom / blocking | [`AM_POLICY_GLOBAL`](../reference/am.md#am_policy_global), [`AM_BLOCK_CONDITIONS`](../reference/am.md#am_block_conditions) |

    If any limit is exceeded, the Gateway returns HTTP 429. See [Manage throttling policies](11-throttling-policies.md).

7. **Forward and record.** The request goes to the backend URL from the deployed revision's artifact. Analytics events go to the analytics system, **not** to these tables. In the test, three successful calls changed **no rows at all**. [`AM_SUBSCRIPTION`](../reference/am.md#am_subscription)`.LAST_ACCESSED` exists but stayed `NULL`.

!!! info "API keys: the other way in"
    A developer can also generate an **API key** for an application. In the test (`POST …/applications/{id}/api-keys/PRODUCTION/generate` with a `keyName`):
    - [`AM_API_KEY`](../reference/am.md#am_api_key) got one row: `API_KEY_UUID`, `NAME = 'pizza-key'`, `API_KEY_HASH = '$sha256$a858…'`, `KEY_TYPE = 'PRODUCTION'`, `API_KEY_PROPERTIES` (allowed referrers and IPs), `AUTHZ_USER = 'admin'`. **The key itself is never stored.**
    - [`AM_API_KEY_APPLICATION_MAPPING`](../reference/am.md#am_api_key_application_mapping) linked it to the app by `APPLICATION_UUID` (`4023…`), not by the integer `APPLICATION_ID`.
    - Deleting the application removed the mapping row.

## What gets cleaned up

- Stored (opaque) tokens that expire or are revoked are removed by the Key Manager's token cleanup, which is configurable. The cleanup may copy them to [`IDN_OAUTH2_ACCESS_TOKEN_AUDIT`](../reference/idn.md#idn_oauth2_access_token_audit) first.
- Deleting the OAuth client cascades to its tokens and their scopes.

## Try it

This query lists the stored (opaque) active tokens for an application's production keys. For JWT-type apps in 4.7.0 it returns nothing, because JWTs aren't stored.

```sql
SELECT ap.NAME AS APPLICATION, t.AUTHZ_USER, t.GRANT_TYPE, t.TOKEN_STATE,
       t.TIME_CREATED, t.VALIDITY_PERIOD / 1000 AS VALID_SECONDS
FROM AM_APPLICATION ap
JOIN AM_APPLICATION_KEY_MAPPING km ON km.APPLICATION_ID = ap.APPLICATION_ID
                                  AND km.KEY_TYPE = 'PRODUCTION'
JOIN IDN_OAUTH_CONSUMER_APPS oc ON oc.CONSUMER_KEY = km.CONSUMER_KEY
JOIN IDN_OAUTH2_ACCESS_TOKEN t ON t.CONSUMER_KEY_ID = oc.ID
WHERE ap.NAME = 'PizzaApp' AND t.TOKEN_STATE = 'ACTIVE';
```

!!! note "Different in 3.x"
    3.x validates tokens the same way, but **stores every token it issues**, JWTs included, in `IDN_OAUTH2_ACCESS_TOKEN`. Its API keys are self-contained JWTs with no database row, and its `AM_SUBSCRIPTION_KEY_MAPPING` table has no 4.x equivalent. See [3.x: Get a token & call the API](../../apim-3/flows/10-token-and-invoke.md).

**Related domains:** [Keys & tokens](../domains/keys-tokens.md) · [Scopes](../domains/scopes.md) · [Throttling policies](../domains/throttling.md) · [Revocation](../domains/revocation.md)
