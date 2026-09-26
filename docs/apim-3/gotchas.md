# Gotchas (3.x)

These are the things that most often trip people up when they read or query the APIM 3.x database.

## 1. The API UUID isn't in `AM_API`

`AM_API` only has an integer `API_ID`. The UUID used in REST APIs is the registry artifact id (`REG_RESOURCE.REG_UUID`). To go from a UUID to an `AM_API` row, look up the artifact's provider, name and version in the registry, then match on `AM_API (API_PROVIDER, API_NAME, API_VERSION)`. See [Registry](domains/registry.md).

## 2. Two kinds of "API ID"

| Table | `API_ID` holds |
|---|---|
| `AM_API`, `AM_SUBSCRIPTION`, `AM_API_URL_MAPPING`, `AM_API_LC_EVENT`, … | the **integer** `AM_API.API_ID` |
| `AM_GW_PUBLISHED_API_DETAILS`, `AM_GW_API_ARTIFACTS` | the API's **UUID string** |
| `AM_API_LC_PUBLISH_EVENTS` | a **string** identifier (`VARCHAR`) |

Never join these columns to each other directly.

## 3. Policies are joined by *name*, not by ID

`AM_SUBSCRIPTION.TIER_ID`, `AM_APPLICATION.APPLICATION_TIER`, `AM_API.API_TIER` and `AM_API_URL_MAPPING.THROTTLING_TIER` all hold a **policy name** such as `Gold` or `Unlimited`. They match `NAME` in `AM_POLICY_SUBSCRIPTION`, `AM_POLICY_APPLICATION` and `AM_API_THROTTLE_POLICY` respectively. Names are unique **per tenant** (`UNIQUE (NAME, TENANT_ID)`), so always add the tenant to the join. There are no foreign keys, so renaming or deleting a policy doesn't update these columns. See [Throttling policies](domains/throttling.md).

## 4. The app → OAuth client link is logical

`AM_APPLICATION_KEY_MAPPING.CONSUMER_KEY` matches `IDN_OAUTH_CONSUMER_APPS.CONSUMER_KEY`, but there's no FK. If keys come from a third-party key manager, there's **no** `IDN_OAUTH_CONSUMER_APPS` row at all. See [Keys & tokens](domains/keys-tokens.md).

## 5. `KEY_MANAGER` holds a name

In 3.2, `AM_APPLICATION_KEY_MAPPING.KEY_MANAGER` and `AM_APPLICATION_REGISTRATION.KEY_MANAGER` hold the key manager's **name** (the built-in one is `Resident Key Manager`). They don't hold `AM_KEY_MANAGER.UUID`. Join on `AM_KEY_MANAGER.NAME` + `TENANT_DOMAIN`.

## 6. Deletes are mostly *blocked*, not cascaded

In 3.2, the key consumer foreign keys use `ON DELETE RESTRICT`:

- `AM_SUBSCRIPTION` → `AM_APPLICATION` and → `AM_API`
- `AM_APPLICATION_KEY_MAPPING` → `AM_APPLICATION`
- `AM_APPLICATION_REGISTRATION` → `AM_APPLICATION`, `AM_SUBSCRIBER`
- `AM_API_LC_EVENT`, `AM_API_COMMENTS`, `AM_API_RATINGS`, `AM_EXTERNAL_STORES`, `AM_SECURITY_AUDIT_UUID_MAPPING` → `AM_API`

So a plain `DELETE FROM AM_APPLICATION` fails while subscriptions or keys exist. APIM's code deletes the child rows first. Only a few children cascade: `AM_APPLICATION_ATTRIBUTES`, `AM_APPLICATION_GROUP_MAPPING`, `AM_API_PRODUCT_MAPPING`, `AM_GRAPHQL_COMPLEXITY`, `AM_API_CLIENT_CERTIFICATE`, and the scope mappings through `AM_API_URL_MAPPING`.

!!! note "Different in 4.x"
    4.x changes several of these to `ON DELETE CASCADE`. See [4.x gotchas](../apim-4/gotchas.md).

## 7. `AM_API_URL_MAPPING.API_ID` has no foreign key

