# AM_* — API Manager core

112 tables in APIM 4.7.0.

## AM_ALERT_EMAILLIST

*APIM DB (WSO2AM_DB)* · PK: `EMAIL_LIST_ID, USER_NAME, STAKE_HOLDER`

| Column | Type | Notes |
|---|---|---|
| `EMAIL_LIST_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `USER_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `STAKE_HOLDER` | `VARCHAR(100)` | PK · NOT NULL |

## AM_ALERT_EMAILLIST_DETAILS

*APIM DB (WSO2AM_DB)* · PK: `EMAIL_LIST_ID, EMAIL`

| Column | Type | Notes |
|---|---|---|
| `EMAIL_LIST_ID` | `INTEGER` | PK |
| `EMAIL` | `VARCHAR(255)` | PK |

## AM_ALERT_TYPES

*APIM DB (WSO2AM_DB)* · PK: `ALERT_TYPE_ID`

| Column | Type | Notes |
|---|---|---|
| `ALERT_TYPE_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `ALERT_TYPE_NAME` | `VARCHAR(255)` | NOT NULL |
| `STAKE_HOLDER` | `VARCHAR(100)` | NOT NULL |

## AM_ALERT_TYPES_VALUES

*APIM DB (WSO2AM_DB)* · PK: `ALERT_TYPE_ID, USER_NAME, STAKE_HOLDER`

| Column | Type | Notes |
|---|---|---|
| `ALERT_TYPE_ID` | `INTEGER` | PK |
| `USER_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `STAKE_HOLDER` | `VARCHAR(100)` | PK · NOT NULL |

## AM_API

*APIM DB (WSO2AM_DB)* · PK: `API_ID` · Unique: `API_PROVIDER, API_NAME, API_VERSION, ORGANIZATION`; `API_UUID`

| Column | Type | Notes |
|---|---|---|
| `API_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `API_UUID` | `VARCHAR(256)` |  |
| `API_PROVIDER` | `VARCHAR(200)` |  |
| `API_NAME` | `VARCHAR(200)` |  |
| `API_VERSION` | `VARCHAR(30)` |  |
| `CONTEXT` | `VARCHAR(256)` |  |
| `CONTEXT_TEMPLATE` | `VARCHAR(256)` |  |
| `API_TIER` | `VARCHAR(256)` |  |
| `API_TYPE` | `VARCHAR(10)` |  |
| `API_SUBTYPE` | `VARCHAR(100)` |  |
| `ORGANIZATION` | `VARCHAR(100)` |  |
| `GATEWAY_VENDOR` | `VARCHAR(100)` | DEFAULT 'wso2' |
| `CREATED_BY` | `VARCHAR(100)` |  |
| `CREATED_TIME` | `TIMESTAMP` |  |
| `UPDATED_BY` | `VARCHAR(100)` |  |
| `UPDATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `STATUS` | `VARCHAR(30)` |  |
| `LOG_LEVEL` | `VARCHAR(255)` | DEFAULT 'OFF' |
| `IS_EGRESS` | `INTEGER` | DEFAULT 0 |
| `REVISIONS_CREATED` | `INTEGER` | DEFAULT 0 |
| `VERSION_COMPARABLE` | `VARCHAR(15)` |  |
| `SUB_VALIDATION` | `VARCHAR(10)` | DEFAULT 'ENABLED' |
| `API_DISPLAY_NAME` | `VARCHAR(256)` |  |
| `INITIATED_FROM_GW` | `INTEGER` | DEFAULT 0 |

**Referenced by**

