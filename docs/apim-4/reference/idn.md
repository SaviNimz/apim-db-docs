# IDN_* — Identity & OAuth

77 tables. Generated from the 4.7.0 DDL.

## IDN_APP_REVOKED_EVENT

*APIM DB (WSO2AM_DB)* · PK: `EVENT_ID` · Unique: `CONSUMER_KEY, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `EVENT_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `CONSUMER_KEY` | `VARCHAR(255)` | NOT NULL |
| `TIME_REVOKED` | `TIMESTAMP` | NOT NULL |
| `ORGANIZATION` | `VARCHAR(100)` |  |

**Likely links (no FK)**

- `CONSUMER_KEY` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) *(name-hint)*

## IDN_ASSOCIATED_ID

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `IDP_USER_ID, TENANT_ID, IDP_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `IDP_USER_ID` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | DEFAULT -1234 |
| `IDP_ID` | `INTEGER` | FK → IDP · NOT NULL |
| `DOMAIN_NAME` | `VARCHAR(255)` | NOT NULL |
| `USER_NAME` | `VARCHAR(255)` | NOT NULL |
| `ASSOCIATION_ID` | `CHAR(36)` | NOT NULL |

**Foreign keys**

- `IDP_ID` → [`IDP`](idp.md#idp) `ID` (on delete: CASCADE)

## IDN_AUTH_SESSION_APP_INFO

*APIM DB (WSO2AM_DB)* · PK: `SESSION_ID, SUBJECT, APP_ID, INBOUND_AUTH_TYPE`

| Column | Type | Notes |
|---|---|---|
| `SESSION_ID` | `VARCHAR (100)` | PK · NOT NULL |
| `SUBJECT` | `VARCHAR (100)` | PK · NOT NULL |
| `APP_ID` | `INTEGER` | PK · NOT NULL |
| `INBOUND_AUTH_TYPE` | `VARCHAR (255)` | PK · NOT NULL |

## IDN_AUTH_SESSION_META_DATA

*APIM DB (WSO2AM_DB)* · PK: `SESSION_ID, PROPERTY_TYPE, VALUE`

| Column | Type | Notes |
|---|---|---|
| `SESSION_ID` | `VARCHAR (100)` | PK · NOT NULL |
| `PROPERTY_TYPE` | `VARCHAR (100)` | PK · NOT NULL |
| `VALUE` | `VARCHAR (255)` | PK · NOT NULL |

## IDN_AUTH_SESSION_STORE

*APIM DB (WSO2AM_DB)* · PK: `SESSION_ID, SESSION_TYPE, TIME_CREATED, OPERATION`

| Column | Type | Notes |
|---|---|---|
| `SESSION_ID` | `VARCHAR (100)` | PK · NOT NULL |
| `SESSION_TYPE` | `VARCHAR(100)` | PK · NOT NULL |
| `OPERATION` | `VARCHAR(10)` | PK · NOT NULL |
| `SESSION_OBJECT` | `BLOB` |  |
| `TIME_CREATED` | `BIGINT` | PK |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |
| `EXPIRY_TIME` | `BIGINT` |  |

## IDN_AUTH_TEMP_SESSION_STORE

*APIM DB (WSO2AM_DB)* · PK: `SESSION_ID, SESSION_TYPE, TIME_CREATED, OPERATION`

| Column | Type | Notes |
|---|---|---|
| `SESSION_ID` | `VARCHAR (100)` | PK · NOT NULL |
| `SESSION_TYPE` | `VARCHAR(100)` | PK · NOT NULL |
| `OPERATION` | `VARCHAR(10)` | PK · NOT NULL |
| `SESSION_OBJECT` | `BLOB` |  |
| `TIME_CREATED` | `BIGINT` | PK |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |
| `EXPIRY_TIME` | `BIGINT` |  |

## IDN_AUTH_USER

*APIM DB (WSO2AM_DB)* · PK: `USER_ID` · Unique: `USER_NAME, TENANT_ID, DOMAIN_NAME, IDP_ID`

| Column | Type | Notes |
|---|---|---|
| `USER_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `USER_NAME` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `DOMAIN_NAME` | `VARCHAR(255)` | NOT NULL |
| `IDP_ID` | `INTEGER` | NOT NULL |

## IDN_AUTH_USER_SESSION_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `USER_ID, SESSION_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `USER_ID` | `VARCHAR(255)` | NOT NULL |
| `SESSION_ID` | `VARCHAR(255)` | NOT NULL |

## IDN_AUTH_WAIT_STATUS

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `LONG_WAIT_KEY`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `LONG_WAIT_KEY` | `VARCHAR(255)` | NOT NULL |
| `WAIT_STATUS` | `CHAR(1)` | NOT NULL DEFAULT '1' |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `EXPIRE_TIME` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |

## IDN_BASE_TABLE

*APIM DB (WSO2AM_DB)* · PK: `PRODUCT_NAME`

| Column | Type | Notes |
|---|---|---|
| `PRODUCT_NAME` | `VARCHAR(20)` | PK |

