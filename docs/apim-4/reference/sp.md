# SP_* — Service providers

13 tables. Generated from the 4.7.0 DDL.

## SP_APP

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `APP_NAME, TENANT_ID`; `UUID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `APP_NAME` | `VARCHAR (255)` | NOT NULL |
| `USER_STORE` | `VARCHAR (255)` | NOT NULL |
| `USERNAME` | `VARCHAR (255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR (1024)` |  |
| `ROLE_CLAIM` | `VARCHAR (512)` |  |
| `AUTH_TYPE` | `VARCHAR (255)` | NOT NULL |
| `PROVISIONING_USERSTORE_DOMAIN` | `VARCHAR (512)` |  |
| `IS_LOCAL_CLAIM_DIALECT` | `CHAR(1)` | DEFAULT '1' |
| `IS_SEND_LOCAL_SUBJECT_ID` | `CHAR(1)` | DEFAULT '0' |
| `IS_SEND_AUTH_LIST_OF_IDPS` | `CHAR(1)` | DEFAULT '0' |
| `IS_USE_TENANT_DOMAIN_SUBJECT` | `CHAR(1)` | DEFAULT '1' |
| `IS_USE_USER_DOMAIN_SUBJECT` | `CHAR(1)` | DEFAULT '1' |
| `ENABLE_AUTHORIZATION` | `CHAR(1)` | DEFAULT '0' |
| `SUBJECT_CLAIM_URI` | `VARCHAR (512)` |  |
| `IS_SAAS_APP` | `CHAR(1)` | DEFAULT '0' |
| `IS_DUMB_MODE` | `CHAR(1)` | DEFAULT '0' |
| `UUID` | `CHAR(36)` |  |
| `IMAGE_URL` | `VARCHAR(1024)` |  |
| `ACCESS_URL` | `VARCHAR(1024)` |  |
| `IS_DISCOVERABLE` | `CHAR(1)` | DEFAULT '0' |

**Referenced by**

- [`IDN_CORS_ASSOCIATION`](idn.md#idn_cors_association) via `SP_APP_ID`
- [`IDN_OAUTH2_USER_CONSENT`](idn.md#idn_oauth2_user_consent) via `APP_ID`
- [`SP_AUTH_STEP`](#sp_auth_step) via `APP_ID`
- [`SP_CLAIM_DIALECT`](#sp_claim_dialect) via `APP_ID`
- [`SP_CLAIM_MAPPING`](#sp_claim_mapping) via `APP_ID`
- [`SP_INBOUND_AUTH`](#sp_inbound_auth) via `APP_ID`
- [`SP_METADATA`](#sp_metadata) via `SP_ID`
- [`SP_PROVISIONING_CONNECTOR`](#sp_provisioning_connector) via `APP_ID`
- [`SP_REQ_PATH_AUTHENTICATOR`](#sp_req_path_authenticator) via `APP_ID`
- [`SP_ROLE_MAPPING`](#sp_role_mapping) via `APP_ID`
- [`SP_SHARED_APP`](#sp_shared_app) via `MAIN_APP_ID`
- [`SP_SHARED_APP`](#sp_shared_app) via `SHARED_APP_ID`

## SP_AUTH_SCRIPT

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `APP_ID` | `INTEGER` | NOT NULL |
| `TYPE` | `VARCHAR(255)` | NOT NULL |
| `CONTENT` | `BLOB` | DEFAULT NULL |
| `IS_ENABLED` | `CHAR(1)` | NOT NULL DEFAULT '0' |

**Likely links (no FK)**

- `APP_ID` → [`SP_APP`](#sp_app) *(name-hint)*

## SP_AUTH_STEP

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `STEP_ORDER` | `INTEGER` | DEFAULT 1 |
| `APP_ID` | `INTEGER` | FK → SP_APP · NOT NULL |
| `IS_SUBJECT_STEP` | `CHAR(1)` | DEFAULT '0' |
| `IS_ATTRIBUTE_STEP` | `CHAR(1)` | DEFAULT '0' |

**Foreign keys**

- `APP_ID` → [`SP_APP`](#sp_app) `ID` (on delete: CASCADE)

**Referenced by**

- [`SP_FEDERATED_IDP`](#sp_federated_idp) via `ID`

## SP_CLAIM_DIALECT

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `SP_DIALECT` | `VARCHAR (512)` | NOT NULL |
| `APP_ID` | `INTEGER` | FK → SP_APP · NOT NULL |

**Foreign keys**

- `APP_ID` → [`SP_APP`](#sp_app) `ID` (on delete: CASCADE)

## SP_CLAIM_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `IDP_CLAIM` | `VARCHAR (512)` | NOT NULL |
| `SP_CLAIM` | `VARCHAR (512)` | NOT NULL |
| `APP_ID` | `INTEGER` | FK → SP_APP · NOT NULL |
| `IS_REQUESTED` | `VARCHAR(128)` | DEFAULT '0' |
| `IS_MANDATORY` | `VARCHAR(128)` | DEFAULT '0' |
| `DEFAULT_VALUE` | `VARCHAR(255)` |  |

**Foreign keys**

- `APP_ID` → [`SP_APP`](#sp_app) `ID` (on delete: CASCADE)

## SP_FEDERATED_IDP

*APIM DB (WSO2AM_DB)* · PK: `ID, AUTHENTICATOR_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · FK → SP_AUTH_STEP · NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `AUTHENTICATOR_ID` | `INTEGER` | PK · NOT NULL |

**Foreign keys**

- `ID` → [`SP_AUTH_STEP`](#sp_auth_step) `ID` (on delete: CASCADE)

## SP_INBOUND_AUTH

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `INBOUND_AUTH_KEY` | `VARCHAR (255)` |  |
| `INBOUND_AUTH_TYPE` | `VARCHAR (255)` | NOT NULL |
| `INBOUND_CONFIG_TYPE` | `VARCHAR (255)` | NOT NULL |
| `PROP_NAME` | `VARCHAR (255)` |  |
| `PROP_VALUE` | `VARCHAR (1024)` |  |
| `APP_ID` | `INTEGER` | FK → SP_APP · NOT NULL |

**Foreign keys**

- `APP_ID` → [`SP_APP`](#sp_app) `ID` (on delete: CASCADE)

## SP_METADATA

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `SP_ID, NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `SP_ID` | `INTEGER` | FK → SP_APP |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `VALUE` | `VARCHAR(255)` | NOT NULL |
| `DISPLAY_NAME` | `VARCHAR(255)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `SP_ID` → [`SP_APP`](#sp_app) `ID` (on delete: CASCADE)

## SP_PROVISIONING_CONNECTOR

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `IDP_NAME` | `VARCHAR (255)` | NOT NULL |
| `CONNECTOR_NAME` | `VARCHAR (255)` | NOT NULL |
| `APP_ID` | `INTEGER` | FK → SP_APP · NOT NULL |
| `IS_JIT_ENABLED` | `CHAR(1)` | NOT NULL DEFAULT '0' |
| `BLOCKING` | `CHAR(1)` | NOT NULL DEFAULT '0' |
| `RULE_ENABLED` | `CHAR(1)` | NOT NULL DEFAULT '0' |

**Foreign keys**

- `APP_ID` → [`SP_APP`](#sp_app) `ID` (on delete: CASCADE)

## SP_REQ_PATH_AUTHENTICATOR

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `AUTHENTICATOR_NAME` | `VARCHAR (255)` | NOT NULL |
| `APP_ID` | `INTEGER` | FK → SP_APP · NOT NULL |

**Foreign keys**

- `APP_ID` → [`SP_APP`](#sp_app) `ID` (on delete: CASCADE)

## SP_ROLE_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `IDP_ROLE` | `VARCHAR (255)` | NOT NULL |
| `SP_ROLE` | `VARCHAR (255)` | NOT NULL |
| `APP_ID` | `INTEGER` | FK → SP_APP · NOT NULL |

**Foreign keys**

- `APP_ID` → [`SP_APP`](#sp_app) `ID` (on delete: CASCADE)

## SP_SHARED_APP

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `MAIN_APP_ID, OWNER_ORG_ID, SHARED_ORG_ID`; `SHARED_APP_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `MAIN_APP_ID` | `CHAR(36)` | FK → SP_APP · NOT NULL |
| `OWNER_ORG_ID` | `CHAR(36)` | NOT NULL |
| `SHARED_APP_ID` | `CHAR(36)` | FK → SP_APP · NOT NULL |
| `SHARED_ORG_ID` | `CHAR(36)` | NOT NULL |

**Foreign keys**

- `MAIN_APP_ID` → [`SP_APP`](#sp_app) `UUID` (on delete: CASCADE)
- `SHARED_APP_ID` → [`SP_APP`](#sp_app) `UUID` (on delete: CASCADE)

## SP_TEMPLATE

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `TENANT_ID, NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1023)` |  |
| `CONTENT` | `BLOB` | DEFAULT NULL |

