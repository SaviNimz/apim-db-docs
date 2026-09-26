# UM_* — Users, roles, tenants

34 tables in APIM 4.7.0.

## UM_ACCOUNT_MAPPING

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID` · Unique: `UM_USER_NAME, UM_TENANT_ID, UM_USER_STORE_DOMAIN, UM_ACC_LINK_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_USER_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | FK → UM_TENANT · NOT NULL |
| `UM_USER_STORE_DOMAIN` | `VARCHAR(100)` |  |
| `UM_ACC_LINK_ID` | `INTEGER` | NOT NULL |

**Foreign keys**

- `UM_TENANT_ID` → [`UM_TENANT`](#um_tenant) `UM_ID` (on delete: CASCADE)

## UM_CLAIM

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_DIALECT_ID, UM_CLAIM_URI, UM_TENANT_ID, UM_MAPPED_ATTRIBUTE_DOMAIN`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_DIALECT_ID` | `INTEGER` | FK → UM_DIALECT · NOT NULL |
| `UM_CLAIM_URI` | `VARCHAR(255)` | NOT NULL |
| `UM_DISPLAY_TAG` | `VARCHAR(255)` |  |
| `UM_DESCRIPTION` | `VARCHAR(255)` |  |
| `UM_MAPPED_ATTRIBUTE_DOMAIN` | `VARCHAR(255)` |  |
| `UM_MAPPED_ATTRIBUTE` | `VARCHAR(255)` |  |
| `UM_REG_EX` | `VARCHAR(255)` |  |
| `UM_SUPPORTED` | `SMALLINT` |  |
| `UM_REQUIRED` | `SMALLINT` |  |
| `UM_DISPLAY_ORDER` | `INTEGER` |  |
| `UM_CHECKED_ATTRIBUTE` | `SMALLINT` |  |
| `UM_READ_ONLY` | `SMALLINT` |  |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_DIALECT · DEFAULT 0 |

**Foreign keys**

- `UM_DIALECT_ID, UM_TENANT_ID` → [`UM_DIALECT`](#um_dialect) `UM_ID, UM_TENANT_ID`

**Referenced by**

- [`UM_CLAIM_BEHAVIOR`](#um_claim_behavior) via `UM_CLAIM_ID, UM_TENANT_ID`

## UM_CLAIM_BEHAVIOR

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_PROFILE_ID` | `INTEGER` | FK → UM_PROFILE_CONFIG |
| `UM_CLAIM_ID` | `INTEGER` | FK → UM_CLAIM |
| `UM_BEHAVIOUR` | `SMALLINT` |  |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_CLAIM · DEFAULT 0 |

**Foreign keys**

- `UM_PROFILE_ID, UM_TENANT_ID` → [`UM_PROFILE_CONFIG`](#um_profile_config) `UM_ID, UM_TENANT_ID`
- `UM_CLAIM_ID, UM_TENANT_ID` → [`UM_CLAIM`](#um_claim) `UM_ID, UM_TENANT_ID`

## UM_DIALECT

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_DIALECT_URI, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_DIALECT_URI` | `VARCHAR(255)` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |

**Referenced by**

- [`UM_CLAIM`](#um_claim) via `UM_DIALECT_ID, UM_TENANT_ID`
- [`UM_PROFILE_CONFIG`](#um_profile_config) via `UM_DIALECT_ID, UM_TENANT_ID`

## UM_DOMAIN

*Shared DB (WSO2SHARED_DB)* · PK: `UM_DOMAIN_ID, UM_TENANT_ID` · Unique: `UM_DOMAIN_NAME, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_DOMAIN_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_DOMAIN_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |

**Referenced by**

- [`UM_GROUP_UUID_DOMAIN_MAPPER`](#um_group_uuid_domain_mapper) via `UM_DOMAIN_ID, UM_TENANT_ID`
- [`UM_HYBRID_GROUP_ROLE`](#um_hybrid_group_role) via `UM_DOMAIN_ID, UM_TENANT_ID`
- [`UM_HYBRID_USER_ROLE`](#um_hybrid_user_role) via `UM_DOMAIN_ID, UM_TENANT_ID`
- [`UM_ROLE_PERMISSION`](#um_role_permission) via `UM_DOMAIN_ID, UM_TENANT_ID`
- [`UM_UUID_DOMAIN_MAPPER`](#um_uuid_domain_mapper) via `UM_DOMAIN_ID, UM_TENANT_ID`

## UM_GROUP_UUID_DOMAIN_MAPPER

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID` · Unique: `UM_GROUP_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_GROUP_ID` | `VARCHAR(255)` | NOT NULL |
| `UM_DOMAIN_ID` | `INTEGER` | FK → UM_DOMAIN · NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | FK → UM_DOMAIN · DEFAULT 0 |

**Foreign keys**

- `UM_DOMAIN_ID, UM_TENANT_ID` → [`UM_DOMAIN`](#um_domain) `UM_DOMAIN_ID, UM_TENANT_ID` (on delete: CASCADE)

## UM_HYBRID_GROUP_ROLE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_GROUP_NAME, UM_ROLE_ID, UM_TENANT_ID, UM_DOMAIN_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_GROUP_NAME` | `VARCHAR(255)` |  |
| `UM_ROLE_ID` | `INTEGER` | FK → UM_HYBRID_ROLE · NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_DOMAIN · DEFAULT 0 |
| `UM_DOMAIN_ID` | `INTEGER` | FK → UM_DOMAIN |

**Foreign keys**

- `UM_ROLE_ID, UM_TENANT_ID` → [`UM_HYBRID_ROLE`](#um_hybrid_role) `UM_ID, UM_TENANT_ID` (on delete: CASCADE)
- `UM_DOMAIN_ID, UM_TENANT_ID` → [`UM_DOMAIN`](#um_domain) `UM_DOMAIN_ID, UM_TENANT_ID` (on delete: CASCADE)

## UM_HYBRID_REMEMBER_ME

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_USER_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_COOKIE_VALUE` | `VARCHAR(1024)` |  |
| `UM_CREATED_TIME` | `TIMESTAMP` |  |
| `UM_TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |

## UM_HYBRID_ROLE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_ROLE_NAME, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_ROLE_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |

**Referenced by**

- [`UM_HYBRID_GROUP_ROLE`](#um_hybrid_group_role) via `UM_ROLE_ID, UM_TENANT_ID`
- [`UM_HYBRID_USER_ROLE`](#um_hybrid_user_role) via `UM_ROLE_ID, UM_TENANT_ID`

## UM_HYBRID_USER_ROLE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_USER_NAME, UM_ROLE_ID, UM_TENANT_ID, UM_DOMAIN_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_USER_NAME` | `VARCHAR(255)` |  |
| `UM_ROLE_ID` | `INTEGER` | FK → UM_HYBRID_ROLE · NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_DOMAIN · DEFAULT 0 |
| `UM_DOMAIN_ID` | `INTEGER` | FK → UM_DOMAIN |

**Foreign keys**

- `UM_ROLE_ID, UM_TENANT_ID` → [`UM_HYBRID_ROLE`](#um_hybrid_role) `UM_ID, UM_TENANT_ID` (on delete: CASCADE)
- `UM_DOMAIN_ID, UM_TENANT_ID` → [`UM_DOMAIN`](#um_domain) `UM_DOMAIN_ID, UM_TENANT_ID` (on delete: CASCADE)

## UM_MODULE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID` · Unique: `UM_MODULE_NAME`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_MODULE_NAME` | `VARCHAR(100)` |  |

**Referenced by**

- [`UM_MODULE_ACTIONS`](#um_module_actions) via `UM_MODULE_ID`

## UM_MODULE_ACTIONS

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ACTION, UM_MODULE_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ACTION` | `VARCHAR(255)` | PK · NOT NULL |
| `UM_MODULE_ID` | `INTEGER` | PK · FK → UM_MODULE · NOT NULL |

**Foreign keys**

- `UM_MODULE_ID` → [`UM_MODULE`](#um_module) `UM_ID` (on delete: CASCADE)

## UM_ORG

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `VARCHAR(36)` | PK · NOT NULL |
| `UM_ORG_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_ORG_DESCRIPTION` | `VARCHAR(1024)` |  |
| `UM_CREATED_TIME` | `TIMESTAMP` | NOT NULL |
| `UM_LAST_MODIFIED` | `TIMESTAMP` | NOT NULL |
| `UM_STATUS` | `VARCHAR(255)` | DEFAULT 'ACTIVE' NOT NULL |
| `UM_PARENT_ID` | `VARCHAR(36)` | FK → UM_ORG |
| `UM_ORG_TYPE` | `VARCHAR(100)` | NOT NULL |

**Foreign keys**

- `UM_PARENT_ID` → [`UM_ORG`](#um_org) `UM_ID` (on delete: CASCADE)

**Referenced by**

- [`UM_ORG`](#um_org) via `UM_PARENT_ID`
- [`UM_ORG_ATTRIBUTE`](#um_org_attribute) via `UM_ORG_ID`
- [`UM_ORG_HIERARCHY`](#um_org_hierarchy) via `UM_PARENT_ID`
- [`UM_ORG_HIERARCHY`](#um_org_hierarchy) via `UM_ID`
- [`UM_ORG_ROLE`](#um_org_role) via `UM_ORG_ID`

## UM_ORG_ATTRIBUTE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID` · Unique: `UM_ORG_ID, UM_ATTRIBUTE_KEY`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_ORG_ID` | `VARCHAR(36)` | FK → UM_ORG · NOT NULL |
| `UM_ATTRIBUTE_KEY` | `VARCHAR(255)` | NOT NULL |
| `UM_ATTRIBUTE_VALUE` | `VARCHAR(512)` |  |

**Foreign keys**

- `UM_ORG_ID` → [`UM_ORG`](#um_org) `UM_ID` (on delete: CASCADE)

## UM_ORG_HIERARCHY

*Shared DB (WSO2SHARED_DB)* · PK: `UM_PARENT_ID, UM_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_PARENT_ID` | `VARCHAR(36)` | PK · FK → UM_ORG · NOT NULL |
| `UM_ID` | `VARCHAR(36)` | PK · FK → UM_ORG · NOT NULL |
| `DEPTH` | `INTEGER` |  |

**Foreign keys**

- `UM_PARENT_ID` → [`UM_ORG`](#um_org) `UM_ID` (on delete: CASCADE)
- `UM_ID` → [`UM_ORG`](#um_org) `UM_ID` (on delete: CASCADE)

## UM_ORG_PERMISSION

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_RESOURCE_ID` | `VARCHAR(255)` | NOT NULL |
| `UM_ACTION` | `VARCHAR(255)` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | DEFAULT 0 |

**Referenced by**

- [`UM_ORG_ROLE_PERMISSION`](#um_org_role_permission) via `UM_PERMISSION_ID`

## UM_ORG_ROLE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ROLE_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ROLE_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `UM_ROLE_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_ORG_ID` | `VARCHAR(36)` | FK → UM_ORG · NOT NULL |

**Foreign keys**

- `UM_ORG_ID` → [`UM_ORG`](#um_org) `UM_ID` (on delete: CASCADE)

**Referenced by**

- [`UM_ORG_ROLE_GROUP`](#um_org_role_group) via `UM_ROLE_ID`
- [`UM_ORG_ROLE_PERMISSION`](#um_org_role_permission) via `UM_ROLE_ID`
- [`UM_ORG_ROLE_USER`](#um_org_role_user) via `UM_ROLE_ID`

## UM_ORG_ROLE_GROUP

*Shared DB (WSO2SHARED_DB)* · PK: `—`

| Column | Type | Notes |
|---|---|---|
| `UM_GROUP_ID` | `VARCHAR(255)` | NOT NULL |
| `UM_ROLE_ID` | `VARCHAR(255)` | FK → UM_ORG_ROLE · NOT NULL |

**Foreign keys**

- `UM_ROLE_ID` → [`UM_ORG_ROLE`](#um_org_role) `UM_ROLE_ID` (on delete: CASCADE)

## UM_ORG_ROLE_PERMISSION

*Shared DB (WSO2SHARED_DB)* · PK: `—`

| Column | Type | Notes |
|---|---|---|
| `UM_PERMISSION_ID` | `INTEGER` | FK → UM_ORG_PERMISSION · NOT NULL |
| `UM_ROLE_ID` | `VARCHAR(255)` | FK → UM_ORG_ROLE · NOT NULL |

**Foreign keys**

- `UM_ROLE_ID` → [`UM_ORG_ROLE`](#um_org_role) `UM_ROLE_ID` (on delete: CASCADE)
- `UM_PERMISSION_ID` → [`UM_ORG_PERMISSION`](#um_org_permission) `UM_ID` (on delete: CASCADE)

## UM_ORG_ROLE_USER

*Shared DB (WSO2SHARED_DB)* · PK: `—`

| Column | Type | Notes |
|---|---|---|
| `UM_USER_ID` | `VARCHAR(255)` | NOT NULL |
| `UM_ROLE_ID` | `VARCHAR(255)` | FK → UM_ORG_ROLE · NOT NULL |

**Foreign keys**

- `UM_ROLE_ID` → [`UM_ORG_ROLE`](#um_org_role) `UM_ROLE_ID` (on delete: CASCADE)

## UM_PERMISSION

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_RESOURCE_ID, UM_ACTION, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_RESOURCE_ID` | `VARCHAR(255)` | NOT NULL |
| `UM_ACTION` | `VARCHAR(255)` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |
| `UM_MODULE_ID` | `INTEGER` | DEFAULT 0 |

**Referenced by**

- [`UM_ROLE_PERMISSION`](#um_role_permission) via `UM_PERMISSION_ID, UM_TENANT_ID`
- [`UM_USER_PERMISSION`](#um_user_permission) via `UM_PERMISSION_ID, UM_TENANT_ID`

## UM_PROFILE_CONFIG

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_DIALECT_ID` | `INTEGER` | FK → UM_DIALECT · NOT NULL |
| `UM_PROFILE_NAME` | `VARCHAR(255)` |  |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_DIALECT · DEFAULT 0 |

**Foreign keys**

- `UM_DIALECT_ID, UM_TENANT_ID` → [`UM_DIALECT`](#um_dialect) `UM_ID, UM_TENANT_ID`

**Referenced by**

- [`UM_CLAIM_BEHAVIOR`](#um_claim_behavior) via `UM_PROFILE_ID, UM_TENANT_ID`

## UM_ROLE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_ROLE_NAME, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_ROLE_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |
| `UM_SHARED_ROLE` | `BOOLEAN` | DEFAULT FALSE |

**Referenced by**

- [`UM_SHARED_USER_ROLE`](#um_shared_user_role) via `UM_ROLE_ID, UM_ROLE_TENANT_ID`
- [`UM_USER_ROLE`](#um_user_role) via `UM_ROLE_ID, UM_TENANT_ID`

## UM_ROLE_PERMISSION

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_PERMISSION_ID, UM_ROLE_NAME, UM_TENANT_ID, UM_DOMAIN_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_PERMISSION_ID` | `INTEGER` | FK → UM_PERMISSION · NOT NULL |
| `UM_ROLE_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_IS_ALLOWED` | `SMALLINT` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_DOMAIN · DEFAULT 0 |
| `UM_DOMAIN_ID` | `INTEGER` | FK → UM_DOMAIN |

**Foreign keys**

- `UM_PERMISSION_ID, UM_TENANT_ID` → [`UM_PERMISSION`](#um_permission) `UM_ID, UM_TENANT_ID` (on delete: CASCADE)
- `UM_DOMAIN_ID, UM_TENANT_ID` → [`UM_DOMAIN`](#um_domain) `UM_DOMAIN_ID, UM_TENANT_ID` (on delete: CASCADE)

## UM_SHARED_USER_ROLE

*Shared DB (WSO2SHARED_DB)* · PK: `ID` · Unique: `UM_USER_ID, UM_ROLE_ID, UM_USER_TENANT_ID, UM_ROLE_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_ROLE_ID` | `INTEGER` | FK → UM_ROLE · NOT NULL |
| `UM_USER_ID` | `INTEGER` | FK → UM_USER · NOT NULL |
| `UM_USER_TENANT_ID` | `INTEGER` | FK → UM_USER · NOT NULL |
| `UM_ROLE_TENANT_ID` | `INTEGER` | FK → UM_ROLE · NOT NULL |

**Foreign keys**

- `UM_ROLE_ID, UM_ROLE_TENANT_ID` → [`UM_ROLE`](#um_role) `UM_ID, UM_TENANT_ID` (on delete: CASCADE)
- `UM_USER_ID, UM_USER_TENANT_ID` → [`UM_USER`](#um_user) `UM_ID, UM_TENANT_ID` (on delete: CASCADE)

## UM_SYSTEM_ROLE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_ROLE_NAME, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_ROLE_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |

**Referenced by**

- [`UM_SYSTEM_USER_ROLE`](#um_system_user_role) via `UM_ROLE_ID, UM_TENANT_ID`

## UM_SYSTEM_USER

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_USER_NAME, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_USER_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_USER_PASSWORD` | `VARCHAR(255)` | NOT NULL |
| `UM_SALT_VALUE` | `VARCHAR(31)` |  |
| `UM_REQUIRE_CHANGE` | `BOOLEAN` | DEFAULT FALSE |
| `UM_CHANGED_TIME` | `TIMESTAMP` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |

## UM_SYSTEM_USER_ROLE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_USER_NAME, UM_ROLE_ID, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_USER_NAME` | `VARCHAR(255)` |  |
| `UM_ROLE_ID` | `INTEGER` | FK → UM_SYSTEM_ROLE · NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_SYSTEM_ROLE · DEFAULT 0 |

**Foreign keys**

- `UM_ROLE_ID, UM_TENANT_ID` → [`UM_SYSTEM_ROLE`](#um_system_role) `UM_ID, UM_TENANT_ID`

## UM_TENANT

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID` · Unique: `UM_DOMAIN_NAME`; `UM_TENANT_UUID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_TENANT_UUID` | `VARCHAR(36)` | NOT NULL |
| `UM_DOMAIN_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_EMAIL` | `VARCHAR(255)` |  |
| `UM_ACTIVE` | `BOOLEAN` | DEFAULT FALSE |
| `UM_CREATED_DATE` | `TIMESTAMP` | NOT NULL |
| `UM_USER_CONFIG` | `LONGBLOB` |  |
| `UM_ORG_UUID` | `VARCHAR(36)` | DEFAULT NULL |

**Referenced by**

- [`UM_ACCOUNT_MAPPING`](#um_account_mapping) via `UM_TENANT_ID`

## UM_USER

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_USER_ID`; `UM_USER_NAME, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_USER_ID` | `VARCHAR(255)` | NOT NULL |
| `UM_USER_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_USER_PASSWORD` | `VARCHAR(255)` | NOT NULL |
| `UM_SALT_VALUE` | `VARCHAR(31)` |  |
| `UM_REQUIRE_CHANGE` | `BOOLEAN` | DEFAULT FALSE |
| `UM_CHANGED_TIME` | `TIMESTAMP` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · DEFAULT 0 |

**Referenced by**

- [`UM_SHARED_USER_ROLE`](#um_shared_user_role) via `UM_USER_ID, UM_USER_TENANT_ID`
- [`UM_USER_ATTRIBUTE`](#um_user_attribute) via `UM_USER_ID, UM_TENANT_ID`
- [`UM_USER_ROLE`](#um_user_role) via `UM_USER_ID, UM_TENANT_ID`

## UM_USER_ATTRIBUTE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_ATTR_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_ATTR_VALUE` | `VARCHAR(1024)` |  |
| `UM_PROFILE_ID` | `VARCHAR(255)` |  |
| `UM_USER_ID` | `INTEGER` | FK → UM_USER |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_USER · DEFAULT 0 |

**Foreign keys**

- `UM_USER_ID, UM_TENANT_ID` → [`UM_USER`](#um_user) `UM_ID, UM_TENANT_ID`

## UM_USER_PERMISSION

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_PERMISSION_ID` | `INTEGER` | FK → UM_PERMISSION · NOT NULL |
| `UM_USER_NAME` | `VARCHAR(255)` | NOT NULL |
| `UM_IS_ALLOWED` | `SMALLINT` | NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_PERMISSION · DEFAULT 0 |

**Foreign keys**

- `UM_PERMISSION_ID, UM_TENANT_ID` → [`UM_PERMISSION`](#um_permission) `UM_ID, UM_TENANT_ID` (on delete: CASCADE)

## UM_USER_ROLE

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID, UM_TENANT_ID` · Unique: `UM_USER_ID, UM_ROLE_ID, UM_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_ROLE_ID` | `INTEGER` | FK → UM_ROLE · NOT NULL |
| `UM_USER_ID` | `INTEGER` | FK → UM_USER · NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | PK · FK → UM_USER · DEFAULT 0 |

**Foreign keys**

- `UM_ROLE_ID, UM_TENANT_ID` → [`UM_ROLE`](#um_role) `UM_ID, UM_TENANT_ID`
- `UM_USER_ID, UM_TENANT_ID` → [`UM_USER`](#um_user) `UM_ID, UM_TENANT_ID`

## UM_UUID_DOMAIN_MAPPER

*Shared DB (WSO2SHARED_DB)* · PK: `UM_ID` · Unique: `UM_USER_ID`

| Column | Type | Notes |
|---|---|---|
| `UM_ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `UM_USER_ID` | `VARCHAR(255)` | NOT NULL |
| `UM_DOMAIN_ID` | `INTEGER` | FK → UM_DOMAIN · NOT NULL |
| `UM_TENANT_ID` | `INTEGER` | FK → UM_DOMAIN · DEFAULT 0 |

**Foreign keys**

- `UM_DOMAIN_ID, UM_TENANT_ID` → [`UM_DOMAIN`](#um_domain) `UM_DOMAIN_ID, UM_TENANT_ID` (on delete: CASCADE)

