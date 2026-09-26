# Create an API product

!!! abstract "What happens"
    An API product bundles resources picked from one or more APIs into a single thing developers can subscribe to. For example, "Food Delivery" might combine `GET /menu` from PizzaShack with `POST /deliveries` from a Delivery API. APIM stores the product as an `AM_API` row of type `APIProduct`, and stores the chosen resources in `AM_API_PRODUCT_MAPPING`.

**Who:** Publisher · **Tables written:** `AM_API`, `AM_API_PRODUCT_MAPPING`, registry `REG_*`, `UM_PERMISSION`, `UM_ROLE_PERMISSION` · **Tables read:** `AM_API_URL_MAPPING` of the underlying APIs

!!! success "Verified on a running server"
    Checked on WSO2 APIM 3.2.0 (H2, default config) by creating a FoodDelivery product from PizzaShack's `GET /menu`, and diffing the database.

    - Written: one `AM_API` row (`API_TYPE = 'APIProduct'`), **one** `AM_API_PRODUCT_MAPPING` row that points straight at PizzaShack's existing `URL_MAPPING_ID`, and the registry artifact.
    - **Not written:** no copied `AM_API_URL_MAPPING` row, no `AM_API_LC_EVENT` row and no `AM_API_DEFAULT_VERSION` row.
    - **Surprise:** when the underlying API was later updated, its URL mappings were recreated with new IDs, and APIM re-pointed the product mapping (`URL_MAPPING_ID` 1 → 6). The mapping row itself was replaced too (ID 1 → 2).

## The flow at a glance

This diagram shows how a product is built from existing resources rather than new ones.

```mermaid
sequenceDiagram
    actor Creator as API creator
    participant Pub as Publisher
    participant DB as Database
    Creator->>Pub: New product "FoodDelivery"
    Pub->>DB: read AM_API_URL_MAPPING of chosen APIs
    Pub->>DB: insert AM_API (API_TYPE = APIProduct)
    Pub->>DB: insert AM_API_PRODUCT_MAPPING (one per resource)
    Pub->>DB: save registry artifact
```

## Step by step

1. **Product row** → [`AM_API`](../reference/am.md#am_api), the same table as normal APIs.

    | `API_ID` | `API_PROVIDER` | `API_NAME` | `API_VERSION` | `CONTEXT` | `API_TYPE` |
    |---|---|---|---|---|---|
    | 3 | `admin` | `FoodDelivery` | `1.0.0` | `/food` | `APIProduct` |

    - Products have a single version (`1.0.0`) in 3.x.
    - Unlike an API, the `CONTEXT` has **no version** (`/food`, not `/food/1.0.0`), and `CONTEXT_TEMPLATE` and `API_TIER` are `NULL`.
    - Because a product is an `AM_API` row, subscriptions, lifecycle events, comments and ratings work for products exactly as they do for APIs.

2. **Picked resources** → [`AM_API_PRODUCT_MAPPING`](../reference/am.md#am_api_product_mapping).

    | `API_PRODUCT_MAPPING_ID` | `API_ID` (the product) | `URL_MAPPING_ID` (a resource of another API) |
    |---|---|---|
    | 1 | 3 | 1 *(PizzaShack GET /menu)* |

    That's the real row from the test run, a product with one resource. A product that combines resources from several APIs has one row per resource.

    - `API_ID` is a real FK to `AM_API` (the product), with `ON DELETE CASCADE`.
    - `URL_MAPPING_ID` is a real FK to `AM_API_URL_MAPPING` (the original resource), with `ON DELETE CASCADE`.
    - The product **reuses** the original `AM_API_URL_MAPPING` rows. It doesn't copy them, so the scopes and resource throttling of those resources apply to the product too.
    - Because updating the underlying API recreates its URL mapping rows, APIM rewrites these mapping rows on every such update. Their IDs are not stable.

3. **Registry artifact & lifecycle.** As for APIs, a registry artifact holds the description and visibility. Creating the product wrote **no** `AM_API_LC_EVENT` row, unlike creating an API. Later state changes (such as publishing the product) do log events. Publishing a product sends its own artifact to the gateways. See [Publish to the gateway](04-publish-to-gateway.md).

## What gets cleaned up

- Deleting the **product** cascades to its `AM_API_PRODUCT_MAPPING` rows. Its subscriptions and lifecycle events must be removed first (`RESTRICT`). In the test run, deleting an unpublished product removed just the `AM_API` row, the mapping row and its registry data.
- Deleting a **resource** from an underlying API (its `AM_API_URL_MAPPING` row) silently cascades and removes it from every product that used it. APIM normally stops you removing a resource that a product uses.

## Try it

This query lists which API resources make up each product.

```sql
SELECT p.API_NAME AS product, src.API_NAME AS from_api, src.API_VERSION,
       u.HTTP_METHOD, u.URL_PATTERN
FROM   AM_API p
JOIN   AM_API_PRODUCT_MAPPING m ON m.API_ID = p.API_ID
JOIN   AM_API_URL_MAPPING u     ON u.URL_MAPPING_ID = m.URL_MAPPING_ID
JOIN   AM_API src               ON src.API_ID = u.API_ID
WHERE  p.API_TYPE = 'APIProduct';
```

Related domains: [API products](../domains/api-products.md) · [API definition](../domains/api-definition.md)

!!! note "Different in 4.x"
    In 4.x, `AM_API_PRODUCT_MAPPING` has a `REVISION_UUID` column, so products can be revisioned and deployed like APIs. 4.x also **copies** the picked resource into a new `AM_API_URL_MAPPING` row instead of pointing at the original, and creates a lifecycle event and a default-version row for the product. See [Create an API product (4.x)](../../apim-4/flows/06-api-product.md).
