# IDP_* — Identity providers

12 tables. Generated from the 3.2.0 DDL.

## IDP

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `TENANT_ID, NAME`; `UUID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` |  |
| `NAME` | `VARCHAR(254)` | NOT NULL |
| `IS_ENABLED` | `CHAR(1)` | NOT NULL DEFAULT '1' |
| `IS_PRIMARY` | `CHAR(1)` | NOT NULL DEFAULT '0' |
| `HOME_REALM_ID` | `VARCHAR(254)` |  |
| `IMAGE` | `MEDIUMBLOB` |  |
| `CERTIFICATE` | `BLOB` |  |
| `ALIAS` | `VARCHAR(254)` |  |
| `INBOUND_PROV_ENABLED` | `CHAR (1)` | NOT NULL DEFAULT '0' |
| `INBOUND_PROV_USER_STORE_ID` | `VARCHAR(254)` |  |
| `USER_CLAIM_URI` | `VARCHAR(254)` |  |
| `ROLE_CLAIM_URI` | `VARCHAR(254)` |  |
| `DESCRIPTION` | `VARCHAR (1024)` |  |
| `DEFAULT_AUTHENTICATOR_NAME` | `VARCHAR(254)` |  |
| `DEFAULT_PRO_CONNECTOR_NAME` | `VARCHAR(254)` |  |
| `PROVISIONING_ROLE` | `VARCHAR(128)` |  |
| `IS_FEDERATION_HUB` | `CHAR(1)` | NOT NULL DEFAULT '0' |
| `IS_LOCAL_CLAIM_DIALECT` | `CHAR(1)` | NOT NULL DEFAULT '0' |
| `DISPLAY_NAME` | `VARCHAR(255)` |  |
| `IMAGE_URL` | `VARCHAR(1024)` |  |
| `UUID` | `CHAR(36)` | NOT NULL |

**Referenced by**