Resources point at their API by integer `API_ID`, but the database doesn't enforce it. Orphaned resource rows are possible if something deletes an API outside APIM.

## 8. API products are `AM_API` rows too

An API product is a row in `AM_API` with `API_TYPE = 'APIProduct'` (that exact casing in 3.2). Filter on `API_TYPE` when you only want APIs. Its `AM_API_PRODUCT_MAPPING` rows point **directly** at the underlying API's own `AM_API_URL_MAPPING` rows; nothing is copied. See [API products](domains/api-products.md).

## 9. Gateway labels ≠ API labels

`AM_LABELS` in 3.x are **microgateway labels**: they say *which gateways* get an API. They aren't tags. Tags live in the registry (`REG_TAG`). See [Lifecycle & labels](domains/lifecycle-labels.md).

## 10. Some tables exist but no bundled component writes them

`AM_SCOPE`, `AM_SCOPE_BINDING`, `AM_POLICY_HARD_THROTTLING`, `AM_API_LC_PUBLISH_EVENTS` and `AM_USAGE_UPLOADED_FILES` are part of the 3.2.0 schema, but APIM 3.2.0 doesn't use them. API scopes actually live in `IDN_OAUTH2_SCOPE`. Expect these tables to be empty.

## 11. Subscribers are created lazily

A user can exist in `UM_USER` without an `AM_SUBSCRIBER` row. The subscriber row is created the first time they act in the Dev Portal, together with their `DefaultApplication`. Similarly, `AM_SYSTEM_APPS` stays empty until someone signs in to the web portals. See [Setup & first user](flows/01-bootstrap.md).

## 12. Tokens are stored, but not quite as you'd expect

With JWT access tokens (the 3.x default for new applications, `AM_APPLICATION.TOKEN_TYPE = 'JWT'`), every issued token still gets an `IDN_OAUTH2_ACCESS_TOKEN` row, but the gateway validates the JWT signature **without** a database lookup. In 3.2.0:

- `ACCESS_TOKEN` holds the JWT's ID (a UUID), not the full JWT.
- Getting a new token for the same app marks the previous one `TOKEN_STATE = 'REVOKED'` in place.
- Explicitly revoking a token **moves** its row to `IDN_OAUTH2_ACCESS_TOKEN_AUDIT` and adds an `AM_REVOKED_JWT` row.
- API keys (self-contained JWTs) and API calls write nothing to the database.

See [Revocation](domains/revocation.md) and [Get a token & call the API](flows/10-token-and-invoke.md).

## 13. URL mapping IDs change every time an API is updated

Saving changes to an API **deletes all its `AM_API_URL_MAPPING` rows and inserts new ones with new IDs**, then re-points `AM_API_RESOURCE_SCOPE_MAPPING` and `AM_API_PRODUCT_MAPPING`. The API's local `IDN_OAUTH2_SCOPE` row is recreated with a new `SCOPE_ID` too. Never cache or store these IDs outside APIM. See [Create an API](flows/02-create-api.md).

## 14. The gateway tables are usually empty

`AM_GW_PUBLISHED_API_DETAILS` and `AM_GW_API_ARTIFACTS` are only written when the gateway artifact synchronizer is turned on. In the default configuration, publishing an API writes just an `AM_API_LC_EVENT` row. Also, an API with no gateway environment selected is published but **not deployed**, and the gateway returns 404. See [Publish to the gateway](flows/04-publish-to-gateway.md).

## 15. Generating keys writes more than you'd think

Clicking *Generate Keys* writes an `AM_APPLICATION_REGISTRATION` row **even without an approval workflow**, and that row stays until the app is deleted. It also creates a service provider (`SP_APP` …), an `Application/<owner>_<app>_<keytype>` role in `UM_HYBRID_ROLE`, and an **initial access token**. With the default config, the consumer secret was stored in plain text in `IDN_OAUTH_CONSUMER_APPS.CONSUMER_SECRET`. See [Generate keys](flows/09-generate-keys.md).

## 16. APIM refuses to delete an API that has subscriptions

The Publisher returns **HTTP 409** ("active subscriptions exist") instead of deleting the subscriptions for you. Remove or move the subscriptions first. See [Revoke & delete](flows/12-revocation-and-delete.md).