## IDN_CERTIFICATE

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `NAME, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `NAME` | `VARCHAR(100)` |  |
| `CERTIFICATE_IN_PEM` | `BLOB` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT 0 |

## IDN_CLAIM

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `DIALECT_ID, CLAIM_URI, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `DIALECT_ID` | `INTEGER` | FK → IDN_CLAIM_DIALECT · NOT NULL |
| `CLAIM_URI` | `VARCHAR (255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |

**Foreign keys**

- `DIALECT_ID` → [`IDN_CLAIM_DIALECT`](#idn_claim_dialect) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDN_CLAIM_MAPPED_ATTRIBUTE`](#idn_claim_mapped_attribute) via `LOCAL_CLAIM_ID`
- [`IDN_CLAIM_MAPPING`](#idn_claim_mapping) via `EXT_CLAIM_ID`
- [`IDN_CLAIM_MAPPING`](#idn_claim_mapping) via `MAPPED_LOCAL_CLAIM_ID`
- [`IDN_CLAIM_PROPERTY`](#idn_claim_property) via `LOCAL_CLAIM_ID`
- [`IDN_OIDC_SCOPE_CLAIM_MAPPING`](#idn_oidc_scope_claim_mapping) via `EXTERNAL_CLAIM_ID`

## IDN_CLAIM_DIALECT

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `DIALECT_URI, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `DIALECT_URI` | `VARCHAR (255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |

**Referenced by**

- [`IDN_CLAIM`](#idn_claim) via `DIALECT_ID`

## IDN_CLAIM_MAPPED_ATTRIBUTE

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `LOCAL_CLAIM_ID, USER_STORE_DOMAIN_NAME, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `LOCAL_CLAIM_ID` | `INTEGER` | FK → IDN_CLAIM |
| `USER_STORE_DOMAIN_NAME` | `VARCHAR (255)` | NOT NULL |
| `ATTRIBUTE_NAME` | `VARCHAR (255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |

**Foreign keys**

- `LOCAL_CLAIM_ID` → [`IDN_CLAIM`](#idn_claim) `ID` (on delete: CASCADE)

## IDN_CLAIM_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `EXT_CLAIM_ID, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `EXT_CLAIM_ID` | `INTEGER` | FK → IDN_CLAIM · NOT NULL |
| `MAPPED_LOCAL_CLAIM_ID` | `INTEGER` | FK → IDN_CLAIM · NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |

**Foreign keys**

- `EXT_CLAIM_ID` → [`IDN_CLAIM`](#idn_claim) `ID` (on delete: CASCADE)
- `MAPPED_LOCAL_CLAIM_ID` → [`IDN_CLAIM`](#idn_claim) `ID` (on delete: CASCADE)

## IDN_CLAIM_PROPERTY

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `LOCAL_CLAIM_ID, PROPERTY_NAME, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `LOCAL_CLAIM_ID` | `INTEGER` | FK → IDN_CLAIM |
| `PROPERTY_NAME` | `VARCHAR (255)` | NOT NULL |
| `PROPERTY_VALUE` | `VARCHAR (255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |

**Foreign keys**

- `LOCAL_CLAIM_ID` → [`IDN_CLAIM`](#idn_claim) `ID` (on delete: CASCADE)

## IDN_CONFIG_ATTRIBUTE

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `RESOURCE_ID(64`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `RESOURCE_ID` | `VARCHAR(255)` | FK → IDN_CONFIG_RESOURCE · NOT NULL |
| `ATTR_KEY` | `VARCHAR(255)` | NOT NULL |
| `ATTR_VALUE` | `VARCHAR(1023)` | NULL |

**Foreign keys**

- `RESOURCE_ID` → [`IDN_CONFIG_RESOURCE`](#idn_config_resource) `ID` (on delete: CASCADE)

## IDN_CONFIG_FILE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `VALUE` | `BLOB` | NULL |
| `RESOURCE_ID` | `VARCHAR(255)` | FK → IDN_CONFIG_RESOURCE · NOT NULL |
| `NAME` | `VARCHAR(255)` | NULL |

**Foreign keys**

- `RESOURCE_ID` → [`IDN_CONFIG_RESOURCE`](#idn_config_resource) `ID` (on delete: CASCADE)

## IDN_CONFIG_RESOURCE

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `NAME, TENANT_ID, TYPE_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `TENANT_ID` | `INT` | NOT NULL |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `CREATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `LAST_MODIFIED` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `HAS_FILE` | `TINYINT(1)` | NOT NULL |
| `HAS_ATTRIBUTE` | `TINYINT(1)` | NOT NULL |
| `TYPE_ID` | `VARCHAR(255)` | FK → IDN_CONFIG_TYPE · NOT NULL |

**Foreign keys**

- `TYPE_ID` → [`IDN_CONFIG_TYPE`](#idn_config_type) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDN_CONFIG_ATTRIBUTE`](#idn_config_attribute) via `RESOURCE_ID`
- [`IDN_CONFIG_FILE`](#idn_config_file) via `RESOURCE_ID`

## IDN_CONFIG_TYPE

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1023)` | NULL |

**Referenced by**

- [`IDN_CONFIG_RESOURCE`](#idn_config_resource) via `TYPE_ID`

## IDN_CORS_ASSOCIATION

*APIM DB (WSO2AM_DB)* · PK: `IDN_CORS_ORIGIN_ID, SP_APP_ID`

| Column | Type | Notes |
|---|---|---|
| `IDN_CORS_ORIGIN_ID` | `INT` | PK · FK → IDN_CORS_ORIGIN · NOT NULL |
| `SP_APP_ID` | `INT` | PK · FK → SP_APP · NOT NULL |

**Foreign keys**

- `IDN_CORS_ORIGIN_ID` → [`IDN_CORS_ORIGIN`](#idn_cors_origin) `ID` (on delete: CASCADE)
- `SP_APP_ID` → [`SP_APP`](sp.md#sp_app) `ID` (on delete: CASCADE)

## IDN_CORS_ORIGIN

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `UUID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INT` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INT` | NOT NULL |
| `ORIGIN` | `VARCHAR(2048)` | NOT NULL |
| `UUID` | `CHAR(36)` | NOT NULL |

**Referenced by**

- [`IDN_CORS_ASSOCIATION`](#idn_cors_association) via `IDN_CORS_ORIGIN_ID`

## IDN_FED_AUTH_SESSION_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `IDP_SESSION_ID, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `IDP_SESSION_ID` | `VARCHAR(255)` | NOT NULL |
| `SESSION_ID` | `VARCHAR(255)` | NOT NULL |
| `IDP_NAME` | `VARCHAR(255)` | NOT NULL |
| `AUTHENTICATOR_ID` | `VARCHAR(255)` |  |
| `PROTOCOL_TYPE` | `VARCHAR(255)` |  |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `TENANT_ID` | `INTEGER` | NOT NULL DEFAULT 0 |

## IDN_FUNCTION_LIBRARY

*APIM DB (WSO2AM_DB)* · PK: `TENANT_ID, NAME`

| Column | Type | Notes |
|---|---|---|
| `NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `DESCRIPTION` | `VARCHAR(1023)` |  |
| `TYPE` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | PK · NOT NULL |
| `DATA` | `BLOB` | NOT NULL |

## IDN_IDENTITY_META_DATA

*APIM DB (WSO2AM_DB)* · PK: `TENANT_ID, USER_NAME, METADATA_TYPE, METADATA`

| Column | Type | Notes |
|---|---|---|
| `USER_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `TENANT_ID` | `INTEGER` | PK · DEFAULT -1234 |
| `METADATA_TYPE` | `VARCHAR(255)` | PK · NOT NULL |
| `METADATA` | `VARCHAR(255)` | PK · NOT NULL |
| `VALID` | `VARCHAR(255)` | NOT NULL |

## IDN_IDENTITY_USER_DATA

*APIM DB (WSO2AM_DB)* · PK: `TENANT_ID, USER_NAME, DATA_KEY`

| Column | Type | Notes |
|---|---|---|
| `TENANT_ID` | `INTEGER` | PK · DEFAULT -1234 |
| `USER_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `DATA_KEY` | `VARCHAR(255)` | PK · NOT NULL |
| `DATA_VALUE` | `VARCHAR(2048)` |  |

## IDN_INVALID_TOKENS

*APIM DB (WSO2AM_DB)* · PK: `UUID`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(255)` | PK · NOT NULL |
| `TOKEN_IDENTIFIER` | `VARCHAR(2048)` | CHARACTER SET latin1 COLLATE latin1_bin NOT NULL |
| `CONSUMER_KEY` | `VARCHAR(255)` | CHARACTER SET latin1 COLLATE latin1_bin NOT NULL |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `EXPIRY_TIMESTAMP` | `TIMESTAMP` | NOT NULL |

**Likely links (no FK)**

- `CONSUMER_KEY` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) *(name-hint)*

## IDN_OAUTH1A_ACCESS_TOKEN

*APIM DB (WSO2AM_DB)* · PK: `ACCESS_TOKEN`

| Column | Type | Notes |
|---|---|---|
| `ACCESS_TOKEN` | `VARCHAR(255)` | PK |
| `ACCESS_TOKEN_SECRET` | `VARCHAR(512)` |  |
| `CONSUMER_KEY_ID` | `INTEGER` | FK → IDN_OAUTH_CONSUMER_APPS |
| `SCOPE` | `VARCHAR(2048)` |  |
| `AUTHZ_USER` | `VARCHAR(512)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `CONSUMER_KEY_ID` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `ID` (on delete: CASCADE)

## IDN_OAUTH1A_REQUEST_TOKEN

*APIM DB (WSO2AM_DB)* · PK: `REQUEST_TOKEN`

| Column | Type | Notes |
|---|---|---|
| `REQUEST_TOKEN` | `VARCHAR(255)` | PK |
| `REQUEST_TOKEN_SECRET` | `VARCHAR(512)` |  |
| `CONSUMER_KEY_ID` | `INTEGER` | FK → IDN_OAUTH_CONSUMER_APPS |
| `CALLBACK_URL` | `VARCHAR(2048)` |  |
| `SCOPE` | `VARCHAR(2048)` |  |
| `AUTHORIZED` | `VARCHAR(128)` |  |
| `OAUTH_VERIFIER` | `VARCHAR(512)` |  |
| `AUTHZ_USER` | `VARCHAR(512)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `CONSUMER_KEY_ID` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `ID` (on delete: CASCADE)

## IDN_OAUTH2_ACCESS_TOKEN

*APIM DB (WSO2AM_DB)* · PK: `TOKEN_ID`

| Column | Type | Notes |
|---|---|---|
| `TOKEN_ID` | `VARCHAR (255)` | PK |
| `ACCESS_TOKEN` | `VARCHAR(2048)` |  |
| `REFRESH_TOKEN` | `VARCHAR(2048)` |  |
| `CONSUMER_KEY_ID` | `INTEGER` | FK → IDN_OAUTH_CONSUMER_APPS |
| `AUTHZ_USER` | `VARCHAR (100)` |  |
| `TENANT_ID` | `INTEGER` |  |
| `USER_DOMAIN` | `VARCHAR(50)` |  |
| `USER_TYPE` | `VARCHAR (25)` |  |
| `GRANT_TYPE` | `VARCHAR (50)` |  |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `REFRESH_TOKEN_TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `VALIDITY_PERIOD` | `BIGINT` |  |
| `REFRESH_TOKEN_VALIDITY_PERIOD` | `BIGINT` |  |
| `TOKEN_SCOPE_HASH` | `VARCHAR(32)` |  |
| `TOKEN_STATE` | `VARCHAR(25)` | DEFAULT 'ACTIVE' |
| `TOKEN_STATE_ID` | `VARCHAR (128)` | DEFAULT 'NONE' |
| `SUBJECT_IDENTIFIER` | `VARCHAR(255)` |  |
| `ACCESS_TOKEN_HASH` | `VARCHAR(512)` |  |
| `REFRESH_TOKEN_HASH` | `VARCHAR(512)` |  |
| `IDP_ID` | `INTEGER` | DEFAULT -1 NOT NULL |
| `TOKEN_BINDING_REF` | `VARCHAR (32)` | DEFAULT 'NONE' |
| `CONSENTED_TOKEN` | `VARCHAR(6)` |  |

**Foreign keys**

- `CONSUMER_KEY_ID` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDN_OAUTH2_ACCESS_TOKEN_SCOPE`](#idn_oauth2_access_token_scope) via `TOKEN_ID`
- [`IDN_OAUTH2_TOKEN_BINDING`](#idn_oauth2_token_binding) via `TOKEN_ID`
- [`IDN_OIDC_REQ_OBJECT_REFERENCE`](#idn_oidc_req_object_reference) via `TOKEN_ID`

## IDN_OAUTH2_ACCESS_TOKEN_AUDIT

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TOKEN_ID` | `VARCHAR (255)` |  |
| `ACCESS_TOKEN` | `VARCHAR(2048)` |  |
| `REFRESH_TOKEN` | `VARCHAR(2048)` |  |
| `CONSUMER_KEY_ID` | `INTEGER` |  |
| `AUTHZ_USER` | `VARCHAR (100)` |  |
| `TENANT_ID` | `INTEGER` |  |
| `USER_DOMAIN` | `VARCHAR(50)` |  |
| `USER_TYPE` | `VARCHAR (25)` |  |
| `GRANT_TYPE` | `VARCHAR (50)` |  |
| `TIME_CREATED` | `TIMESTAMP` | NULL |
| `REFRESH_TOKEN_TIME_CREATED` | `TIMESTAMP` | NULL |
| `VALIDITY_PERIOD` | `BIGINT` |  |
| `REFRESH_TOKEN_VALIDITY_PERIOD` | `BIGINT` |  |
| `TOKEN_SCOPE_HASH` | `VARCHAR(32)` |  |
| `TOKEN_STATE` | `VARCHAR(25)` |  |
| `TOKEN_STATE_ID` | `VARCHAR (128)` |  |
| `SUBJECT_IDENTIFIER` | `VARCHAR(255)` |  |
| `ACCESS_TOKEN_HASH` | `VARCHAR(512)` |  |
| `REFRESH_TOKEN_HASH` | `VARCHAR(512)` |  |
| `INVALIDATED_TIME` | `TIMESTAMP` | NULL |
| `IDP_ID` | `INTEGER` | DEFAULT -1 NOT NULL |

**Likely links (no FK)**

- `TOKEN_ID` → [`IDN_OAUTH2_ACCESS_TOKEN`](#idn_oauth2_access_token) *(name-hint)*

## IDN_OAUTH2_ACCESS_TOKEN_SCOPE

*APIM DB (WSO2AM_DB)* · PK: `TOKEN_ID, TOKEN_SCOPE`

| Column | Type | Notes |
|---|---|---|
| `TOKEN_ID` | `VARCHAR (255)` | PK · FK → IDN_OAUTH2_ACCESS_TOKEN |
| `TOKEN_SCOPE` | `VARCHAR (100)` | PK |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `TOKEN_ID` → [`IDN_OAUTH2_ACCESS_TOKEN`](#idn_oauth2_access_token) `TOKEN_ID` (on delete: CASCADE)

## IDN_OAUTH2_AUTHORIZATION_CODE

*APIM DB (WSO2AM_DB)* · PK: `CODE_ID`

| Column | Type | Notes |
|---|---|---|
| `CODE_ID` | `VARCHAR (255)` | PK |
| `AUTHORIZATION_CODE` | `VARCHAR(2048)` |  |
| `CONSUMER_KEY_ID` | `INTEGER` | FK → IDN_OAUTH_CONSUMER_APPS |
| `CALLBACK_URL` | `VARCHAR(2048)` |  |
| `SCOPE` | `VARCHAR(2048)` |  |
| `AUTHZ_USER` | `VARCHAR (100)` |  |
| `TENANT_ID` | `INTEGER` |  |
| `USER_DOMAIN` | `VARCHAR(50)` |  |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `VALIDITY_PERIOD` | `BIGINT` |  |
| `STATE` | `VARCHAR (25)` | DEFAULT 'ACTIVE' |
| `TOKEN_ID` | `VARCHAR(255)` |  |
| `SUBJECT_IDENTIFIER` | `VARCHAR(255)` |  |
| `PKCE_CODE_CHALLENGE` | `VARCHAR(255)` |  |
| `PKCE_CODE_CHALLENGE_METHOD` | `VARCHAR(128)` |  |
| `AUTHORIZATION_CODE_HASH` | `VARCHAR(512)` |  |
| `IDP_ID` | `INTEGER` | DEFAULT -1 NOT NULL |

**Foreign keys**

- `CONSUMER_KEY_ID` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDN_OAUTH2_AUTHZ_CODE_SCOPE`](#idn_oauth2_authz_code_scope) via `CODE_ID`
- [`IDN_OIDC_REQ_OBJECT_REFERENCE`](#idn_oidc_req_object_reference) via `CODE_ID`

**Likely links (no FK)**

- `TOKEN_ID` → [`IDN_OAUTH2_ACCESS_TOKEN`](#idn_oauth2_access_token) *(name-hint)*

## IDN_OAUTH2_AUTHZ_CODE_SCOPE

*APIM DB (WSO2AM_DB)* · PK: `CODE_ID, SCOPE`

| Column | Type | Notes |
|---|---|---|
| `CODE_ID` | `VARCHAR(255)` | PK · FK → IDN_OAUTH2_AUTHORIZATION_CODE |
| `SCOPE` | `VARCHAR(60)` | PK |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `CODE_ID` → [`IDN_OAUTH2_AUTHORIZATION_CODE`](#idn_oauth2_authorization_code) `CODE_ID` (on delete: CASCADE)

## IDN_OAUTH2_CIBA_AUTH_CODE

*APIM DB (WSO2AM_DB)* · PK: `AUTH_CODE_KEY` · Unique: `AUTH_REQ_ID`

| Column | Type | Notes |
|---|---|---|
| `AUTH_CODE_KEY` | `CHAR (36)` | PK |
| `AUTH_REQ_ID` | `CHAR (36)` |  |
| `ISSUED_TIME` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `CONSUMER_KEY` | `VARCHAR(255)` | FK → IDN_OAUTH_CONSUMER_APPS |
| `LAST_POLLED_TIME` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `POLLING_INTERVAL` | `INTEGER` |  |
| `EXPIRES_IN` | `INTEGER` |  |
| `AUTHENTICATED_USER_NAME` | `VARCHAR(255)` |  |
| `USER_STORE_DOMAIN` | `VARCHAR(100)` |  |
| `TENANT_ID` | `INTEGER` |  |
| `AUTH_REQ_STATUS` | `VARCHAR (100)` | DEFAULT 'REQUESTED' |
| `IDP_ID` | `INTEGER` |  |

**Foreign keys**

- `CONSUMER_KEY` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `CONSUMER_KEY` (on delete: CASCADE)

**Referenced by**

- [`IDN_OAUTH2_CIBA_REQUEST_SCOPES`](#idn_oauth2_ciba_request_scopes) via `AUTH_CODE_KEY`

## IDN_OAUTH2_CIBA_REQUEST_SCOPES

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `AUTH_CODE_KEY` | `CHAR (36)` | FK → IDN_OAUTH2_CIBA_AUTH_CODE |
| `SCOPE` | `VARCHAR (255)` |  |

**Foreign keys**

- `AUTH_CODE_KEY` → [`IDN_OAUTH2_CIBA_AUTH_CODE`](#idn_oauth2_ciba_auth_code) `AUTH_CODE_KEY` (on delete: CASCADE)

## IDN_OAUTH2_DEVICE_FLOW

*APIM DB (WSO2AM_DB)* · PK: `DEVICE_CODE` · Unique: `CODE_ID`; `USER_CODE, QUANTIFIER`

| Column | Type | Notes |
|---|---|---|
| `CODE_ID` | `VARCHAR(255)` |  |
| `DEVICE_CODE` | `VARCHAR(255)` | PK |
| `USER_CODE` | `VARCHAR(25)` |  |
| `QUANTIFIER` | `INTEGER` | NOT NULL DEFAULT 0 |
| `CONSUMER_KEY_ID` | `INTEGER` | FK → IDN_OAUTH_CONSUMER_APPS |
| `LAST_POLL_TIME` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `EXPIRY_TIME` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `POLL_TIME` | `BIGINT` |  |
| `STATUS` | `VARCHAR (25)` | DEFAULT 'PENDING' |
| `AUTHZ_USER` | `VARCHAR (100)` |  |
| `TENANT_ID` | `INTEGER` |  |
| `USER_DOMAIN` | `VARCHAR(50)` |  |
| `IDP_ID` | `INTEGER` |  |

**Foreign keys**

- `CONSUMER_KEY_ID` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDN_OAUTH2_DEVICE_FLOW_SCOPES`](#idn_oauth2_device_flow_scopes) via `SCOPE_ID`

## IDN_OAUTH2_DEVICE_FLOW_SCOPES

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `SCOPE_ID` | `VARCHAR(255)` | FK → IDN_OAUTH2_DEVICE_FLOW |
| `SCOPE` | `VARCHAR(255)` |  |

**Foreign keys**

- `SCOPE_ID` → [`IDN_OAUTH2_DEVICE_FLOW`](#idn_oauth2_device_flow) `CODE_ID` (on delete: CASCADE)

## IDN_OAUTH2_RESOURCE_SCOPE

*APIM DB (WSO2AM_DB)* · PK: `RESOURCE_PATH`

| Column | Type | Notes |
|---|---|---|
| `RESOURCE_PATH` | `VARCHAR(255)` | PK · NOT NULL |
| `SCOPE_ID` | `INTEGER` | FK → IDN_OAUTH2_SCOPE · NOT NULL |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `SCOPE_ID` → [`IDN_OAUTH2_SCOPE`](#idn_oauth2_scope) `SCOPE_ID` (on delete: CASCADE)

## IDN_OAUTH2_SCOPE

*APIM DB (WSO2AM_DB)* · PK: `SCOPE_ID` · Unique: `NAME, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `SCOPE_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `DISPLAY_NAME` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(512)` |  |
| `TENANT_ID` | `INTEGER` | NOT NULL DEFAULT -1 |
| `SCOPE_TYPE` | `VARCHAR(255)` | NOT NULL |

**Referenced by**

- [`IDN_OAUTH2_RESOURCE_SCOPE`](#idn_oauth2_resource_scope) via `SCOPE_ID`
- [`IDN_OAUTH2_SCOPE_BINDING`](#idn_oauth2_scope_binding) via `SCOPE_ID`
- [`IDN_OIDC_SCOPE_CLAIM_MAPPING`](#idn_oidc_scope_claim_mapping) via `SCOPE_ID`

## IDN_OAUTH2_SCOPE_BINDING

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `SCOPE_ID, SCOPE_BINDING, BINDING_TYPE`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `SCOPE_ID` | `INTEGER` | FK → IDN_OAUTH2_SCOPE · NOT NULL |
| `SCOPE_BINDING` | `VARCHAR(255)` | NOT NULL |
| `BINDING_TYPE` | `VARCHAR(255)` | NOT NULL |

**Foreign keys**

- `SCOPE_ID` → [`IDN_OAUTH2_SCOPE`](#idn_oauth2_scope) `SCOPE_ID` (on delete: CASCADE)

## IDN_OAUTH2_SCOPE_VALIDATORS

*APIM DB (WSO2AM_DB)* · PK: `APP_ID, SCOPE_VALIDATOR`

| Column | Type | Notes |
|---|---|---|
| `APP_ID` | `INTEGER` | PK · FK → IDN_OAUTH_CONSUMER_APPS · NOT NULL |
| `SCOPE_VALIDATOR` | `VARCHAR (128)` | PK · NOT NULL |

**Foreign keys**

- `APP_ID` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `ID` (on delete: CASCADE)

## IDN_OAUTH2_TOKEN_BINDING

*APIM DB (WSO2AM_DB)* · PK: `—` · Unique: `TOKEN_ID, TOKEN_BINDING_TYPE, TOKEN_BINDING_VALUE`

| Column | Type | Notes |
|---|---|---|
| `TOKEN_ID` | `VARCHAR (255)` | FK → IDN_OAUTH2_ACCESS_TOKEN |
| `TOKEN_BINDING_TYPE` | `VARCHAR (32)` | CHARACTER SET latin1 COLLATE latin1_bin |
| `TOKEN_BINDING_REF` | `VARCHAR (32)` |  |
| `TOKEN_BINDING_VALUE` | `VARCHAR (1024)` | CHARACTER SET latin1 COLLATE latin1_bin |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `TOKEN_ID` → [`IDN_OAUTH2_ACCESS_TOKEN`](#idn_oauth2_access_token) `TOKEN_ID` (on delete: CASCADE)

## IDN_OAUTH2_USER_CONSENT

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `USER_ID, APP_ID, TENANT_ID`; `CONSENT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `USER_ID` | `VARCHAR(255)` | NOT NULL |
| `APP_ID` | `CHAR(36)` | FK → SP_APP · NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL DEFAULT -1 |
| `CONSENT_ID` | `VARCHAR(255)` | NOT NULL |

**Foreign keys**

- `APP_ID` → [`SP_APP`](sp.md#sp_app) `UUID` (on delete: CASCADE)

**Referenced by**

- [`IDN_OAUTH2_USER_CONSENTED_SCOPES`](#idn_oauth2_user_consented_scopes) via `CONSENT_ID`

**Likely links (no FK)**

- `CONSENT_ID` → [`IDN_OAUTH2_USER_CONSENTED_SCOPES`](#idn_oauth2_user_consented_scopes) *(same-name key)*

## IDN_OAUTH2_USER_CONSENTED_SCOPES

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `CONSENT_ID, SCOPE`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `CONSENT_ID` | `VARCHAR(255)` | FK → IDN_OAUTH2_USER_CONSENT · NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL DEFAULT -1 |
| `SCOPE` | `VARCHAR(255)` | NOT NULL |
| `CONSENT` | `BOOLEAN` | NOT NULL DEFAULT 1 |

**Foreign keys**

- `CONSENT_ID` → [`IDN_OAUTH2_USER_CONSENT`](#idn_oauth2_user_consent) `CONSENT_ID` (on delete: CASCADE)

## IDN_OAUTH_CONSUMER_APPS

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `CONSUMER_KEY`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `CONSUMER_KEY` | `VARCHAR(255)` |  |
| `CONSUMER_SECRET` | `VARCHAR(2048)` |  |
| `USERNAME` | `VARCHAR(255)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT 0 |
| `USER_DOMAIN` | `VARCHAR(50)` |  |
| `APP_NAME` | `VARCHAR(255)` |  |
| `OAUTH_VERSION` | `VARCHAR(128)` |  |
| `CALLBACK_URL` | `VARCHAR(2048)` |  |
| `GRANT_TYPES` | `VARCHAR (1024)` |  |
| `PKCE_MANDATORY` | `CHAR(1)` | DEFAULT '0' |
| `PKCE_SUPPORT_PLAIN` | `CHAR(1)` | DEFAULT '0' |
| `APP_STATE` | `VARCHAR (25)` | DEFAULT 'ACTIVE' |
| `USER_ACCESS_TOKEN_EXPIRE_TIME` | `BIGINT` | DEFAULT 3600 |
| `APP_ACCESS_TOKEN_EXPIRE_TIME` | `BIGINT` | DEFAULT 3600 |
| `REFRESH_TOKEN_EXPIRE_TIME` | `BIGINT` | DEFAULT 84600 |
| `ID_TOKEN_EXPIRE_TIME` | `BIGINT` | DEFAULT 3600 |

**Referenced by**

- [`IDN_OAUTH1A_ACCESS_TOKEN`](#idn_oauth1a_access_token) via `CONSUMER_KEY_ID`
- [`IDN_OAUTH1A_REQUEST_TOKEN`](#idn_oauth1a_request_token) via `CONSUMER_KEY_ID`
- [`IDN_OAUTH2_ACCESS_TOKEN`](#idn_oauth2_access_token) via `CONSUMER_KEY_ID`
- [`IDN_OAUTH2_AUTHORIZATION_CODE`](#idn_oauth2_authorization_code) via `CONSUMER_KEY_ID`
- [`IDN_OAUTH2_CIBA_AUTH_CODE`](#idn_oauth2_ciba_auth_code) via `CONSUMER_KEY`
- [`IDN_OAUTH2_DEVICE_FLOW`](#idn_oauth2_device_flow) via `CONSUMER_KEY_ID`
- [`IDN_OAUTH2_SCOPE_VALIDATORS`](#idn_oauth2_scope_validators) via `APP_ID`
- [`IDN_OAUTH_CONSUMER_SECRETS`](#idn_oauth_consumer_secrets) via `CONSUMER_KEY`
- [`IDN_OIDC_PROPERTY`](#idn_oidc_property) via `CONSUMER_KEY`
- [`IDN_OIDC_REQ_OBJECT_REFERENCE`](#idn_oidc_req_object_reference) via `CONSUMER_KEY_ID`

## IDN_OAUTH_CONSUMER_SECRETS

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `SECRET_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `SECRET_ID` | `VARCHAR(100)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1024)` |  |
| `CONSUMER_KEY` | `VARCHAR(255)` | FK → IDN_OAUTH_CONSUMER_APPS · NOT NULL |
| `SECRET_VALUE` | `VARCHAR(2048)` | NOT NULL |
| `SECRET_HASH` | `VARCHAR(512)` | NOT NULL |
| `EXPIRY_TIME` | `BIGINT` |  |

**Foreign keys**

- `CONSUMER_KEY` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `CONSUMER_KEY` (on delete: CASCADE)

## IDN_OIDC_JTI

*APIM DB (WSO2AM_DB)* · PK: `JWT_ID`

| Column | Type | Notes |
|---|---|---|
| `JWT_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `EXP_TIME` | `TIMESTAMP` | NOT NULL |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |

## IDN_OIDC_PROPERTY

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` |  |
| `CONSUMER_KEY` | `VARCHAR(255)` | FK → IDN_OAUTH_CONSUMER_APPS |
| `PROPERTY_KEY` | `VARCHAR(255)` | NOT NULL |
| `PROPERTY_VALUE` | `VARCHAR(2047)` |  |

**Foreign keys**

- `CONSUMER_KEY` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `CONSUMER_KEY` (on delete: CASCADE)

## IDN_OIDC_REQ_OBJECT_CLAIMS

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `REQ_OBJECT_ID` | `INTEGER` | FK → IDN_OIDC_REQ_OBJECT_REFERENCE |
| `CLAIM_ATTRIBUTE` | `VARCHAR(255)` |  |
| `ESSENTIAL` | `CHAR(1)` | NOT NULL DEFAULT '0' |
| `VALUE` | `VARCHAR(255)` |  |
| `IS_USERINFO` | `CHAR(1)` | NOT NULL DEFAULT '0' |

**Foreign keys**

- `REQ_OBJECT_ID` → [`IDN_OIDC_REQ_OBJECT_REFERENCE`](#idn_oidc_req_object_reference) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDN_OIDC_REQ_OBJ_CLAIM_VALUES`](#idn_oidc_req_obj_claim_values) via `REQ_OBJECT_CLAIMS_ID`

## IDN_OIDC_REQ_OBJECT_REFERENCE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `CONSUMER_KEY_ID` | `INTEGER` | FK → IDN_OAUTH_CONSUMER_APPS |
| `CODE_ID` | `VARCHAR(255)` | FK → IDN_OAUTH2_AUTHORIZATION_CODE |
| `TOKEN_ID` | `VARCHAR(255)` | FK → IDN_OAUTH2_ACCESS_TOKEN |
| `SESSION_DATA_KEY` | `VARCHAR(255)` |  |

**Foreign keys**

- `CONSUMER_KEY_ID` → [`IDN_OAUTH_CONSUMER_APPS`](#idn_oauth_consumer_apps) `ID` (on delete: CASCADE)
- `TOKEN_ID` → [`IDN_OAUTH2_ACCESS_TOKEN`](#idn_oauth2_access_token) `TOKEN_ID` (on delete: CASCADE)
- `CODE_ID` → [`IDN_OAUTH2_AUTHORIZATION_CODE`](#idn_oauth2_authorization_code) `CODE_ID` (on delete: CASCADE)

**Referenced by**

- [`IDN_OIDC_REQ_OBJECT_CLAIMS`](#idn_oidc_req_object_claims) via `REQ_OBJECT_ID`

## IDN_OIDC_REQ_OBJ_CLAIM_VALUES

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `REQ_OBJECT_CLAIMS_ID` | `INTEGER` | FK → IDN_OIDC_REQ_OBJECT_CLAIMS |
| `CLAIM_VALUES` | `VARCHAR(255)` |  |

**Foreign keys**

- `REQ_OBJECT_CLAIMS_ID` → [`IDN_OIDC_REQ_OBJECT_CLAIMS`](#idn_oidc_req_object_claims) `ID` (on delete: CASCADE)

## IDN_OIDC_SCOPE_CLAIM_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `SCOPE_ID, EXTERNAL_CLAIM_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `SCOPE_ID` | `INTEGER` | FK → IDN_OAUTH2_SCOPE · NOT NULL |
| `EXTERNAL_CLAIM_ID` | `INTEGER` | FK → IDN_CLAIM · NOT NULL |

**Foreign keys**

- `SCOPE_ID` → [`IDN_OAUTH2_SCOPE`](#idn_oauth2_scope) `SCOPE_ID` (on delete: CASCADE)
- `EXTERNAL_CLAIM_ID` → [`IDN_CLAIM`](#idn_claim) `ID` (on delete: CASCADE)

## IDN_OPENID_ASSOCIATIONS

*APIM DB (WSO2AM_DB)* · PK: `HANDLE`

| Column | Type | Notes |
|---|---|---|
| `HANDLE` | `VARCHAR(255)` | PK · NOT NULL |
| `ASSOC_TYPE` | `VARCHAR(255)` | NOT NULL |
| `EXPIRE_IN` | `TIMESTAMP` | NOT NULL |
| `MAC_KEY` | `VARCHAR(255)` | NOT NULL |
| `ASSOC_STORE` | `VARCHAR(128)` | DEFAULT 'SHARED' |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

## IDN_OPENID_REMEMBER_ME

*APIM DB (WSO2AM_DB)* · PK: `USER_NAME, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `USER_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |
| `COOKIE_VALUE` | `VARCHAR(1024)` |  |
| `CREATED_TIME` | `TIMESTAMP` |  |

## IDN_OPENID_USER_RPS

*APIM DB (WSO2AM_DB)* · PK: `USER_NAME, TENANT_ID, RP_URL`

| Column | Type | Notes |
|---|---|---|
| `USER_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |
| `RP_URL` | `VARCHAR(255)` | PK · NOT NULL |
| `TRUSTED_ALWAYS` | `VARCHAR(128)` | DEFAULT 'FALSE' |
| `LAST_VISIT` | `DATE` | NOT NULL |
| `VISIT_COUNT` | `INTEGER` | DEFAULT 0 |
| `DEFAULT_PROFILE_NAME` | `VARCHAR(255)` | DEFAULT 'DEFAULT' |

## IDN_PASSWORD_HISTORY_DATA

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `USER_NAME` | `VARCHAR(255)` | NOT NULL |
| `USER_DOMAIN` | `VARCHAR(127)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |
| `SALT_VALUE` | `VARCHAR(255)` |  |
| `HASH` | `VARCHAR(255)` | NOT NULL |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |

## IDN_RECOVERY_DATA

*APIM DB (WSO2AM_DB)* · PK: `USER_NAME, USER_DOMAIN, TENANT_ID, SCENARIO, STEP` · Unique: `CODE`

| Column | Type | Notes |
|---|---|---|
| `USER_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `USER_DOMAIN` | `VARCHAR(127)` | PK · NOT NULL |
| `TENANT_ID` | `INTEGER` | PK · DEFAULT -1 |
| `CODE` | `VARCHAR(255)` | NOT NULL |
| `SCENARIO` | `VARCHAR(255)` | PK · NOT NULL |
| `STEP` | `VARCHAR(127)` | PK · NOT NULL |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `REMAINING_SETS` | `VARCHAR(2500)` | DEFAULT NULL |

## IDN_REMOTE_FETCH_CONFIG

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `TENANT_ID, CONFIG_DEPLOYER_TYPE`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `TENANT_ID` | `INT` | NOT NULL |
| `IS_ENABLED` | `CHAR(1)` | NOT NULL |
| `REPO_MANAGER_TYPE` | `VARCHAR(255)` | NOT NULL |
| `ACTION_LISTENER_TYPE` | `VARCHAR(255)` | NOT NULL |
| `CONFIG_DEPLOYER_TYPE` | `VARCHAR(255)` | NOT NULL |
| `REMOTE_FETCH_NAME` | `VARCHAR(255)` |  |
| `REMOTE_RESOURCE_URI` | `VARCHAR(255)` | NOT NULL |
| `ATTRIBUTES_JSON` | `MEDIUMTEXT` | NOT NULL |

**Referenced by**

- [`IDN_REMOTE_FETCH_REVISIONS`](#idn_remote_fetch_revisions) via `CONFIG_ID`

## IDN_REMOTE_FETCH_REVISIONS

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `CONFIG_ID, ITEM_NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `CONFIG_ID` | `VARCHAR(255)` | FK → IDN_REMOTE_FETCH_CONFIG · NOT NULL |
| `FILE_PATH` | `VARCHAR(255)` | NOT NULL |
| `FILE_HASH` | `VARCHAR(255)` |  |
| `DEPLOYED_DATE` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `LAST_SYNC_TIME` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `DEPLOYMENT_STATUS` | `VARCHAR(255)` |  |
| `ITEM_NAME` | `VARCHAR(255)` |  |
| `DEPLOY_ERR_LOG` | `MEDIUMTEXT` |  |

**Foreign keys**

- `CONFIG_ID` → [`IDN_REMOTE_FETCH_CONFIG`](#idn_remote_fetch_config) `ID` (on delete: CASCADE)

## IDN_SAML2_ARTIFACT_STORE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INT(11)` | PK · NOT NULL AUTO_INCREMENT |
| `SOURCE_ID` | `VARCHAR(255)` | NOT NULL |
| `MESSAGE_HANDLER` | `VARCHAR(255)` | NOT NULL |
| `AUTHN_REQ_DTO` | `BLOB` | NOT NULL |
| `SESSION_ID` | `VARCHAR(255)` | NOT NULL |
| `EXP_TIMESTAMP` | `TIMESTAMP` | NOT NULL |
| `INIT_TIMESTAMP` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `ASSERTION_ID` | `VARCHAR(255)` |  |

## IDN_SAML2_ASSERTION_STORE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `SAML2_ID` | `VARCHAR(255)` |  |
| `SAML2_ISSUER` | `VARCHAR(255)` |  |
| `SAML2_SUBJECT` | `VARCHAR(255)` |  |
| `SAML2_SESSION_INDEX` | `VARCHAR(255)` |  |
| `SAML2_AUTHN_CONTEXT_CLASS_REF` | `VARCHAR(255)` |  |
| `SAML2_ASSERTION` | `VARCHAR(4096)` |  |
| `ASSERTION` | `BLOB` |  |

## IDN_SCIM_GROUP

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `TENANT_ID, ROLE_NAME, ATTR_NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `ROLE_NAME` | `VARCHAR(255)` | CHARACTER SET latin1 COLLATE latin1_bin NOT NULL |
| `ATTR_NAME` | `VARCHAR(1024)` | CHARACTER SET latin1 COLLATE latin1_bin NOT NULL |
| `ATTR_VALUE` | `VARCHAR(1024)` |  |

## IDN_SECRET

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `SECRET_NAME, TENANT_ID, TYPE_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `TENANT_ID` | `INT` | NOT NULL |
| `SECRET_NAME` | `VARCHAR(255)` | NOT NULL |
| `SECRET_VALUE` | `VARCHAR(8000)` | NOT NULL |
| `CREATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `LAST_MODIFIED` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `TYPE_ID` | `VARCHAR(255)` | FK → IDN_SECRET_TYPE · NOT NULL |
| `DESCRIPTION` | `VARCHAR(1023)` | NULL |

**Foreign keys**

- `TYPE_ID` → [`IDN_SECRET_TYPE`](#idn_secret_type) `ID` (on delete: CASCADE)

## IDN_SECRET_TYPE

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1023)` | NULL |

**Referenced by**

- [`IDN_SECRET`](#idn_secret) via `TYPE_ID`

## IDN_STS_STORE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TOKEN_ID` | `VARCHAR(255)` | NOT NULL |
| `TOKEN_CONTENT` | `BLOB(1024)` | NOT NULL |
| `CREATE_DATE` | `TIMESTAMP` | NOT NULL |
| `EXPIRE_DATE` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `STATE` | `INTEGER` | DEFAULT 0 |

## IDN_SUBJECT_ENTITY_REVOKED_EVENT

*APIM DB (WSO2AM_DB)* · PK: `EVENT_ID` · Unique: `ENTITY_ID, ENTITY_TYPE, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `EVENT_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `ENTITY_ID` | `VARCHAR(255)` | NOT NULL |
| `ENTITY_TYPE` | `VARCHAR(100)` | NOT NULL |
| `TIME_REVOKED` | `TIMESTAMP` | NOT NULL |
| `ORGANIZATION` | `VARCHAR(100)` |  |

**Likely links (no FK)**

- `ENTITY_ID` → [`AM_SUBJECT_ENTITY_REVOKED_EVENT`](am.md#am_subject_entity_revoked_event) *(same-name key)*

## IDN_THRIFT_SESSION

*APIM DB (WSO2AM_DB)* · PK: `SESSION_ID`

| Column | Type | Notes |
|---|---|---|
| `SESSION_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `USER_NAME` | `VARCHAR(255)` | NOT NULL |
| `CREATED_TIME` | `VARCHAR(255)` | NOT NULL |
| `LAST_MODIFIED_TIME` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

## IDN_UMA_PERMISSION_TICKET

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT NOT NULL |
| `PT` | `VARCHAR(255)` | NOT NULL |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `EXPIRY_TIME` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `TICKET_STATE` | `VARCHAR(25)` | DEFAULT 'ACTIVE' |
| `TENANT_ID` | `INTEGER` | DEFAULT -1234 |
| `TOKEN_ID` | `VARCHAR(255)` |  |

**Referenced by**

- [`IDN_UMA_PT_RESOURCE`](#idn_uma_pt_resource) via `PT_ID`

## IDN_UMA_PT_RESOURCE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT NOT NULL |
| `PT_RESOURCE_ID` | `INTEGER` | FK → IDN_UMA_RESOURCE · NOT NULL |
| `PT_ID` | `INTEGER` | FK → IDN_UMA_PERMISSION_TICKET · NOT NULL |

**Foreign keys**

- `PT_ID` → [`IDN_UMA_PERMISSION_TICKET`](#idn_uma_permission_ticket) `ID` (on delete: CASCADE)
- `PT_RESOURCE_ID` → [`IDN_UMA_RESOURCE`](#idn_uma_resource) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDN_UMA_PT_RESOURCE_SCOPE`](#idn_uma_pt_resource_scope) via `PT_RESOURCE_ID`

## IDN_UMA_PT_RESOURCE_SCOPE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT NOT NULL |
| `PT_RESOURCE_ID` | `INTEGER` | FK → IDN_UMA_PT_RESOURCE · NOT NULL |
| `PT_SCOPE_ID` | `INTEGER` | FK → IDN_UMA_RESOURCE_SCOPE · NOT NULL |

**Foreign keys**

- `PT_RESOURCE_ID` → [`IDN_UMA_PT_RESOURCE`](#idn_uma_pt_resource) `ID` (on delete: CASCADE)
- `PT_SCOPE_ID` → [`IDN_UMA_RESOURCE_SCOPE`](#idn_uma_resource_scope) `ID` (on delete: CASCADE)

## IDN_UMA_RESOURCE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT NOT NULL |
| `RESOURCE_ID` | `VARCHAR(255)` |  |
| `RESOURCE_NAME` | `VARCHAR(255)` |  |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL |
| `RESOURCE_OWNER_NAME` | `VARCHAR(255)` |  |
| `CLIENT_ID` | `VARCHAR(255)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT -1234 |
| `USER_DOMAIN` | `VARCHAR(50)` |  |

**Referenced by**

- [`IDN_UMA_PT_RESOURCE`](#idn_uma_pt_resource) via `PT_RESOURCE_ID`
- [`IDN_UMA_RESOURCE_META_DATA`](#idn_uma_resource_meta_data) via `RESOURCE_IDENTITY`
- [`IDN_UMA_RESOURCE_SCOPE`](#idn_uma_resource_scope) via `RESOURCE_IDENTITY`

## IDN_UMA_RESOURCE_META_DATA

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT NOT NULL |
| `RESOURCE_IDENTITY` | `INTEGER` | FK → IDN_UMA_RESOURCE · NOT NULL |
| `PROPERTY_KEY` | `VARCHAR(40)` |  |
| `PROPERTY_VALUE` | `VARCHAR(255)` |  |

**Foreign keys**

- `RESOURCE_IDENTITY` → [`IDN_UMA_RESOURCE`](#idn_uma_resource) `ID` (on delete: CASCADE)

## IDN_UMA_RESOURCE_SCOPE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT NOT NULL |
| `RESOURCE_IDENTITY` | `INTEGER` | FK → IDN_UMA_RESOURCE · NOT NULL |
| `SCOPE_NAME` | `VARCHAR(255)` |  |

**Foreign keys**

- `RESOURCE_IDENTITY` → [`IDN_UMA_RESOURCE`](#idn_uma_resource) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDN_UMA_PT_RESOURCE_SCOPE`](#idn_uma_pt_resource_scope) via `PT_SCOPE_ID`

## IDN_USER_ACCOUNT_ASSOCIATION

*APIM DB (WSO2AM_DB)* · PK: `TENANT_ID, DOMAIN_NAME, USER_NAME`

| Column | Type | Notes |
|---|---|---|
| `ASSOCIATION_KEY` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | PK |
| `DOMAIN_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `USER_NAME` | `VARCHAR(255)` | PK · NOT NULL |

## IDN_USER_FUNCTIONALITY_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `USER_ID, TENANT_ID, FUNCTIONALITY_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `USER_ID` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `FUNCTIONALITY_ID` | `VARCHAR(255)` | NOT NULL |
| `IS_FUNCTIONALITY_LOCKED` | `BOOLEAN` | NOT NULL |
| `FUNCTIONALITY_UNLOCK_TIME` | `BIGINT` | NOT NULL |
| `FUNCTIONALITY_LOCK_REASON` | `VARCHAR(1023)` |  |
| `FUNCTIONALITY_LOCK_REASON_CODE` | `VARCHAR(255)` |  |

**Likely links (no FK)**

- `FUNCTIONALITY_ID` → [`IDN_USER_FUNCTIONALITY_PROPERTY`](#idn_user_functionality_property) *(same-name key)*

## IDN_USER_FUNCTIONALITY_PROPERTY

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `USER_ID, TENANT_ID, FUNCTIONALITY_ID, PROPERTY_NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `USER_ID` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `FUNCTIONALITY_ID` | `VARCHAR(255)` | NOT NULL |
| `PROPERTY_NAME` | `VARCHAR(255)` |  |
| `PROPERTY_VALUE` | `VARCHAR(255)` |  |

**Likely links (no FK)**

- `FUNCTIONALITY_ID` → [`IDN_USER_FUNCTIONALITY_MAPPING`](#idn_user_functionality_mapping) *(same-name key)*