- [`IDN_ASSOCIATED_ID`](idn.md#idn_associated_id) via `IDP_ID`
- [`IDP_AUTHENTICATOR`](#idp_authenticator) via `IDP_ID`
- [`IDP_CLAIM`](#idp_claim) via `IDP_ID`
- [`IDP_LOCAL_CLAIM`](#idp_local_claim) via `IDP_ID`
- [`IDP_METADATA`](#idp_metadata) via `IDP_ID`
- [`IDP_PROVISIONING_CONFIG`](#idp_provisioning_config) via `IDP_ID`
- [`IDP_ROLE`](#idp_role) via `IDP_ID`

## IDP_AUTHENTICATOR

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `TENANT_ID, IDP_ID, NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` |  |
| `IDP_ID` | `INTEGER` | FK → IDP |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `IS_ENABLED` | `CHAR (1)` | DEFAULT '1' |
| `DISPLAY_NAME` | `VARCHAR(255)` |  |

**Foreign keys**

- `IDP_ID` → [`IDP`](#idp) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDP_AUTHENTICATOR_PROPERTY`](#idp_authenticator_property) via `AUTHENTICATOR_ID`

## IDP_AUTHENTICATOR_PROPERTY

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `TENANT_ID, AUTHENTICATOR_ID, PROPERTY_KEY`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` |  |
| `AUTHENTICATOR_ID` | `INTEGER` | FK → IDP_AUTHENTICATOR |
| `PROPERTY_KEY` | `VARCHAR(255)` | NOT NULL |
| `PROPERTY_VALUE` | `VARCHAR(2047)` |  |
| `IS_SECRET` | `CHAR (1)` | DEFAULT '0' |

**Foreign keys**

- `AUTHENTICATOR_ID` → [`IDP_AUTHENTICATOR`](#idp_authenticator) `ID` (on delete: CASCADE)

## IDP_CLAIM

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `IDP_ID, CLAIM`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `IDP_ID` | `INTEGER` | FK → IDP |
| `TENANT_ID` | `INTEGER` |  |
| `CLAIM` | `VARCHAR(254)` |  |

**Foreign keys**

- `IDP_ID` → [`IDP`](#idp) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDP_CLAIM_MAPPING`](#idp_claim_mapping) via `IDP_CLAIM_ID`

## IDP_CLAIM_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `IDP_CLAIM_ID, TENANT_ID, LOCAL_CLAIM`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `IDP_CLAIM_ID` | `INTEGER` | FK → IDP_CLAIM |
| `TENANT_ID` | `INTEGER` |  |
| `LOCAL_CLAIM` | `VARCHAR(253)` |  |
| `DEFAULT_VALUE` | `VARCHAR(255)` |  |
| `IS_REQUESTED` | `VARCHAR(128)` | DEFAULT '0' |

**Foreign keys**

- `IDP_CLAIM_ID` → [`IDP_CLAIM`](#idp_claim) `ID` (on delete: CASCADE)

## IDP_LOCAL_CLAIM

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `TENANT_ID, IDP_ID, CLAIM_URI`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` |  |
| `IDP_ID` | `INTEGER` | FK → IDP |
| `CLAIM_URI` | `VARCHAR(255)` | NOT NULL |
| `DEFAULT_VALUE` | `VARCHAR(255)` |  |
| `IS_REQUESTED` | `VARCHAR(128)` | DEFAULT '0' |

**Foreign keys**

- `IDP_ID` → [`IDP`](#idp) `ID` (on delete: CASCADE)

## IDP_METADATA

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `IDP_ID, NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `IDP_ID` | `INTEGER` | FK → IDP |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `VALUE` | `VARCHAR(255)` | NOT NULL |
| `DISPLAY_NAME` | `VARCHAR(255)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `IDP_ID` → [`IDP`](#idp) `ID` (on delete: CASCADE)

## IDP_PROVISIONING_CONFIG

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `TENANT_ID, IDP_ID, PROVISIONING_CONNECTOR_TYPE`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` |  |
| `IDP_ID` | `INTEGER` | FK → IDP |
| `PROVISIONING_CONNECTOR_TYPE` | `VARCHAR(255)` | NOT NULL |
| `IS_ENABLED` | `CHAR (1)` | DEFAULT '0' |
| `IS_BLOCKING` | `CHAR (1)` | DEFAULT '0' |
| `IS_RULES_ENABLED` | `CHAR (1)` | DEFAULT '0' |

**Foreign keys**

- `IDP_ID` → [`IDP`](#idp) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDP_PROVISIONING_ENTITY`](#idp_provisioning_entity) via `PROVISIONING_CONFIG_ID`
- [`IDP_PROV_CONFIG_PROPERTY`](#idp_prov_config_property) via `PROVISIONING_CONFIG_ID`

## IDP_PROVISIONING_ENTITY

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `ENTITY_TYPE, TENANT_ID, ENTITY_LOCAL_USERSTORE, ENTITY_NAME, PROVISIONING_CONFIG_ID`; `PROVISIONING_CONFIG_ID, ENTITY_TYPE, ENTITY_VALUE`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `PROVISIONING_CONFIG_ID` | `INTEGER` | FK → IDP_PROVISIONING_CONFIG |
| `ENTITY_TYPE` | `VARCHAR(255)` | NOT NULL |
| `ENTITY_LOCAL_USERSTORE` | `VARCHAR(255)` | NOT NULL |
| `ENTITY_NAME` | `VARCHAR(255)` | NOT NULL |
| `ENTITY_VALUE` | `VARCHAR(255)` |  |
| `TENANT_ID` | `INTEGER` |  |
| `ENTITY_LOCAL_ID` | `VARCHAR(255)` |  |

**Foreign keys**

- `PROVISIONING_CONFIG_ID` → [`IDP_PROVISIONING_CONFIG`](#idp_provisioning_config) `ID` (on delete: CASCADE)

## IDP_PROV_CONFIG_PROPERTY

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `TENANT_ID, PROVISIONING_CONFIG_ID, PROPERTY_KEY`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TENANT_ID` | `INTEGER` |  |
| `PROVISIONING_CONFIG_ID` | `INTEGER` | FK → IDP_PROVISIONING_CONFIG |
| `PROPERTY_KEY` | `VARCHAR(255)` | NOT NULL |
| `PROPERTY_VALUE` | `VARCHAR(2048)` |  |
| `PROPERTY_BLOB_VALUE` | `BLOB` |  |
| `PROPERTY_TYPE` | `CHAR(32)` | NOT NULL |
| `IS_SECRET` | `CHAR (1)` | DEFAULT '0' |

**Foreign keys**

- `PROVISIONING_CONFIG_ID` → [`IDP_PROVISIONING_CONFIG`](#idp_provisioning_config) `ID` (on delete: CASCADE)

## IDP_ROLE

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `IDP_ID, ROLE`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `IDP_ID` | `INTEGER` | FK → IDP |
| `TENANT_ID` | `INTEGER` |  |
| `ROLE` | `VARCHAR(254)` |  |

**Foreign keys**

- `IDP_ID` → [`IDP`](#idp) `ID` (on delete: CASCADE)

**Referenced by**

- [`IDP_ROLE_MAPPING`](#idp_role_mapping) via `IDP_ROLE_ID`

## IDP_ROLE_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `IDP_ROLE_ID, TENANT_ID, USER_STORE_ID, LOCAL_ROLE`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `IDP_ROLE_ID` | `INTEGER` | FK → IDP_ROLE |
| `TENANT_ID` | `INTEGER` |  |
| `USER_STORE_ID` | `VARCHAR (253)` |  |
| `LOCAL_ROLE` | `VARCHAR(253)` |  |

**Foreign keys**

- `IDP_ROLE_ID` → [`IDP_ROLE`](#idp_role) `ID` (on delete: CASCADE)

