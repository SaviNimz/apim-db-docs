# Glossary

API
:   A set of HTTP resources (for example `GET /menu`) that APIM exposes and protects. Each version of an API is its own row in `AM_API`.

API product
:   A bundle of resources taken from one or more APIs and sold as a single package. It's stored as an `AM_API` row with type `APIProduct`.

Application
:   The identity of a *consumer's* software, such as a mobile app. Developers create applications in the Developer Portal, subscribe them to APIs and generate keys for them. Stored in `AM_APPLICATION`.

Consumer key / consumer secret
:   The OAuth client ID and secret generated for an application. The application uses them to get access tokens.

Developer Portal (Dev Portal)
:   The website where API consumers find APIs, create applications, subscribe and get keys. It was called the *Store* in older versions.

Environment (gateway environment)
:   A named group of gateways, such as *Production and Sandbox*, that an API can be deployed to. From 4.x, environments can be created in the Admin Portal and are stored in `AM_GATEWAY_ENVIRONMENT`.

Gateway
:   The runtime component that receives API calls, checks tokens, applies rate limits and forwards requests to the backend.

Gateway label (3.x)
:   In 3.x, a name used to decide which gateways (including microgateways) receive an API's artifacts.

Governance (4.x)
:   Rules (rulesets and policies) that APIs are checked against, such as "every API must have a description". Stored in the `GOV_*` tables.

JWT
:   JSON Web Token: a self-contained, signed token. Most APIM tokens are JWTs, so the gateway can check them without a database lookup.

Key Manager (KM)
:   The component that issues and validates OAuth tokens. APIM has a built-in *Resident Key Manager*, and you can plug in others such as Keycloak or Okta. Stored in `AM_KEY_MANAGER`.

Key type
:   `PRODUCTION` or `SANDBOX`. An application can have one set of keys for each type (per key manager).

Lifecycle (LC)
:   The states an API moves through: *Created → Published → Deprecated → Retired* (plus *Prototyped* and *Blocked*). Every change is logged in `AM_API_LC_EVENT`.

Operation policy (4.x)
:   A reusable piece of mediation, such as "add header" or "rewrite path", attached to an API resource in the request, response or fault flow.

Organization (4.x)
:   The owning scope of most APIM data in 4.x, stored in `ORGANIZATION` columns. By default it's the tenant domain, e.g. `carbon.super`.

Publisher
:   The website where API creators design, version, deploy and publish APIs.

Registry
:   A generic resource store in the shared database (`REG_*` tables). APIM keeps each API's full metadata (description, tags, lifecycle and so on) there as an "artifact".

Revision (4.x)
:   A read-only snapshot of an API. Revisions are what get deployed to gateways, so you can edit the "current" API without affecting live traffic.

Scope
:   A permission name, such as `order:write`. You attach it to API resources, and a token must contain it to call those resources.

Subscriber
:   A Developer Portal user, as APIM sees them (`AM_SUBSCRIBER`). The row is created the first time the user does something in the portal.

Subscription
:   The link that says "this application may call this API, under this tier". Stored in `AM_SUBSCRIPTION`.

Tenant
:   An isolated slice of an APIM deployment, with its own users, APIs and applications. The default tenant is `carbon.super` (ID `-1234`).

Tier / throttling policy
:   A rate limit, such as *Gold: 5000 requests/min*. There are policies at the subscription, application, resource (API) and global (custom) levels.

VHost (4.x)
:   A virtual host (hostname plus ports) inside a gateway environment. An API revision is deployed to an environment *and* a VHost.

Workflow
:   An approval step that can be put in front of actions such as creating an application or subscribing. Tracked in `AM_WORKFLOWS`.