- [`AM_API_AI_CONFIGURATION`](#am_api_ai_configuration) via `API_UUID`
- [`AM_API_CLIENT_CERTIFICATE`](#am_api_client_certificate) via `API_ID`
- [`AM_API_COMMENTS`](#am_api_comments) via `API_ID`
- [`AM_API_ENDPOINTS`](#am_api_endpoints) via `API_UUID`
- [`AM_API_ENVIRONMENT_KEYS`](#am_api_environment_keys) via `API_UUID`
- [`AM_API_EXTERNAL_API_MAPPING`](#am_api_external_api_mapping) via `API_ID`
- [`AM_API_KEY_API_MAPPING`](#am_api_key_api_mapping) via `API_UUID`
- [`AM_API_LABEL_MAPPING`](#am_api_label_mapping) via `API_UUID`
- [`AM_API_LC_EVENT`](#am_api_lc_event) via `API_ID`
- [`AM_API_METADATA`](#am_api_metadata) via `API_UUID`
- [`AM_API_POLICY_MAPPING`](#am_api_policy_mapping) via `API_UUID`
- [`AM_API_PRIMARY_EP_MAPPING`](#am_api_primary_ep_mapping) via `API_UUID`
- [`AM_API_PRODUCT_MAPPING`](#am_api_product_mapping) via `API_ID`
- [`AM_API_RATINGS`](#am_api_ratings) via `API_ID`
- [`AM_API_SEQUENCE_BACKEND`](#am_api_sequence_backend) via `API_UUID`
- [`AM_API_SERVICE_MAPPING`](#am_api_service_mapping) via `API_ID`
- [`AM_BACKEND`](#am_backend) via `REFERENCE_API_UUID`
- [`AM_EXTERNAL_STORES`](#am_external_stores) via `API_ID`
- [`AM_GRAPHQL_COMPLEXITY`](#am_graphql_complexity) via `API_ID`
- [`AM_GW_REVISION_DEPLOYMENT`](#am_gw_revision_deployment) via `API_ID`
- [`AM_REVISION`](#am_revision) via `API_UUID`
- [`AM_SECURITY_AUDIT_UUID_MAPPING`](#am_security_audit_uuid_mapping) via `API_ID`
- [`AM_SUBSCRIPTION`](#am_subscription) via `API_ID`

## AM_API_AI_CONFIGURATION

*APIM DB (WSO2AM_DB)* · PK: `AI_CONFIGURATION_UUID`

| Column | Type | Notes |
|---|---|---|
| `AI_CONFIGURATION_UUID` | `VARCHAR(255)` | PK · NOT NULL |
| `API_UUID` | `VARCHAR(256)` | FK → AM_API · NOT NULL |
| `API_REVISION_UUID` | `VARCHAR(255)` |  |
| `LLM_PROVIDER_UUID` | `VARCHAR(255)` | FK → AM_LLM_PROVIDER · NOT NULL |

**Foreign keys**

- `API_UUID` → [`AM_API`](#am_api) `API_UUID`
- `LLM_PROVIDER_UUID` → [`AM_LLM_PROVIDER`](#am_llm_provider) `UUID`

## AM_API_CATEGORIES

*APIM DB (WSO2AM_DB)* · PK: `UUID` · Unique: `NAME, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(50)` | PK |
| `NAME` | `VARCHAR(255)` |  |
| `DESCRIPTION` | `VARCHAR(1024)` |  |
| `ORGANIZATION` | `VARCHAR(100)` |  |

## AM_API_CLIENT_CERTIFICATE

*APIM DB (WSO2AM_DB)* · PK: `ALIAS, TENANT_ID, KEY_TYPE, REMOVED, REVISION_UUID`

| Column | Type | Notes |
|---|---|---|
| `TENANT_ID` | `INT(11)` | PK · NOT NULL |
| `ALIAS` | `VARCHAR(45)` | PK · NOT NULL |
| `API_ID` | `INTEGER` | FK → AM_API · NOT NULL |
| `CERTIFICATE` | `BLOB` | NOT NULL |
| `REMOVED` | `BOOLEAN` | PK · NOT NULL DEFAULT 0 |
| `TIER_NAME` | `VARCHAR (512)` |  |
| `KEY_TYPE` | `VARCHAR(20)` | PK · NOT NULL DEFAULT 'PRODUCTION' |
| `REVISION_UUID` | `VARCHAR(255)` | PK · NOT NULL DEFAULT 'Current API' |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: CASCADE)

**Related tables (not enforced)**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_API_COMMENTS

*APIM DB (WSO2AM_DB)* · PK: `COMMENT_ID`

| Column | Type | Notes |
|---|---|---|
| `COMMENT_ID` | `VARCHAR(64)` | PK · NOT NULL |
| `COMMENT_TEXT` | `VARCHAR(512)` |  |
| `CREATED_BY` | `VARCHAR(512)` |  |
| `CREATED_TIME` | `TIMESTAMP` | NOT NULL |
| `UPDATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `API_ID` | `INTEGER` | FK → AM_API |
| `PARENT_COMMENT_ID` | `VARCHAR(64)` | FK → AM_API_COMMENTS · DEFAULT NULL |
| `ENTRY_POINT` | `VARCHAR(20)` |  |
| `CATEGORY` | `VARCHAR(20)` | DEFAULT 'general' |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: CASCADE)
- `PARENT_COMMENT_ID` → [`AM_API_COMMENTS`](#am_api_comments) `COMMENT_ID`

**Referenced by**

- [`AM_API_COMMENTS`](#am_api_comments) via `PARENT_COMMENT_ID`

## AM_API_DEFAULT_VERSION

*APIM DB (WSO2AM_DB)* · PK: `DEFAULT_VERSION_ID`

| Column | Type | Notes |
|---|---|---|
| `DEFAULT_VERSION_ID` | `INT` | PK · AUTO_INCREMENT |
| `API_NAME` | `VARCHAR(256)` | NOT NULL |
| `API_PROVIDER` | `VARCHAR(256)` | NOT NULL |
| `DEFAULT_API_VERSION` | `VARCHAR(30)` |  |
| `PUBLISHED_DEFAULT_API_VERSION` | `VARCHAR(30)` |  |
| `ORGANIZATION` | `VARCHAR(100)` |  |

## AM_API_ENDPOINTS

*APIM DB (WSO2AM_DB)* · PK: `API_UUID, ENDPOINT_UUID, REVISION_UUID, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `API_UUID` | `VARCHAR(256)` | PK · FK → AM_API · NOT NULL |
| `ENDPOINT_UUID` | `VARCHAR(100)` | PK · NOT NULL |
| `REVISION_UUID` | `VARCHAR(100)` | PK · NOT NULL DEFAULT 'Current API' |
| `ENDPOINT_NAME` | `VARCHAR(255)` | NOT NULL |
| `KEY_TYPE` | `VARCHAR(100)` |  |
| `ENDPOINT_CONFIG` | `LONGBLOB` | NOT NULL |
| `ORGANIZATION` | `VARCHAR(100)` | PK · NOT NULL |

**Foreign keys**

- `API_UUID` → [`AM_API`](#am_api) `API_UUID` (on delete: CASCADE)

**Related tables (not enforced)**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_API_ENVIRONMENT_KEYS

*APIM DB (WSO2AM_DB)* · PK: `UUID` · Unique: `ENVIRONMENT_ID, API_UUID`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(45)` | PK · NOT NULL |
| `ENVIRONMENT_ID` | `VARCHAR(45)` | NOT NULL |
| `API_UUID` | `VARCHAR(256)` | FK → AM_API · NOT NULL |
| `PROPERTY_CONFIG` | `BLOB` | DEFAULT NULL |

**Foreign keys**

- `API_UUID` → [`AM_API`](#am_api) `API_UUID` (on delete: CASCADE)

## AM_API_EXTERNAL_API_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `API_ID, GATEWAY_ENV_ID`

| Column | Type | Notes |
|---|---|---|
| `API_ID` | `VARCHAR(255)` | PK · FK → AM_API · NOT NULL |
| `GATEWAY_ENV_ID` | `VARCHAR(255)` | PK · FK → AM_GATEWAY_ENVIRONMENT · NOT NULL |
| `REFERENCE_ARTIFACT` | `LONGBLOB` | NOT NULL |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_UUID` (on delete: CASCADE)
- `GATEWAY_ENV_ID` → [`AM_GATEWAY_ENVIRONMENT`](#am_gateway_environment) `UUID`

## AM_API_KEY

*APIM DB (WSO2AM_DB)* · PK: `API_KEY_UUID`

| Column | Type | Notes |
|---|---|---|
| `API_KEY_UUID` | `VARCHAR(64)` | PK · PRIMARY KEY |
| `NAME` | `VARCHAR(512)` | NOT NULL |
| `API_KEY_HASH` | `VARCHAR(512)` | NOT NULL UNIQUE |
| `KEY_TYPE` | `VARCHAR(100)` |  |
| `API_KEY_PROPERTIES` | `BLOB` | DEFAULT NULL |
| `AUTHZ_USER` | `VARCHAR(512)` |  |
| `TIME_CREATED` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `VALIDITY_PERIOD` | `BIGINT` |  |
| `LAST_USED` | `TIMESTAMP` | NULL DEFAULT NULL |
| `STATUS` | `VARCHAR(100)` | DEFAULT 'ACTIVE' NOT NULL |

**Referenced by**

- [`AM_API_KEY_API_MAPPING`](#am_api_key_api_mapping) via `API_KEY_UUID`
- [`AM_API_KEY_APPLICATION_MAPPING`](#am_api_key_application_mapping) via `API_KEY_UUID`

## AM_API_KEY_API_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `API_KEY_UUID, API_UUID`

| Column | Type | Notes |
|---|---|---|
| `API_KEY_UUID` | `VARCHAR(64)` | PK · FK → AM_API_KEY |
| `API_UUID` | `VARCHAR(64)` | PK · FK → AM_API |

**Foreign keys**

- `API_KEY_UUID` → [`AM_API_KEY`](#am_api_key) `API_KEY_UUID`
- `API_UUID` → [`AM_API`](#am_api) `API_UUID`

## AM_API_KEY_APPLICATION_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `API_KEY_UUID, APPLICATION_UUID`

| Column | Type | Notes |
|---|---|---|
| `API_KEY_UUID` | `VARCHAR(64)` | PK · FK → AM_API_KEY |
| `APPLICATION_UUID` | `VARCHAR(64)` | PK · FK → AM_APPLICATION |

**Foreign keys**

- `API_KEY_UUID` → [`AM_API_KEY`](#am_api_key) `API_KEY_UUID`
- `APPLICATION_UUID` → [`AM_APPLICATION`](#am_application) `UUID`

## AM_API_LABEL_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `API_UUID, LABEL_UUID`

| Column | Type | Notes |
|---|---|---|
| `API_UUID` | `VARCHAR(256)` | PK · FK → AM_API · NOT NULL |
| `LABEL_UUID` | `VARCHAR(50)` | PK · NOT NULL |

**Foreign keys**

- `API_UUID` → [`AM_API`](#am_api) `API_UUID` (on delete: CASCADE)

**Related tables (not enforced)**

- `LABEL_UUID` → [`AM_LABEL`](#am_label)

## AM_API_LC_EVENT

*APIM DB (WSO2AM_DB)* · PK: `EVENT_ID`

| Column | Type | Notes |
|---|---|---|
| `EVENT_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `API_ID` | `INTEGER` | FK → AM_API · NOT NULL |
| `PREVIOUS_STATE` | `VARCHAR(50)` |  |
| `NEW_STATE` | `VARCHAR(50)` | NOT NULL |
| `USER_ID` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `EVENT_DATE` | `TIMESTAMP` | NOT NULL |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: CASCADE)

## AM_API_LC_PUBLISH_EVENTS

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER(11)` | PK · NOT NULL AUTO_INCREMENT |
| `TENANT_DOMAIN` | `VARCHAR(500)` | NOT NULL |
| `API_ID` | `VARCHAR(500)` | NOT NULL |
| `EVENT_TIME` | `TIMESTAMP` | NOT NULL |

**Related tables (not enforced)**

- `API_ID` → [`AM_API`](#am_api)

## AM_API_METADATA

*APIM DB (WSO2AM_DB)* · PK: `API_UUID, REVISION_UUID, METADATA_KEY`

| Column | Type | Notes |
|---|---|---|
| `API_UUID` | `VARCHAR(256)` | PK · FK → AM_API · NOT NULL |
| `REVISION_UUID` | `VARCHAR(255)` | PK · NOT NULL DEFAULT 'Current API' |
| `METADATA_KEY` | `VARCHAR(256)` | PK · NOT NULL |
| `METADATA_VALUE` | `VARCHAR(1024)` | NOT NULL |

**Foreign keys**

- `API_UUID` → [`AM_API`](#am_api) `API_UUID`

**Related tables (not enforced)**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_API_OPERATION_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `MAPPING_ID`

| Column | Type | Notes |
|---|---|---|
| `MAPPING_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `URL_MAPPING_ID` | `INTEGER` | FK → AM_API_URL_MAPPING · NOT NULL |
| `REF_URL_MAPPING_ID` | `INTEGER` | FK → AM_API_URL_MAPPING · NOT NULL |

**Foreign keys**

- `URL_MAPPING_ID` → [`AM_API_URL_MAPPING`](#am_api_url_mapping) `URL_MAPPING_ID`
- `REF_URL_MAPPING_ID` → [`AM_API_URL_MAPPING`](#am_api_url_mapping) `URL_MAPPING_ID`

## AM_API_OPERATION_POLICY

*APIM DB (WSO2AM_DB)* · PK: `API_SPECIFIC_POLICY_ID`

| Column | Type | Notes |
|---|---|---|
| `API_SPECIFIC_POLICY_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `POLICY_UUID` | `VARCHAR(45)` | FK → AM_OPERATION_POLICY · NOT NULL |
| `API_UUID` | `VARCHAR(45)` | NOT NULL |
| `REVISION_UUID` | `VARCHAR(45)` |  |
| `CLONED_POLICY_UUID` | `VARCHAR(45)` |  |

**Foreign keys**

- `POLICY_UUID` → [`AM_OPERATION_POLICY`](#am_operation_policy) `POLICY_UUID` (on delete: CASCADE)

**Related tables (not enforced)**

- `API_UUID` → [`AM_API`](#am_api)
- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_API_OPERATION_POLICY_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `OPERATION_POLICY_MAPPING_ID`

| Column | Type | Notes |
|---|---|---|
| `OPERATION_POLICY_MAPPING_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `URL_MAPPING_ID` | `INTEGER` | FK → AM_API_URL_MAPPING · NOT NULL |
| `POLICY_UUID` | `VARCHAR(45)` | FK → AM_OPERATION_POLICY · NOT NULL |
| `POLICY_ORDER` | `INTEGER` | NOT NULL |
| `DIRECTION` | `VARCHAR(10)` | NOT NULL |
| `PARAMETERS` | `LONGBLOB` | NOT NULL |

**Foreign keys**

- `URL_MAPPING_ID` → [`AM_API_URL_MAPPING`](#am_api_url_mapping) `URL_MAPPING_ID` (on delete: CASCADE)
- `POLICY_UUID` → [`AM_OPERATION_POLICY`](#am_operation_policy) `POLICY_UUID` (on delete: CASCADE)

## AM_API_POLICY_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `API_POLICY_MAPPING_ID`

| Column | Type | Notes |
|---|---|---|
| `API_POLICY_MAPPING_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `API_UUID` | `VARCHAR(256)` | FK → AM_API · NOT NULL |
| `REVISION_UUID` | `VARCHAR(45)` |  |
| `POLICY_UUID` | `VARCHAR(45)` | FK → AM_OPERATION_POLICY · NOT NULL |
| `POLICY_ORDER` | `INTEGER` | NOT NULL |
| `DIRECTION` | `VARCHAR(10)` | NOT NULL |
| `PARAMETERS` | `LONGBLOB` | NOT NULL |

**Foreign keys**

- `API_UUID` → [`AM_API`](#am_api) `API_UUID` (on delete: CASCADE)
- `POLICY_UUID` → [`AM_OPERATION_POLICY`](#am_operation_policy) `POLICY_UUID` (on delete: CASCADE)

**Related tables (not enforced)**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_API_PRIMARY_EP_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `MAPPING_ID`

| Column | Type | Notes |
|---|---|---|
| `MAPPING_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `API_UUID` | `VARCHAR(256)` | FK → AM_API · NOT NULL |
| `ENDPOINT_UUID` | `VARCHAR(256)` | NOT NULL |
| `REVISION_UUID` | `VARCHAR(100)` | NOT NULL DEFAULT 'Current API' |

**Foreign keys**

- `API_UUID` → [`AM_API`](#am_api) `API_UUID` (on delete: CASCADE)

**Related tables (not enforced)**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_API_PRODUCT_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `API_PRODUCT_MAPPING_ID`

| Column | Type | Notes |
|---|---|---|
| `API_PRODUCT_MAPPING_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `API_ID` | `INTEGER` | FK → AM_API |
| `URL_MAPPING_ID` | `INTEGER` | FK → AM_API_URL_MAPPING |
| `REVISION_UUID` | `VARCHAR(255)` |  |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: CASCADE)
- `URL_MAPPING_ID` → [`AM_API_URL_MAPPING`](#am_api_url_mapping) `URL_MAPPING_ID` (on delete: CASCADE)

**Related tables (not enforced)**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_API_RATINGS

*APIM DB (WSO2AM_DB)* · PK: `RATING_ID`

| Column | Type | Notes |
|---|---|---|
| `RATING_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `API_ID` | `INTEGER` | FK → AM_API |
| `RATING` | `INTEGER` |  |
| `SUBSCRIBER_ID` | `INTEGER` | FK → AM_SUBSCRIBER |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: CASCADE)
- `SUBSCRIBER_ID` → [`AM_SUBSCRIBER`](#am_subscriber) `SUBSCRIBER_ID` (on delete: RESTRICT)

## AM_API_RESOURCE_SCOPE_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `SCOPE_NAME, URL_MAPPING_ID`

| Column | Type | Notes |
|---|---|---|
| `SCOPE_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `URL_MAPPING_ID` | `INTEGER` | PK · FK → AM_API_URL_MAPPING · NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |

**Foreign keys**

- `URL_MAPPING_ID` → [`AM_API_URL_MAPPING`](#am_api_url_mapping) `URL_MAPPING_ID` (on delete: CASCADE)

## AM_API_REVISION_METADATA

*APIM DB (WSO2AM_DB)* · PK: `—` · Unique: `API_UUID, REVISION_UUID`

| Column | Type | Notes |
|---|---|---|
| `API_UUID` | `VARCHAR(64)` |  |
| `REVISION_UUID` | `VARCHAR(255)` | FK → AM_REVISION |
| `API_TIER` | `VARCHAR(128)` |  |

**Foreign keys**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision) `REVISION_UUID` (on delete: CASCADE)

**Related tables (not enforced)**

- `API_UUID` → [`AM_API`](#am_api)

## AM_API_SEQUENCE_BACKEND

*APIM DB (WSO2AM_DB)* · PK: `ID, API_UUID, REVISION_UUID, TYPE`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(60)` | PK · NOT NULL |
| `API_UUID` | `VARCHAR(256)` | PK · FK → AM_API · NOT NULL |
| `REVISION_UUID` | `VARCHAR(256)` | PK · DEFAULT '0' |
| `SEQUENCE` | `LONGBLOB` | NOT NULL |
| `NAME` | `VARCHAR(256)` | NOT NULL |
| `TYPE` | `VARCHAR(120)` | PK · NOT NULL |

**Foreign keys**

- `API_UUID` → [`AM_API`](#am_api) `API_UUID` (on delete: CASCADE)

**Related tables (not enforced)**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_API_SERVICE_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `API_ID, SERVICE_KEY`

| Column | Type | Notes |
|---|---|---|
| `API_ID` | `INTEGER` | PK · FK → AM_API · NOT NULL |
| `SERVICE_KEY` | `VARCHAR(256)` | PK · NOT NULL |
| `MD5` | `VARCHAR(512)` |  |
| `TENANT_ID` | `INTEGER` | NOT NULL |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: CASCADE)

## AM_API_THROTTLE_POLICY

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID` · Unique: `NAME, TENANT_ID`; `UUID`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `INT(11)` | PK · NOT NULL AUTO_INCREMENT |
| `NAME` | `VARCHAR(512)` | NOT NULL |
| `DISPLAY_NAME` | `VARCHAR(512)` | NULL DEFAULT NULL |
| `TENANT_ID` | `INT(11)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR (1024)` |  |
| `DEFAULT_QUOTA_TYPE` | `VARCHAR(25)` | NOT NULL |
| `DEFAULT_QUOTA` | `INTEGER` | NOT NULL |
| `DEFAULT_QUOTA_UNIT` | `VARCHAR(10)` | NULL |
| `DEFAULT_UNIT_TIME` | `INTEGER` | NOT NULL |
| `DEFAULT_TIME_UNIT` | `VARCHAR(25)` | NOT NULL |
| `APPLICABLE_LEVEL` | `VARCHAR(25)` | NOT NULL |
| `IS_DEPLOYED` | `TINYINT(1)` | NOT NULL DEFAULT 0 |
| `UUID` | `VARCHAR(256)` |  |

**Referenced by**

- [`AM_CONDITION_GROUP`](#am_condition_group) via `POLICY_ID`

## AM_API_URL_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `URL_MAPPING_ID`

| Column | Type | Notes |
|---|---|---|
| `URL_MAPPING_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `API_ID` | `INTEGER` | NOT NULL |
| `HTTP_METHOD` | `VARCHAR(20)` | NULL |
| `AUTH_SCHEME` | `VARCHAR(50)` | NULL |
| `URL_PATTERN` | `VARCHAR(512)` | NULL |
| `THROTTLING_TIER` | `VARCHAR(512)` | DEFAULT NULL |
| `MEDIATION_SCRIPT` | `BLOB` |  |
| `REVISION_UUID` | `VARCHAR(255)` |  |
| `LOG_LEVEL` | `VARCHAR(255)` | DEFAULT 'OFF' |
| `DESCRIPTION` | `BLOB` |  |
| `SCHEMA_DEFINITION` | `BLOB` |  |

**Referenced by**

- [`AM_API_OPERATION_MAPPING`](#am_api_operation_mapping) via `URL_MAPPING_ID`
- [`AM_API_OPERATION_MAPPING`](#am_api_operation_mapping) via `REF_URL_MAPPING_ID`
- [`AM_API_OPERATION_POLICY_MAPPING`](#am_api_operation_policy_mapping) via `URL_MAPPING_ID`
- [`AM_API_PRODUCT_MAPPING`](#am_api_product_mapping) via `URL_MAPPING_ID`
- [`AM_API_RESOURCE_SCOPE_MAPPING`](#am_api_resource_scope_mapping) via `URL_MAPPING_ID`
- [`AM_BACKEND_OPERATION_MAPPING`](#am_backend_operation_mapping) via `URL_MAPPING_ID`

**Related tables (not enforced)**

- `API_ID` → [`AM_API`](#am_api)
- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_APPLICATION

*APIM DB (WSO2AM_DB)* · PK: `APPLICATION_ID` · Unique: `NAME, SUBSCRIBER_ID, ORGANIZATION`; `UUID`

| Column | Type | Notes |
|---|---|---|
| `APPLICATION_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `NAME` | `VARCHAR(100)` |  |
| `SUBSCRIBER_ID` | `INTEGER` | FK → AM_SUBSCRIBER |
| `APPLICATION_TIER` | `VARCHAR(50)` | DEFAULT 'Unlimited' |
| `CALLBACK_URL` | `VARCHAR(512)` |  |
| `DESCRIPTION` | `VARCHAR(512)` |  |
| `APPLICATION_STATUS` | `VARCHAR(50)` | DEFAULT 'APPROVED' |
| `GROUP_ID` | `VARCHAR(100)` |  |
| `CREATED_BY` | `VARCHAR(100)` |  |
| `CREATED_TIME` | `TIMESTAMP` |  |
| `UPDATED_BY` | `VARCHAR(100)` |  |
| `UPDATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `UUID` | `VARCHAR(256)` |  |
| `TOKEN_TYPE` | `VARCHAR(10)` |  |
| `ORGANIZATION` | `VARCHAR(100)` |  |
| `SHARED_ORGANIZATION` | `VARCHAR(100)` |  |

**Foreign keys**

- `SUBSCRIBER_ID` → [`AM_SUBSCRIBER`](#am_subscriber) `SUBSCRIBER_ID` (on delete: RESTRICT)

**Referenced by**

- [`AM_API_KEY_APPLICATION_MAPPING`](#am_api_key_application_mapping) via `APPLICATION_UUID`
- [`AM_APPLICATION_ATTRIBUTES`](#am_application_attributes) via `APPLICATION_ID`
- [`AM_APPLICATION_GROUP_MAPPING`](#am_application_group_mapping) via `APPLICATION_ID`
- [`AM_APPLICATION_KEY_MAPPING`](#am_application_key_mapping) via `APPLICATION_ID`
- [`AM_APPLICATION_REGISTRATION`](#am_application_registration) via `APP_ID`
- [`AM_SUBSCRIPTION`](#am_subscription) via `APPLICATION_ID`

## AM_APPLICATION_ATTRIBUTES

*APIM DB (WSO2AM_DB)* · PK: `APPLICATION_ID, NAME`

| Column | Type | Notes |
|---|---|---|
| `APPLICATION_ID` | `INT(11)` | PK · FK → AM_APPLICATION · NOT NULL |
| `NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `APP_ATTRIBUTE` | `VARCHAR(1024)` | NOT NULL |
| `TENANT_ID` | `INT(11)` | NOT NULL |

**Foreign keys**

- `APPLICATION_ID` → [`AM_APPLICATION`](#am_application) `APPLICATION_ID` (on delete: CASCADE)

## AM_APPLICATION_GROUP_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `APPLICATION_ID, GROUP_ID, TENANT`

| Column | Type | Notes |
|---|---|---|
| `APPLICATION_ID` | `INTEGER` | PK · FK → AM_APPLICATION · NOT NULL |
| `GROUP_ID` | `VARCHAR(512)` | PK · NOT NULL |
| `TENANT` | `VARCHAR(255)` | PK |

**Foreign keys**

- `APPLICATION_ID` → [`AM_APPLICATION`](#am_application) `APPLICATION_ID` (on delete: CASCADE)

## AM_APPLICATION_KEY_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `APPLICATION_ID, KEY_TYPE, KEY_MANAGER`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(100)` |  |
| `APPLICATION_ID` | `INTEGER` | PK · FK → AM_APPLICATION |
| `CONSUMER_KEY` | `VARCHAR(255)` |  |
| `KEY_TYPE` | `VARCHAR(512)` | PK · NOT NULL |
| `STATE` | `VARCHAR(30)` | NOT NULL |
| `CREATE_MODE` | `VARCHAR(30)` | DEFAULT 'CREATED' |
| `KEY_MANAGER` | `VARCHAR(100)` | PK |
| `APP_INFO` | `BLOB` |  |

**Foreign keys**

- `APPLICATION_ID` → [`AM_APPLICATION`](#am_application) `APPLICATION_ID` (on delete: CASCADE)

**Related tables (not enforced)**

- `CONSUMER_KEY` → [`IDN_OAUTH_CONSUMER_APPS`](idn.md#idn_oauth_consumer_apps)
- `KEY_MANAGER` → [`AM_KEY_MANAGER`](#am_key_manager)

## AM_APPLICATION_REGISTRATION

*APIM DB (WSO2AM_DB)* · PK: `REG_ID` · Unique: `SUBSCRIBER_ID, APP_ID, TOKEN_TYPE, KEY_MANAGER`

| Column | Type | Notes |
|---|---|---|
| `REG_ID` | `INT` | PK · AUTO_INCREMENT |
| `SUBSCRIBER_ID` | `INT` | FK → AM_SUBSCRIBER |
| `WF_REF` | `VARCHAR(255)` | NOT NULL |
| `APP_ID` | `INT` | FK → AM_APPLICATION |
| `TOKEN_TYPE` | `VARCHAR(30)` |  |
| `TOKEN_SCOPE` | `VARCHAR(1500)` | DEFAULT 'default' |
| `INPUTS` | `LONGBLOB` |  |
| `ALLOWED_DOMAINS` | `VARCHAR(256)` |  |
| `VALIDITY_PERIOD` | `BIGINT` |  |
| `KEY_MANAGER` | `VARCHAR(255)` | NOT NULL |

**Foreign keys**

- `SUBSCRIBER_ID` → [`AM_SUBSCRIBER`](#am_subscriber) `SUBSCRIBER_ID` (on delete: RESTRICT)
- `APP_ID` → [`AM_APPLICATION`](#am_application) `APPLICATION_ID` (on delete: CASCADE)

**Related tables (not enforced)**

- `KEY_MANAGER` → [`AM_KEY_MANAGER`](#am_key_manager)

## AM_APP_KEY_DOMAIN_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `CONSUMER_KEY, AUTHZ_DOMAIN`

| Column | Type | Notes |
|---|---|---|
| `CONSUMER_KEY` | `VARCHAR(255)` | PK |
| `AUTHZ_DOMAIN` | `VARCHAR(255)` | PK · DEFAULT 'ALL' |

**Related tables (not enforced)**

- `CONSUMER_KEY` → [`IDN_OAUTH_CONSUMER_APPS`](idn.md#idn_oauth_consumer_apps)

## AM_APP_REVOKED_EVENT

*APIM DB (WSO2AM_DB)* · PK: `CONSUMER_KEY, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `CONSUMER_KEY` | `VARCHAR(255)` | PK · NOT NULL |
| `TIME_REVOKED` | `TIMESTAMP` | NOT NULL |
| `ORGANIZATION` | `VARCHAR(100)` | PK |

**Related tables (not enforced)**

- `CONSUMER_KEY` → [`IDN_OAUTH_CONSUMER_APPS`](idn.md#idn_oauth_consumer_apps)

## AM_ARTIFACT

*APIM DB (WSO2AM_DB)* · PK: `UUID`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(45)` | PK |
| `ARTIFACT` | `LONGBLOB` | NOT NULL |
| `TYPE` | `VARCHAR(25)` | NOT NULL |

## AM_BACKEND

*APIM DB (WSO2AM_DB)* · PK: `BACKEND_ID` · Unique: `REFERENCE_API_UUID, REFERENCE_API_REVISION_UUID, BACKEND_NAME`

| Column | Type | Notes |
|---|---|---|
| `BACKEND_ID` | `VARCHAR(40)` | PK · NOT NULL |
| `BACKEND_NAME` | `VARCHAR(256)` | NOT NULL |
| `ENDPOINT_CONFIG` | `BLOB` |  |
| `DEFINITION` | `LONGBLOB` |  |
| `REFERENCE_API_UUID` | `VARCHAR(256)` | FK → AM_API · NOT NULL |
| `REFERENCE_API_REVISION_UUID` | `VARCHAR(256)` | NOT NULL DEFAULT 'Current API' |
| `ORGANIZATION` | `VARCHAR(100)` | NOT NULL |

**Foreign keys**

- `REFERENCE_API_UUID` → [`AM_API`](#am_api) `API_UUID`

**Referenced by**

- [`AM_BACKEND_OPERATION_MAPPING`](#am_backend_operation_mapping) via `BACKEND_ID`

## AM_BACKEND_OPERATION_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `MAPPING_ID`

| Column | Type | Notes |
|---|---|---|
| `MAPPING_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `URL_MAPPING_ID` | `INTEGER` | FK → AM_API_URL_MAPPING · NOT NULL |
| `BACKEND_ID` | `VARCHAR(40)` | FK → AM_BACKEND · NOT NULL |
| `TARGET` | `VARCHAR(256)` | NOT NULL |
| `VERB` | `VARCHAR(10)` | NOT NULL |

**Foreign keys**

- `URL_MAPPING_ID` → [`AM_API_URL_MAPPING`](#am_api_url_mapping) `URL_MAPPING_ID`
- `BACKEND_ID` → [`AM_BACKEND`](#am_backend) `BACKEND_ID`

## AM_BLOCK_CONDITIONS

*APIM DB (WSO2AM_DB)* · PK: `CONDITION_ID` · Unique: `UUID`

| Column | Type | Notes |
|---|---|---|
| `CONDITION_ID` | `INT(11)` | PK · NOT NULL AUTO_INCREMENT |
| `TYPE` | `VARCHAR(45)` | DEFAULT NULL |
| `BLOCK_CONDITION` | `VARCHAR(512)` | DEFAULT NULL |
| `ENABLED` | `VARCHAR(45)` | DEFAULT NULL |
| `DOMAIN` | `VARCHAR(45)` | DEFAULT NULL |
| `UUID` | `VARCHAR(256)` |  |

## AM_CERTIFICATE_METADATA

*APIM DB (WSO2AM_DB)* · PK: `ALIAS`

| Column | Type | Notes |
|---|---|---|
| `TENANT_ID` | `INT(11)` | NOT NULL |
| `ALIAS` | `VARCHAR(255)` | PK · NOT NULL |
| `END_POINT` | `VARCHAR(255)` | NOT NULL |
| `CERTIFICATE` | `BLOB` | DEFAULT NULL |

## AM_COMMON_OPERATION_POLICY

*APIM DB (WSO2AM_DB)* · PK: `COMMON_POLICY_ID`

| Column | Type | Notes |
|---|---|---|
| `COMMON_POLICY_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `POLICY_UUID` | `VARCHAR(45)` | FK → AM_OPERATION_POLICY · NOT NULL |

**Foreign keys**

- `POLICY_UUID` → [`AM_OPERATION_POLICY`](#am_operation_policy) `POLICY_UUID` (on delete: CASCADE)

## AM_CONDITION_GROUP

*APIM DB (WSO2AM_DB)* · PK: `CONDITION_GROUP_ID`

| Column | Type | Notes |
|---|---|---|
| `CONDITION_GROUP_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `POLICY_ID` | `INTEGER` | FK → AM_API_THROTTLE_POLICY · NOT NULL |
| `QUOTA_TYPE` | `VARCHAR(25)` |  |
| `QUOTA` | `INTEGER` | NOT NULL |
| `QUOTA_UNIT` | `VARCHAR(10)` | NULL DEFAULT NULL |
| `UNIT_TIME` | `INTEGER` | NOT NULL |
| `TIME_UNIT` | `VARCHAR(25)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR (1024)` | NULL DEFAULT NULL |

**Foreign keys**

- `POLICY_ID` → [`AM_API_THROTTLE_POLICY`](#am_api_throttle_policy) `POLICY_ID` (on delete: CASCADE)

**Referenced by**

- [`AM_HEADER_FIELD_CONDITION`](#am_header_field_condition) via `CONDITION_GROUP_ID`
- [`AM_IP_CONDITION`](#am_ip_condition) via `CONDITION_GROUP_ID`
- [`AM_JWT_CLAIM_CONDITION`](#am_jwt_claim_condition) via `CONDITION_GROUP_ID`
- [`AM_QUERY_PARAMETER_CONDITION`](#am_query_parameter_condition) via `CONDITION_GROUP_ID`

## AM_CORRELATION_CONFIGS

*APIM DB (WSO2AM_DB)* · PK: `COMPONENT_NAME`

| Column | Type | Notes |
|---|---|---|
| `COMPONENT_NAME` | `VARCHAR(45)` | PK · NOT NULL |
| `ENABLED` | `VARCHAR(45)` | NOT NULL |

**Referenced by**

- [`AM_CORRELATION_PROPERTIES`](#am_correlation_properties) via `COMPONENT_NAME`

## AM_CORRELATION_PROPERTIES

*APIM DB (WSO2AM_DB)* · PK: `PROPERTY_NAME, COMPONENT_NAME`

| Column | Type | Notes |
|---|---|---|
| `PROPERTY_NAME` | `VARCHAR(45)` | PK · NOT NULL |
| `COMPONENT_NAME` | `VARCHAR(45)` | PK · FK → AM_CORRELATION_CONFIGS · NOT NULL |
| `PROPERTY_VALUE` | `VARCHAR(1023)` | NOT NULL |

**Foreign keys**

- `COMPONENT_NAME` → [`AM_CORRELATION_CONFIGS`](#am_correlation_configs) `COMPONENT_NAME` (on delete: CASCADE)

## AM_DEPLOYED_REVISION

*APIM DB (WSO2AM_DB)* · PK: `NAME, REVISION_UUID`

| Column | Type | Notes |
|---|---|---|
| `NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `VHOST` | `VARCHAR(255)` | NULL |
| `REVISION_UUID` | `VARCHAR(255)` | PK · FK → AM_REVISION · NOT NULL |
| `DEPLOYED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |

**Foreign keys**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision) `REVISION_UUID` (on delete: CASCADE)

## AM_DEPLOYMENT_REVISION_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `NAME, REVISION_UUID`

| Column | Type | Notes |
|---|---|---|
| `NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `VHOST` | `VARCHAR(255)` | NULL |
| `REVISION_UUID` | `VARCHAR(255)` | PK · FK → AM_REVISION · NOT NULL |
| `REVISION_STATUS` | `VARCHAR(255)` | NULL |
| `DISPLAY_ON_DEVPORTAL` | `BOOLEAN` | DEFAULT 0 |
| `DEPLOYED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |

**Foreign keys**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision) `REVISION_UUID` (on delete: CASCADE)

## AM_DEVPORTAL_API_CONTENT

*APIM DB (WSO2AM_DB)* · PK: `API_UUID, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `API_UUID` | `VARCHAR(256)` | PK |
| `ORGANIZATION` | `VARCHAR(100)` | PK |
| `DRAFTED_ARTIFACT` | `VARCHAR(45)` |  |
| `PUBLISHED_ARTIFACT` | `VARCHAR(45)` |  |

**Related tables (not enforced)**

- `API_UUID` → [`AM_API`](#am_api)

## AM_DEVPORTAL_API_REFERENCE

*APIM DB (WSO2AM_DB)* · PK: `API_UUID, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `API_UUID` | `VARCHAR(256)` | PK |
| `ORGANIZATION` | `VARCHAR(100)` | PK · NOT NULL |
| `REFERENCE_APIID` | `VARCHAR(256)` | NOT NULL |

**Related tables (not enforced)**

- `API_UUID` → [`AM_API`](#am_api)

## AM_DEVPORTAL_ORG_CONTENT

*APIM DB (WSO2AM_DB)* · PK: `ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `ORGANIZATION` | `VARCHAR(100)` | PK |
| `DRAFTED_ARTIFACT` | `VARCHAR(45)` |  |
| `PUBLISHED_ARTIFACT` | `VARCHAR(45)` |  |

## AM_EXTERNAL_STORES

*APIM DB (WSO2AM_DB)* · PK: `APISTORE_ID`

| Column | Type | Notes |
|---|---|---|
| `APISTORE_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `API_ID` | `INTEGER` | FK → AM_API |
| `STORE_ID` | `VARCHAR(255)` | NOT NULL |
| `STORE_DISPLAY_NAME` | `VARCHAR(255)` | NOT NULL |
| `STORE_ENDPOINT` | `VARCHAR(255)` | NOT NULL |
| `STORE_TYPE` | `VARCHAR(255)` | NOT NULL |
| `LAST_UPDATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: RESTRICT)

## AM_GATEWAY_ENVIRONMENT

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `NAME, ORGANIZATION`; `UUID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UUID` | `VARCHAR(45)` | NOT NULL |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `TYPE` | `VARCHAR(255)` | NULL |
| `DISPLAY_NAME` | `VARCHAR(255)` | NULL |
| `DESCRIPTION` | `VARCHAR(1023)` | NULL |
| `PROVIDER` | `VARCHAR(255)` | NOT NULL |
| `GATEWAY_TYPE` | `VARCHAR(255)` | NOT NULL |
| `ENV_MODE` | `VARCHAR(45)` | NOT NULL DEFAULT 'WRITE_ONLY' |
| `SCHEDULED_TIME` | `INTEGER` |  |
| `CONFIGURATION` | `BLOB` | NULL |
| `ORGANIZATION` | `VARCHAR(255)` | NOT NULL |

**Referenced by**

- [`AM_API_EXTERNAL_API_MAPPING`](#am_api_external_api_mapping) via `GATEWAY_ENV_ID`
- [`AM_GATEWAY_PERMISSIONS`](#am_gateway_permissions) via `GATEWAY_UUID`
- [`AM_GATEWAY_TOKEN`](#am_gateway_token) via `GATEWAY_ID`
- [`AM_GW_PLATFORM_EVENT`](#am_gw_platform_event) via `GATEWAY_ID`
- [`AM_GW_VHOST`](#am_gw_vhost) via `GATEWAY_ENV_ID`

## AM_GATEWAY_PERMISSIONS

*APIM DB (WSO2AM_DB)* · PK: `GATEWAY_UUID, ROLE`

| Column | Type | Notes |
|---|---|---|
| `GATEWAY_UUID` | `VARCHAR(45)` | PK · FK → AM_GATEWAY_ENVIRONMENT · NOT NULL |
| `PERMISSIONS_TYPE` | `VARCHAR(50)` | NOT NULL |
| `ROLE` | `VARCHAR(255)` | PK |

**Foreign keys**

- `GATEWAY_UUID` → [`AM_GATEWAY_ENVIRONMENT`](#am_gateway_environment) `UUID` (on delete: CASCADE)

## AM_GATEWAY_POLICY_DEPLOYMENT

*APIM DB (WSO2AM_DB)* · PK: `ORGANIZATION, GATEWAY_LABEL`

| Column | Type | Notes |
|---|---|---|
| `GATEWAY_LABEL` | `VARCHAR(255)` | PK · NOT NULL |
| `GLOBAL_POLICY_MAPPING_UUID` | `VARCHAR(45)` | FK → AM_GATEWAY_POLICY_METADATA · NOT NULL |
| `ORGANIZATION` | `VARCHAR(100)` | PK · NOT NULL |

**Foreign keys**

- `GLOBAL_POLICY_MAPPING_UUID` → [`AM_GATEWAY_POLICY_METADATA`](#am_gateway_policy_metadata) `GLOBAL_POLICY_MAPPING_UUID` (on delete: RESTRICT)

## AM_GATEWAY_POLICY_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `POLICY_TO_FLOW_INFO_MAPPING_ID`

| Column | Type | Notes |
|---|---|---|
| `POLICY_TO_FLOW_INFO_MAPPING_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `GLOBAL_POLICY_MAPPING_UUID` | `VARCHAR(45)` | FK → AM_GATEWAY_POLICY_METADATA · NOT NULL |
| `POLICY_UUID` | `VARCHAR(45)` | FK → AM_OPERATION_POLICY · NOT NULL |
| `POLICY_ORDER` | `INTEGER` | NOT NULL |
| `DIRECTION` | `VARCHAR(10)` | NOT NULL |
| `PARAMETERS` | `VARCHAR(2048)` | NOT NULL |

**Foreign keys**

- `POLICY_UUID` → [`AM_OPERATION_POLICY`](#am_operation_policy) `POLICY_UUID` (on delete: RESTRICT)
- `GLOBAL_POLICY_MAPPING_UUID` → [`AM_GATEWAY_POLICY_METADATA`](#am_gateway_policy_metadata) `GLOBAL_POLICY_MAPPING_UUID` (on delete: CASCADE)

## AM_GATEWAY_POLICY_METADATA

*APIM DB (WSO2AM_DB)* · PK: `GLOBAL_POLICY_MAPPING_UUID`

| Column | Type | Notes |
|---|---|---|
| `GLOBAL_POLICY_MAPPING_UUID` | `VARCHAR(45)` | PK · NOT NULL |
| `DISPLAY_NAME` | `VARCHAR(255)` | NULL |
| `DESCRIPTION` | `VARCHAR(1023)` | NULL |
| `ORGANIZATION` | `VARCHAR(100)` | NOT NULL |

**Referenced by**

- [`AM_GATEWAY_POLICY_DEPLOYMENT`](#am_gateway_policy_deployment) via `GLOBAL_POLICY_MAPPING_UUID`
- [`AM_GATEWAY_POLICY_MAPPING`](#am_gateway_policy_mapping) via `GLOBAL_POLICY_MAPPING_UUID`

## AM_GATEWAY_TOKEN

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `GATEWAY_ID` | `VARCHAR(45)` | FK → AM_GATEWAY_ENVIRONMENT · NOT NULL |
| `TOKEN_HASH` | `VARCHAR(255)` | NOT NULL |
| `STATUS` | `VARCHAR(50)` | NOT NULL DEFAULT 'active' |
| `CREATED_AT` | `TIMESTAMP` | NOT NULL |
| `REVOKED_AT` | `TIMESTAMP` | NULL |

**Foreign keys**

- `GATEWAY_ID` → [`AM_GATEWAY_ENVIRONMENT`](#am_gateway_environment) `UUID` (on delete: CASCADE)

## AM_GRAPHQL_COMPLEXITY

*APIM DB (WSO2AM_DB)* · PK: `UUID`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(256)` | PK |
| `API_ID` | `INTEGER` | FK → AM_API · NOT NULL |
| `TYPE` | `VARCHAR(256)` |  |
| `FIELD` | `VARCHAR(256)` |  |
| `COMPLEXITY_VALUE` | `INTEGER` |  |
| `REVISION_UUID` | `VARCHAR(255)` |  |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: CASCADE)

**Related tables (not enforced)**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_GW_API_ARTIFACTS

*APIM DB (WSO2AM_DB)* · PK: `REVISION_ID, API_ID`

| Column | Type | Notes |
|---|---|---|
| `API_ID` | `VARCHAR(255)` | PK · FK → AM_GW_PUBLISHED_API_DETAILS · NOT NULL |
| `REVISION_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `ARTIFACT` | `MEDIUMBLOB` |  |
| `TIME_STAMP` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP |

**Foreign keys**

- `API_ID` → [`AM_GW_PUBLISHED_API_DETAILS`](#am_gw_published_api_details) `API_ID`

## AM_GW_API_DEPLOYMENTS

*APIM DB (WSO2AM_DB)* · PK: `REVISION_ID, API_ID, LABEL`

| Column | Type | Notes |
|---|---|---|
| `API_ID` | `VARCHAR(255)` | PK · FK → AM_GW_PUBLISHED_API_DETAILS · NOT NULL |
| `REVISION_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `LABEL` | `VARCHAR(255)` | PK · NOT NULL |
| `VHOST` | `VARCHAR(255)` | NULL |

**Foreign keys**

- `API_ID` → [`AM_GW_PUBLISHED_API_DETAILS`](#am_gw_published_api_details) `API_ID` (on delete: CASCADE)

## AM_GW_INSTANCES

*APIM DB (WSO2AM_DB)* · PK: `GATEWAY_ID` · Unique: `GATEWAY_UUID, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `GATEWAY_ID` | `INT` | PK · NOT NULL AUTO_INCREMENT |
| `GATEWAY_UUID` | `VARCHAR(255)` | NOT NULL |
| `ORGANIZATION` | `VARCHAR(128)` | NOT NULL |
| `LAST_UPDATED` | `TIMESTAMP` | NOT NULL |
| `GW_PROPERTIES` | `BLOB` |  |

**Referenced by**

- [`AM_GW_INSTANCE_ENV_MAPPING`](#am_gw_instance_env_mapping) via `GATEWAY_ID`
- [`AM_GW_REVISION_DEPLOYMENT`](#am_gw_revision_deployment) via `GATEWAY_ID`

## AM_GW_INSTANCE_ENV_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `GATEWAY_ID, ENV_LABEL`

| Column | Type | Notes |
|---|---|---|
| `GATEWAY_ID` | `INT` | PK · FK → AM_GW_INSTANCES · NOT NULL |
| `ENV_LABEL` | `VARCHAR(255)` | PK · NOT NULL |

**Foreign keys**

- `GATEWAY_ID` → [`AM_GW_INSTANCES`](#am_gw_instances) `GATEWAY_ID` (on delete: CASCADE)

## AM_GW_PLATFORM_API_ARTIFACTS

*APIM DB (WSO2AM_DB)* · PK: `DEPLOYMENT_ID` · Unique: `GATEWAY_ENV_UUID, API_ID, REVISION_ID`

| Column | Type | Notes |
|---|---|---|
| `API_ID` | `VARCHAR(255)` | FK → AM_GW_PUBLISHED_API_DETAILS · NOT NULL |
| `REVISION_ID` | `VARCHAR(255)` | NOT NULL |
| `GATEWAY_ENV_UUID` | `VARCHAR(255)` | NOT NULL |
| `DEPLOYMENT_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `ARTIFACT` | `MEDIUMBLOB` |  |
| `TIME_STAMP` | `TIMESTAMP` | NOT NULL |

**Foreign keys**

- `API_ID` → [`AM_GW_PUBLISHED_API_DETAILS`](#am_gw_published_api_details) `API_ID`

## AM_GW_PLATFORM_EVENT

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(36)` | PK · NOT NULL |
| `GATEWAY_ID` | `VARCHAR(45)` | FK → AM_GATEWAY_ENVIRONMENT · NOT NULL |
| `EVENT_TYPE` | `VARCHAR(32)` | NOT NULL |
| `PAYLOAD` | `MEDIUMBLOB` | NOT NULL |
| `CREATED_AT` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `DELIVERED_AT` | `TIMESTAMP` | NULL |
| `CLAIMED_AT` | `TIMESTAMP` | NULL |
| `CLAIMED_BY` | `VARCHAR(36)` | NULL |

**Foreign keys**

- `GATEWAY_ID` → [`AM_GATEWAY_ENVIRONMENT`](#am_gateway_environment) `UUID` (on delete: CASCADE)

## AM_GW_PUBLISHED_API_DETAILS

*APIM DB (WSO2AM_DB)* · PK: `API_ID`

| Column | Type | Notes |
|---|---|---|
| `API_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `TENANT_DOMAIN` | `VARCHAR(255)` |  |
| `API_PROVIDER` | `VARCHAR(255)` |  |
| `API_NAME` | `VARCHAR(255)` |  |
| `API_VERSION` | `VARCHAR(255)` |  |
| `API_TYPE` | `VARCHAR(50)` |  |

**Referenced by**

- [`AM_GW_API_ARTIFACTS`](#am_gw_api_artifacts) via `API_ID`
- [`AM_GW_API_DEPLOYMENTS`](#am_gw_api_deployments) via `API_ID`
- [`AM_GW_PLATFORM_API_ARTIFACTS`](#am_gw_platform_api_artifacts) via `API_ID`

**Related tables (not enforced)**

- `API_ID` → [`AM_API`](#am_api)

## AM_GW_REVISION_DEPLOYMENT

*APIM DB (WSO2AM_DB)* · PK: `GATEWAY_ID, API_ID`

| Column | Type | Notes |
|---|---|---|
| `GATEWAY_ID` | `INT` | PK · FK → AM_GW_INSTANCES · NOT NULL |
| `API_ID` | `VARCHAR(256)` | PK · FK → AM_API · NOT NULL |
| `ORGANIZATION` | `VARCHAR(128)` | NOT NULL |
| `STATUS` | `VARCHAR(255)` | NOT NULL |
| `ACTION` | `VARCHAR(255)` | NOT NULL |
| `REVISION_UUID` | `VARCHAR(255)` |  |
| `LAST_UPDATED` | `BIGINT` | NOT NULL |

**Foreign keys**

- `GATEWAY_ID` → [`AM_GW_INSTANCES`](#am_gw_instances) `GATEWAY_ID` (on delete: CASCADE)
- `API_ID` → [`AM_API`](#am_api) `API_UUID` (on delete: CASCADE)

**Related tables (not enforced)**

- `REVISION_UUID` → [`AM_REVISION`](#am_revision)

## AM_GW_VHOST

*APIM DB (WSO2AM_DB)* · PK: `GATEWAY_ENV_ID, HOST`

| Column | Type | Notes |
|---|---|---|
| `GATEWAY_ENV_ID` | `INTEGER` | PK · FK → AM_GATEWAY_ENVIRONMENT · NOT NULL |
| `HOST` | `VARCHAR(255)` | PK · NOT NULL |
| `HTTP_CONTEXT` | `VARCHAR(255)` | NULL |
| `HTTP_PORT` | `VARCHAR(5)` | NOT NULL |
| `HTTPS_PORT` | `VARCHAR(5)` | NOT NULL |
| `WS_PORT` | `VARCHAR(5)` | NOT NULL |
| `WSS_PORT` | `VARCHAR(5)` | NOT NULL |

**Foreign keys**

- `GATEWAY_ENV_ID` → [`AM_GATEWAY_ENVIRONMENT`](#am_gateway_environment) `ID` (on delete: CASCADE)

## AM_HEADER_FIELD_CONDITION

*APIM DB (WSO2AM_DB)* · PK: `HEADER_FIELD_ID`

| Column | Type | Notes |
|---|---|---|
| `HEADER_FIELD_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `CONDITION_GROUP_ID` | `INTEGER` | FK → AM_CONDITION_GROUP · NOT NULL |
| `HEADER_FIELD_NAME` | `VARCHAR(255)` | DEFAULT NULL |
| `HEADER_FIELD_VALUE` | `VARCHAR(255)` | DEFAULT NULL |
| `IS_HEADER_FIELD_MAPPING` | `BOOLEAN` | DEFAULT 1 |

**Foreign keys**

- `CONDITION_GROUP_ID` → [`AM_CONDITION_GROUP`](#am_condition_group) `CONDITION_GROUP_ID` (on delete: CASCADE)

## AM_IP_CONDITION

*APIM DB (WSO2AM_DB)* · PK: `AM_IP_CONDITION_ID`

| Column | Type | Notes |
|---|---|---|
| `AM_IP_CONDITION_ID` | `INT` | PK · NOT NULL AUTO_INCREMENT |
| `STARTING_IP` | `VARCHAR(45)` | NULL |
| `ENDING_IP` | `VARCHAR(45)` | NULL |
| `SPECIFIC_IP` | `VARCHAR(45)` | NULL |
| `WITHIN_IP_RANGE` | `BOOLEAN` | DEFAULT 1 |
| `CONDITION_GROUP_ID` | `INT` | FK → AM_CONDITION_GROUP · NULL |

**Foreign keys**

- `CONDITION_GROUP_ID` → [`AM_CONDITION_GROUP`](#am_condition_group) `CONDITION_GROUP_ID` (on delete: CASCADE)

## AM_JWT_CLAIM_CONDITION

*APIM DB (WSO2AM_DB)* · PK: `JWT_CLAIM_ID`

| Column | Type | Notes |
|---|---|---|
| `JWT_CLAIM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `CONDITION_GROUP_ID` | `INTEGER` | FK → AM_CONDITION_GROUP · NOT NULL |
| `CLAIM_URI` | `VARCHAR(512)` | DEFAULT NULL |
| `CLAIM_ATTRIB` | `VARCHAR(1024)` | DEFAULT NULL |
| `IS_CLAIM_MAPPING` | `BOOLEAN` | DEFAULT 1 |

**Foreign keys**

- `CONDITION_GROUP_ID` → [`AM_CONDITION_GROUP`](#am_condition_group) `CONDITION_GROUP_ID` (on delete: CASCADE)

## AM_KEY_MANAGER

*APIM DB (WSO2AM_DB)* · PK: `UUID` · Unique: `NAME, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(50)` | PK · NOT NULL |
| `NAME` | `VARCHAR(100)` | NULL |
| `DISPLAY_NAME` | `VARCHAR(100)` | NULL |
| `DESCRIPTION` | `VARCHAR(256)` | NULL |
| `TYPE` | `VARCHAR(45)` | NULL |
| `CONFIGURATION` | `BLOB` | NULL |
| `ENABLED` | `BOOLEAN` | DEFAULT 1 |
| `ORGANIZATION` | `VARCHAR(100)` | NULL |
| `TOKEN_TYPE` | `VARCHAR(45)` | NULL |
| `EXTERNAL_REFERENCE_ID` | `VARCHAR(100)` | NULL |

**Referenced by**

- [`AM_KEY_MANAGER_ALLOWED_ORGS`](#am_key_manager_allowed_orgs) via `KEY_MANAGER_UUID`
- [`AM_KEY_MANAGER_PERMISSIONS`](#am_key_manager_permissions) via `KEY_MANAGER_UUID`

## AM_KEY_MANAGER_ALLOWED_ORGS

*APIM DB (WSO2AM_DB)* · PK: `KEY_MANAGER_UUID, ALLOWED_ORGANIZATIONS`

| Column | Type | Notes |
|---|---|---|
| `KEY_MANAGER_UUID` | `VARCHAR(50)` | PK · FK → AM_KEY_MANAGER · NOT NULL |
| `ALLOWED_ORGANIZATIONS` | `VARCHAR(50)` | PK · NOT NULL |

**Foreign keys**

- `KEY_MANAGER_UUID` → [`AM_KEY_MANAGER`](#am_key_manager) `UUID` (on delete: CASCADE)

## AM_KEY_MANAGER_PERMISSIONS

*APIM DB (WSO2AM_DB)* · PK: `KEY_MANAGER_UUID, ROLE`

| Column | Type | Notes |
|---|---|---|
| `KEY_MANAGER_UUID` | `VARCHAR(50)` | PK · FK → AM_KEY_MANAGER · NOT NULL |
| `PERMISSIONS_TYPE` | `VARCHAR(50)` | NOT NULL |
| `ROLE` | `VARCHAR(255)` | PK |

**Foreign keys**

- `KEY_MANAGER_UUID` → [`AM_KEY_MANAGER`](#am_key_manager) `UUID` (on delete: CASCADE)

## AM_LABEL

*APIM DB (WSO2AM_DB)* · PK: `UUID` · Unique: `NAME, TENANT_DOMAIN`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(50)` | PK · NOT NULL |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1024)` |  |
| `TENANT_DOMAIN` | `VARCHAR(255)` | DEFAULT 'carbon.super' |

## AM_LLM_PROVIDER

*APIM DB (WSO2AM_DB)* · PK: `UUID` · Unique: `NAME, API_VERSION, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(255)` | PK · NOT NULL |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `API_VERSION` | `VARCHAR(50)` | NOT NULL |
| `ORGANIZATION` | `VARCHAR(255)` | NOT NULL |
| `BUILT_IN_SUPPORT` | `VARCHAR(5)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1023)` |  |
| `CONFIGURATIONS` | `BLOB` | NOT NULL |
| `API_DEFINITION` | `LONGBLOB` | NOT NULL |
| `MODEL_FAMILY_SUPPORTED` | `VARCHAR(5)` | NOT NULL DEFAULT 'false' |

**Referenced by**

- [`AM_API_AI_CONFIGURATION`](#am_api_ai_configuration) via `LLM_PROVIDER_UUID`
- [`AM_LLM_PROVIDER_MODEL`](#am_llm_provider_model) via `LLM_PROVIDER_UUID`

## AM_LLM_PROVIDER_MODEL

*APIM DB (WSO2AM_DB)* · PK: `MODEL_ID`

| Column | Type | Notes |
|---|---|---|
| `MODEL_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `MODEL_NAME` | `VARCHAR(255)` | NOT NULL |
| `MODEL_FAMILY_NAME` | `VARCHAR(255)` | NULL |
| `LLM_PROVIDER_UUID` | `VARCHAR(255)` | FK → AM_LLM_PROVIDER · NOT NULL |

**Foreign keys**

- `LLM_PROVIDER_UUID` → [`AM_LLM_PROVIDER`](#am_llm_provider) `UUID`

## AM_MONETIZATION_USAGE

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(100)` | PK · NOT NULL |
| `STATE` | `VARCHAR(50)` | NOT NULL |
| `STATUS` | `VARCHAR(50)` | NOT NULL |
| `STARTED_TIME` | `VARCHAR(50)` | NOT NULL |
| `PUBLISHED_TIME` | `VARCHAR(50)` | NOT NULL |

## AM_NOTIFICATION_SUBSCRIBER

*APIM DB (WSO2AM_DB)* · PK: `UUID, SUBSCRIBER_ADDRESS`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(255)` | PK |
| `CATEGORY` | `VARCHAR(255)` |  |
| `NOTIFICATION_METHOD` | `VARCHAR(255)` |  |
| `SUBSCRIBER_ADDRESS` | `VARCHAR(255)` | PK · NOT NULL |

## AM_OPERATION_POLICY

*APIM DB (WSO2AM_DB)* · PK: `POLICY_UUID`

| Column | Type | Notes |
|---|---|---|
| `POLICY_UUID` | `VARCHAR(45)` | PK · NOT NULL |
| `POLICY_NAME` | `VARCHAR(300)` | NOT NULL |
| `POLICY_VERSION` | `VARCHAR(45)` | DEFAULT 'v1' |
| `DISPLAY_NAME` | `VARCHAR(300)` | NOT NULL |
| `POLICY_DESCRIPTION` | `VARCHAR(1024)` |  |
| `APPLICABLE_FLOWS` | `VARCHAR(45)` | NOT NULL |
| `GATEWAY_TYPES` | `VARCHAR(45)` | NOT NULL |
| `API_TYPES` | `VARCHAR(45)` | NOT NULL |
| `POLICY_PARAMETERS` | `BLOB` |  |
| `ORGANIZATION` | `VARCHAR(100)` |  |
| `POLICY_CATEGORY` | `VARCHAR(45)` | NOT NULL |
| `POLICY_MD5` | `VARCHAR(512)` | NOT NULL |

**Referenced by**

- [`AM_API_OPERATION_POLICY`](#am_api_operation_policy) via `POLICY_UUID`
- [`AM_API_OPERATION_POLICY_MAPPING`](#am_api_operation_policy_mapping) via `POLICY_UUID`
- [`AM_API_POLICY_MAPPING`](#am_api_policy_mapping) via `POLICY_UUID`
- [`AM_COMMON_OPERATION_POLICY`](#am_common_operation_policy) via `POLICY_UUID`
- [`AM_GATEWAY_POLICY_MAPPING`](#am_gateway_policy_mapping) via `POLICY_UUID`
- [`AM_OPERATION_POLICY_DEFINITION`](#am_operation_policy_definition) via `POLICY_UUID`

## AM_OPERATION_POLICY_DEFINITION

*APIM DB (WSO2AM_DB)* · PK: `DEFINITION_ID` · Unique: `POLICY_UUID, GATEWAY_TYPE`

| Column | Type | Notes |
|---|---|---|
| `DEFINITION_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `POLICY_UUID` | `VARCHAR(45)` | FK → AM_OPERATION_POLICY · NOT NULL |
| `POLICY_DEFINITION` | `MEDIUMBLOB` | NOT NULL |
| `GATEWAY_TYPE` | `VARCHAR(20)` | NOT NULL |
| `DEFINITION_MD5` | `VARCHAR(512)` | NOT NULL |

**Foreign keys**

- `POLICY_UUID` → [`AM_OPERATION_POLICY`](#am_operation_policy) `POLICY_UUID` (on delete: CASCADE)

## AM_ORGANIZATION_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `ORG_UUID`

| Column | Type | Notes |
|---|---|---|
| `ORG_UUID` | `VARCHAR(50)` | PK · NOT NULL |
| `EXT_ORG_ID` | `VARCHAR(100)` | NOT NULL |
| `DISPLAY_NAME` | `VARCHAR(100)` | NULL |
| `PARENT_ORG_UUID` | `VARCHAR(50)` |  |
| `ORG_HANDLE` | `VARCHAR(100)` |  |
| `DESCRIPTION` | `VARCHAR(256)` | NULL |
| `ROOT_ORGANIZATION` | `VARCHAR(255)` |  |

## AM_POLICY_APPLICATION

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID` · Unique: `NAME, TENANT_ID`; `UUID`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `INT(11)` | PK · NOT NULL AUTO_INCREMENT |
| `NAME` | `VARCHAR(512)` | NOT NULL |
| `DISPLAY_NAME` | `VARCHAR(512)` | NULL DEFAULT NULL |
| `TENANT_ID` | `INT(11)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1024)` | NULL DEFAULT NULL |
| `QUOTA_TYPE` | `VARCHAR(25)` | NOT NULL |
| `QUOTA` | `INT(11)` | NOT NULL |
| `QUOTA_UNIT` | `VARCHAR(10)` | NULL DEFAULT NULL |
| `UNIT_TIME` | `INT(11)` | NOT NULL |
| `TIME_UNIT` | `VARCHAR(25)` | NOT NULL |
| `IS_DEPLOYED` | `TINYINT(1)` | NOT NULL DEFAULT 0 |
| `CUSTOM_ATTRIBUTES` | `BLOB` | DEFAULT NULL |
| `RATE_LIMIT_COUNT` | `INT(11)` | NULL DEFAULT 0 |
| `RATE_LIMIT_TIME_UNIT` | `VARCHAR(25)` | NULL DEFAULT NULL |
| `UUID` | `VARCHAR(256)` |  |

## AM_POLICY_GLOBAL

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID` · Unique: `UUID`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `INT(11)` | PK · NOT NULL AUTO_INCREMENT |
| `NAME` | `VARCHAR(512)` | NOT NULL |
| `KEY_TEMPLATE` | `VARCHAR(512)` | NOT NULL |
| `TENANT_ID` | `INT(11)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1024)` | NULL DEFAULT NULL |
| `SIDDHI_QUERY` | `BLOB` | DEFAULT NULL |
| `IS_DEPLOYED` | `TINYINT(1)` | NOT NULL DEFAULT 0 |
| `UUID` | `VARCHAR(256)` |  |

## AM_POLICY_HARD_THROTTLING

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID` · Unique: `NAME, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `INT(11)` | PK · NOT NULL AUTO_INCREMENT |
| `NAME` | `VARCHAR(512)` | NOT NULL |
| `TENANT_ID` | `INT(11)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1024)` | NULL DEFAULT NULL |
| `QUOTA_TYPE` | `VARCHAR(25)` | NOT NULL |
| `QUOTA` | `INT(11)` | NOT NULL |
| `QUOTA_UNIT` | `VARCHAR(10)` | NULL DEFAULT NULL |
| `UNIT_TIME` | `INT(11)` | NOT NULL |
| `TIME_UNIT` | `VARCHAR(25)` | NOT NULL |
| `IS_DEPLOYED` | `TINYINT(1)` | NOT NULL DEFAULT 0 |

## AM_POLICY_SUBSCRIPTION

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID` · Unique: `NAME, TENANT_ID`; `UUID`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `INT(11)` | PK · NOT NULL AUTO_INCREMENT |
| `NAME` | `VARCHAR(512)` | NOT NULL |
| `DISPLAY_NAME` | `VARCHAR(512)` | NULL DEFAULT NULL |
| `TENANT_ID` | `INT(11)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1024)` | NULL DEFAULT NULL |
| `QUOTA_TYPE` | `VARCHAR(25)` | NOT NULL |
| `QUOTA` | `INT(11)` | NOT NULL |
| `QUOTA_UNIT` | `VARCHAR(10)` | NULL |
| `UNIT_TIME` | `INT(11)` | NOT NULL |
| `TIME_UNIT` | `VARCHAR(25)` | NOT NULL |
| `RATE_LIMIT_COUNT` | `INT(11)` | NULL DEFAULT NULL |
| `RATE_LIMIT_TIME_UNIT` | `VARCHAR(25)` | NULL DEFAULT NULL |
| `IS_DEPLOYED` | `TINYINT(1)` | NOT NULL DEFAULT 0 |
| `CUSTOM_ATTRIBUTES` | `BLOB` | DEFAULT NULL |
| `STOP_ON_QUOTA_REACH` | `BOOLEAN` | NOT NULL DEFAULT 0 |
| `BILLING_PLAN` | `VARCHAR(20)` | NOT NULL |
| `UUID` | `VARCHAR(256)` |  |
| `MONETIZATION_PLAN` | `VARCHAR(25)` | NULL DEFAULT NULL |
| `FIXED_RATE` | `VARCHAR(15)` | NULL DEFAULT NULL |
| `BILLING_CYCLE` | `VARCHAR(15)` | NULL DEFAULT NULL |
| `PRICE_PER_REQUEST` | `VARCHAR(15)` | NULL DEFAULT NULL |
| `CURRENCY` | `VARCHAR(15)` | NULL DEFAULT NULL |
| `MAX_COMPLEXITY` | `INT(11)` | NOT NULL DEFAULT 0 |
| `MAX_DEPTH` | `INT(11)` | NOT NULL DEFAULT 0 |
| `CONNECTIONS_COUNT` | `INT(11)` | NOT NULL DEFAULT 0 |
| `TOTAL_TOKEN_COUNT` | `BIGINT` |  |
| `PROMPT_TOKEN_COUNT` | `BIGINT` |  |
| `COMPLETION_TOKEN_COUNT` | `BIGINT` |  |

## AM_QUERY_PARAMETER_CONDITION

*APIM DB (WSO2AM_DB)* · PK: `QUERY_PARAMETER_ID`

| Column | Type | Notes |
|---|---|---|
| `QUERY_PARAMETER_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `CONDITION_GROUP_ID` | `INTEGER` | FK → AM_CONDITION_GROUP · NOT NULL |
| `PARAMETER_NAME` | `VARCHAR(255)` | DEFAULT NULL |
| `PARAMETER_VALUE` | `VARCHAR(255)` | DEFAULT NULL |
| `IS_PARAM_MAPPING` | `BOOLEAN` | DEFAULT 1 |

**Foreign keys**

- `CONDITION_GROUP_ID` → [`AM_CONDITION_GROUP`](#am_condition_group) `CONDITION_GROUP_ID` (on delete: CASCADE)

## AM_REVISION

*APIM DB (WSO2AM_DB)* · PK: `ID, API_UUID` · Unique: `REVISION_UUID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL |
| `API_UUID` | `VARCHAR(256)` | PK · FK → AM_API · NOT NULL |
| `REVISION_UUID` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(255)` |  |
| `CREATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `CREATED_BY` | `VARCHAR(255)` |  |

**Foreign keys**

- `API_UUID` → [`AM_API`](#am_api) `API_UUID` (on delete: CASCADE)

**Referenced by**

- [`AM_API_REVISION_METADATA`](#am_api_revision_metadata) via `REVISION_UUID`
- [`AM_DEPLOYED_REVISION`](#am_deployed_revision) via `REVISION_UUID`
- [`AM_DEPLOYMENT_REVISION_MAPPING`](#am_deployment_revision_mapping) via `REVISION_UUID`

## AM_REVOKED_JWT

*APIM DB (WSO2AM_DB)* · PK: `UUID`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(255)` | PK · NOT NULL |
| `SIGNATURE` | `VARCHAR(2048)` | NOT NULL |
| `EXPIRY_TIMESTAMP` | `BIGINT` | NOT NULL |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |
| `TOKEN_TYPE` | `VARCHAR(15)` | DEFAULT 'DEFAULT' |
| `TIME_CREATED` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |

## AM_SCOPE

*APIM DB (WSO2AM_DB)* · PK: `SCOPE_ID`

| Column | Type | Notes |
|---|---|---|
| `SCOPE_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `DISPLAY_NAME` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(512)` |  |
| `TENANT_ID` | `INTEGER` | NOT NULL DEFAULT -1 |
| `SCOPE_TYPE` | `VARCHAR(255)` | NOT NULL |

**Referenced by**

- [`AM_SCOPE_BINDING`](#am_scope_binding) via `SCOPE_ID`

**Related tables (not enforced)**

- `SCOPE_ID` → [`IDN_OAUTH2_SCOPE`](idn.md#idn_oauth2_scope)

## AM_SCOPE_BINDING

*APIM DB (WSO2AM_DB)* · PK: `—`

| Column | Type | Notes |
|---|---|---|
| `SCOPE_ID` | `INTEGER` | FK → AM_SCOPE · NOT NULL |
| `SCOPE_BINDING` | `VARCHAR(255)` | NOT NULL |
| `BINDING_TYPE` | `VARCHAR(255)` | NOT NULL |

**Foreign keys**

- `SCOPE_ID` → [`AM_SCOPE`](#am_scope) `SCOPE_ID` (on delete: CASCADE)

## AM_SECURITY_AUDIT_UUID_MAPPING

*APIM DB (WSO2AM_DB)* · PK: `API_ID`

| Column | Type | Notes |
|---|---|---|
| `API_ID` | `INTEGER` | PK · FK → AM_API · NOT NULL |
| `AUDIT_UUID` | `VARCHAR(255)` | NOT NULL |

**Foreign keys**

- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: CASCADE)

## AM_SERVICE_CATALOG

*APIM DB (WSO2AM_DB)* · PK: `UUID` · Unique: `SERVICE_NAME, SERVICE_VERSION, TENANT_ID`; `SERVICE_KEY, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR(36)` | PK · NOT NULL |
| `SERVICE_KEY` | `VARCHAR(512)` | NOT NULL |
| `MD5` | `VARCHAR(512)` | NOT NULL |
| `SERVICE_NAME` | `VARCHAR(255)` | NOT NULL |
| `SERVICE_VERSION` | `VARCHAR(30)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `SERVICE_URL` | `VARCHAR(2048)` | NOT NULL |
| `DEFINITION_TYPE` | `VARCHAR(20)` |  |
| `DEFINITION_URL` | `VARCHAR(2048)` |  |
| `DESCRIPTION` | `VARCHAR(1024)` |  |
| `SECURITY_TYPE` | `VARCHAR(50)` |  |
| `MUTUAL_SSL_ENABLED` | `BOOLEAN` | DEFAULT 0 |
| `CREATED_TIME` | `TIMESTAMP` | NULL |
| `LAST_UPDATED_TIME` | `TIMESTAMP` | NULL |
| `CREATED_BY` | `VARCHAR(255)` |  |
| `UPDATED_BY` | `VARCHAR(255)` |  |
| `SERVICE_DEFINITION` | `BLOB` | NOT NULL |

## AM_SHARED_SCOPE

*APIM DB (WSO2AM_DB)* · PK: `UUID`

| Column | Type | Notes |
|---|---|---|
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `UUID` | `VARCHAR (256)` | PK |
| `TENANT_ID` | `INTEGER` |  |

## AM_SUBJECT_ENTITY_REVOKED_EVENT

*APIM DB (WSO2AM_DB)* · PK: `ENTITY_ID, ENTITY_TYPE, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `ENTITY_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `ENTITY_TYPE` | `VARCHAR(100)` | PK · NOT NULL |
| `TIME_REVOKED` | `TIMESTAMP` | NOT NULL |
| `ORGANIZATION` | `VARCHAR(100)` | PK |

## AM_SUBSCRIBER

*APIM DB (WSO2AM_DB)* · PK: `SUBSCRIBER_ID` · Unique: `TENANT_ID, USER_ID`

| Column | Type | Notes |
|---|---|---|
| `SUBSCRIBER_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `USER_ID` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |
| `EMAIL_ADDRESS` | `VARCHAR(256)` | NULL |
| `DATE_SUBSCRIBED` | `TIMESTAMP` | NOT NULL |
| `CREATED_BY` | `VARCHAR(100)` |  |
| `CREATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `UPDATED_BY` | `VARCHAR(100)` |  |
| `UPDATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |

**Referenced by**

- [`AM_API_RATINGS`](#am_api_ratings) via `SUBSCRIBER_ID`
- [`AM_APPLICATION`](#am_application) via `SUBSCRIBER_ID`
- [`AM_APPLICATION_REGISTRATION`](#am_application_registration) via `SUBSCRIBER_ID`

## AM_SUBSCRIPTION

*APIM DB (WSO2AM_DB)* · PK: `SUBSCRIPTION_ID` · Unique: `UUID`

| Column | Type | Notes |
|---|---|---|
| `SUBSCRIPTION_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TIER_ID` | `VARCHAR(50)` |  |
| `TIER_ID_PENDING` | `VARCHAR(50)` |  |
| `API_ID` | `INTEGER` | FK → AM_API |
| `LAST_ACCESSED` | `TIMESTAMP` | NULL |
| `APPLICATION_ID` | `INTEGER` | FK → AM_APPLICATION |
| `SUB_STATUS` | `VARCHAR(50)` |  |
| `SUBS_CREATE_STATE` | `VARCHAR(50)` | DEFAULT 'SUBSCRIBE' |
| `CREATED_BY` | `VARCHAR(100)` |  |
| `CREATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `UPDATED_BY` | `VARCHAR(100)` |  |
| `UPDATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `UUID` | `VARCHAR(256)` |  |

**Foreign keys**

- `APPLICATION_ID` → [`AM_APPLICATION`](#am_application) `APPLICATION_ID` (on delete: CASCADE)
- `API_ID` → [`AM_API`](#am_api) `API_ID` (on delete: CASCADE)

## AM_SYSTEM_APPS

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `CONSUMER_KEY`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `NAME` | `VARCHAR(50)` | NOT NULL |
| `CONSUMER_KEY` | `VARCHAR(512)` | NOT NULL |
| `CONSUMER_SECRET` | `VARCHAR(512)` | NOT NULL |
| `CREATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `TENANT_DOMAIN` | `VARCHAR(255)` | DEFAULT 'carbon.super' |

**Related tables (not enforced)**

- `CONSUMER_KEY` → [`IDN_OAUTH_CONSUMER_APPS`](idn.md#idn_oauth_consumer_apps)

## AM_SYSTEM_CONFIGS

*APIM DB (WSO2AM_DB)* · PK: `ORGANIZATION, CONFIG_TYPE`

| Column | Type | Notes |
|---|---|---|
| `ORGANIZATION` | `VARCHAR(100)` | PK · NOT NULL |
| `CONFIG_TYPE` | `VARCHAR(100)` | PK · NOT NULL |
| `CONFIGURATION` | `BLOB` | NOT NULL |

## AM_TASK_LOCK

*APIM DB (WSO2AM_DB)* · PK: `TASK_ID`

| Column | Type | Notes |
|---|---|---|
| `LOCK_TIME` | `BIGINT` | NOT NULL |
| `TASK_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `NODE_ID` | `VARCHAR(255)` | NOT NULL |

## AM_TENANT_THEMES

*APIM DB (WSO2AM_DB)* · PK: `TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `TENANT_ID` | `INTEGER` | PK · NOT NULL |
| `THEME` | `MEDIUMBLOB` | NOT NULL |

## AM_THROTTLE_TIER_PERMISSIONS

*APIM DB (WSO2AM_DB)* · PK: `THROTTLE_TIER_PERMISSIONS_ID`

| Column | Type | Notes |
|---|---|---|
| `THROTTLE_TIER_PERMISSIONS_ID` | `INT` | PK · NOT NULL AUTO_INCREMENT |
| `TIER` | `VARCHAR(50)` | NULL |
| `PERMISSIONS_TYPE` | `VARCHAR(50)` | NULL |
| `ROLES` | `VARCHAR(512)` | NULL |
| `TENANT_ID` | `INT(11)` | NULL |

## AM_TIER_PERMISSIONS

*APIM DB (WSO2AM_DB)* · PK: `TIER_PERMISSIONS_ID`

| Column | Type | Notes |
|---|---|---|
| `TIER_PERMISSIONS_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `TIER` | `VARCHAR(50)` | NOT NULL |
| `PERMISSIONS_TYPE` | `VARCHAR(50)` | NOT NULL |
| `ROLES` | `VARCHAR(512)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | NOT NULL |

## AM_TRANSACTION_RECORDS

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(255)` | PK · NOT NULL |
| `HOST` | `VARCHAR(255)` |  |
| `SERVER_ID` | `VARCHAR(255)` |  |
| `SERVER_TYPE` | `VARCHAR(20)` |  |
| `COUNT` | `INT` | NOT NULL |
| `RECORDED_TIME` | `TIMESTAMP` | NOT NULL |

## AM_USAGE_UPLOADED_FILES

*APIM DB (WSO2AM_DB)* · PK: `TENANT_DOMAIN, FILE_NAME, FILE_TIMESTAMP`

| Column | Type | Notes |
|---|---|---|
| `TENANT_DOMAIN` | `VARCHAR(255)` | PK · NOT NULL |
| `FILE_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `FILE_TIMESTAMP` | `TIMESTAMP` | PK · DEFAULT CURRENT_TIMESTAMP |
| `FILE_PROCESSED` | `TINYINT(1)` | DEFAULT FALSE |
| `FILE_CONTENT` | `MEDIUMBLOB` | DEFAULT NULL |

## AM_USER

*APIM DB (WSO2AM_DB)* · PK: `USER_ID`

| Column | Type | Notes |
|---|---|---|
| `USER_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `USER_NAME` | `VARCHAR(255)` | NOT NULL |

## AM_WEBHOOKS_SUBSCRIPTION

*APIM DB (WSO2AM_DB)* · PK: `WH_SUBSCRIPTION_ID`

| Column | Type | Notes |
|---|---|---|
| `WH_SUBSCRIPTION_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `API_UUID` | `VARCHAR(255)` | NOT NULL |
| `APPLICATION_ID` | `VARCHAR(20)` | NOT NULL |
| `TENANT_DOMAIN` | `VARCHAR(255)` | NOT NULL |
| `HUB_CALLBACK_URL` | `VARCHAR(1024)` | NOT NULL |
| `HUB_TOPIC` | `VARCHAR(255)` | NOT NULL |
| `HUB_SECRET` | `VARCHAR(2048)` |  |
| `HUB_LEASE_SECONDS` | `INTEGER` |  |
| `UPDATED_AT` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `EXPIRY_AT` | `BIGINT` |  |
| `DELIVERED_AT` | `TIMESTAMP` | NULL |
| `DELIVERY_STATE` | `INTEGER` | NOT NULL DEFAULT 0 |

**Related tables (not enforced)**

- `API_UUID` → [`AM_API`](#am_api)
- `APPLICATION_ID` → [`AM_APPLICATION`](#am_application)

## AM_WEBHOOKS_UNSUBSCRIPTION

*APIM DB (WSO2AM_DB)* · PK: `—`

| Column | Type | Notes |
|---|---|---|
| `API_UUID` | `VARCHAR(255)` | NOT NULL |
| `APPLICATION_ID` | `VARCHAR(20)` | NOT NULL |
| `TENANT_DOMAIN` | `VARCHAR(255)` | NOT NULL |
| `HUB_CALLBACK_URL` | `VARCHAR(1024)` | NOT NULL |
| `HUB_TOPIC` | `VARCHAR(255)` | NOT NULL |
| `HUB_SECRET` | `VARCHAR(2048)` |  |
| `HUB_LEASE_SECONDS` | `INTEGER` |  |
| `ADDED_AT` | `TIMESTAMP` | NOT NULL DEFAULT CURRENT_TIMESTAMP |

**Related tables (not enforced)**

- `API_UUID` → [`AM_API`](#am_api)
- `APPLICATION_ID` → [`AM_APPLICATION`](#am_application)

## AM_WORKFLOWS

*APIM DB (WSO2AM_DB)* · PK: `WF_ID` · Unique: `WF_EXTERNAL_REFERENCE`

| Column | Type | Notes |
|---|---|---|
| `WF_ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `WF_REFERENCE` | `VARCHAR(255)` | NOT NULL |
| `WF_TYPE` | `VARCHAR(255)` | NOT NULL |
| `WF_STATUS` | `VARCHAR(255)` | NOT NULL |
| `WF_CREATED_TIME` | `TIMESTAMP` |  |
| `WF_UPDATED_TIME` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP |
| `WF_STATUS_DESC` | `VARCHAR(1000)` |  |
| `TENANT_ID` | `INTEGER` |  |
| `TENANT_DOMAIN` | `VARCHAR(255)` |  |
| `WF_EXTERNAL_REFERENCE` | `VARCHAR(255)` | NOT NULL |
| `WF_METADATA` | `BLOB` | DEFAULT NULL |
| `WF_PROPERTIES` | `BLOB` | DEFAULT NULL |

