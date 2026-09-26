# CM_* — Consent management

10 tables. Generated from the 4.7.0 DDL.

## CM_CONSENT_RECEIPT_PROPERTY

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `CONSENT_RECEIPT_ID, NAME`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `CONSENT_RECEIPT_ID` | `VARCHAR(255)` | FK → CM_RECEIPT · NOT NULL |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `VALUE` | `VARCHAR(1023)` | NOT NULL |

**Foreign keys**

- `CONSENT_RECEIPT_ID` → [`CM_RECEIPT`](#cm_receipt) `CONSENT_RECEIPT_ID`

## CM_PII_CATEGORY

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `NAME, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1023)` |  |
| `DISPLAY_NAME` | `VARCHAR(255)` |  |
| `IS_SENSITIVE` | `INTEGER` | NOT NULL |
| `TENANT_ID` | `INTEGER` | DEFAULT '-1234' |

**Referenced by**

- [`CM_SP_PURPOSE_PII_CAT_ASSOC`](#cm_sp_purpose_pii_cat_assoc) via `PII_CATEGORY_ID`

## CM_PURPOSE

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `NAME, TENANT_ID, PURPOSE_GROUP, GROUP_TYPE`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1023)` |  |
| `PURPOSE_GROUP` | `VARCHAR(255)` | NOT NULL |
| `GROUP_TYPE` | `VARCHAR(255)` | NOT NULL |
| `TENANT_ID` | `INTEGER` | DEFAULT '-1234' |

**Referenced by**

- [`CM_SP_PURPOSE_ASSOC`](#cm_sp_purpose_assoc) via `PURPOSE_ID`

## CM_PURPOSE_CATEGORY

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `NAME, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `NAME` | `VARCHAR(255)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1023)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT '-1234' |

**Referenced by**

- [`CM_SP_PURPOSE_PURPOSE_CAT_ASSC`](#cm_sp_purpose_purpose_cat_assc) via `PURPOSE_CATEGORY_ID`

## CM_PURPOSE_PII_CAT_ASSOC

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `PURPOSE_ID, CM_PII_CATEGORY_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `PURPOSE_ID` | `INTEGER` | NOT NULL |
| `CM_PII_CATEGORY_ID` | `INTEGER` | NOT NULL |
| `IS_MANDATORY` | `INTEGER` | NOT NULL |

**Likely links (no FK)**

- `PURPOSE_ID` → [`CM_SP_PURPOSE_ASSOC`](#cm_sp_purpose_assoc) *(same-name key)*

## CM_RECEIPT

*APIM DB (WSO2AM_DB)* · PK: `CONSENT_RECEIPT_ID`

| Column | Type | Notes |
|---|---|---|
| `CONSENT_RECEIPT_ID` | `VARCHAR(255)` | PK · NOT NULL |
| `VERSION` | `VARCHAR(255)` | NOT NULL |
| `JURISDICTION` | `VARCHAR(255)` | NOT NULL |
| `CONSENT_TIMESTAMP` | `TIMESTAMP` | NOT NULL |
| `COLLECTION_METHOD` | `VARCHAR(255)` | NOT NULL |
| `LANGUAGE` | `VARCHAR(255)` | NOT NULL |
| `PII_PRINCIPAL_ID` | `VARCHAR(255)` | NOT NULL |
| `PRINCIPAL_TENANT_ID` | `INTEGER` | DEFAULT '-1234' |
| `POLICY_URL` | `VARCHAR(255)` | NOT NULL |
| `STATE` | `VARCHAR(255)` | NOT NULL |
| `PII_CONTROLLER` | `VARCHAR(2048)` | NOT NULL |

**Referenced by**

- [`CM_CONSENT_RECEIPT_PROPERTY`](#cm_consent_receipt_property) via `CONSENT_RECEIPT_ID`
- [`CM_RECEIPT_SP_ASSOC`](#cm_receipt_sp_assoc) via `CONSENT_RECEIPT_ID`

## CM_RECEIPT_SP_ASSOC

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `CONSENT_RECEIPT_ID, SP_NAME, SP_TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `CONSENT_RECEIPT_ID` | `VARCHAR(255)` | FK → CM_RECEIPT · NOT NULL |
| `SP_NAME` | `VARCHAR(255)` | NOT NULL |
| `SP_DISPLAY_NAME` | `VARCHAR(255)` |  |
| `SP_DESCRIPTION` | `VARCHAR(1024)` |  |
| `SP_TENANT_ID` | `INTEGER` | DEFAULT '-1234' |

**Foreign keys**

- `CONSENT_RECEIPT_ID` → [`CM_RECEIPT`](#cm_receipt) `CONSENT_RECEIPT_ID`

**Referenced by**

- [`CM_SP_PURPOSE_ASSOC`](#cm_sp_purpose_assoc) via `RECEIPT_SP_ASSOC`

## CM_SP_PURPOSE_ASSOC

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `RECEIPT_SP_ASSOC, PURPOSE_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · AUTO_INCREMENT |
| `RECEIPT_SP_ASSOC` | `INTEGER` | FK → CM_RECEIPT_SP_ASSOC · NOT NULL |
| `PURPOSE_ID` | `INTEGER` | FK → CM_PURPOSE · NOT NULL |
| `CONSENT_TYPE` | `VARCHAR(255)` | NOT NULL |
| `IS_PRIMARY_PURPOSE` | `INTEGER` | NOT NULL |
| `TERMINATION` | `VARCHAR(255)` | NOT NULL |
| `THIRD_PARTY_DISCLOSURE` | `INTEGER` | NOT NULL |
| `THIRD_PARTY_NAME` | `VARCHAR(255)` |  |

**Foreign keys**

- `RECEIPT_SP_ASSOC` → [`CM_RECEIPT_SP_ASSOC`](#cm_receipt_sp_assoc) `ID`
- `PURPOSE_ID` → [`CM_PURPOSE`](#cm_purpose) `ID`

**Referenced by**

- [`CM_SP_PURPOSE_PII_CAT_ASSOC`](#cm_sp_purpose_pii_cat_assoc) via `SP_PURPOSE_ASSOC_ID`
- [`CM_SP_PURPOSE_PURPOSE_CAT_ASSC`](#cm_sp_purpose_purpose_cat_assc) via `SP_PURPOSE_ASSOC_ID`

## CM_SP_PURPOSE_PII_CAT_ASSOC

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `SP_PURPOSE_ASSOC_ID, PII_CATEGORY_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `SP_PURPOSE_ASSOC_ID` | `INTEGER` | FK → CM_SP_PURPOSE_ASSOC · NOT NULL |
| `PII_CATEGORY_ID` | `INTEGER` | FK → CM_PII_CATEGORY · NOT NULL |
| `VALIDITY` | `VARCHAR(1023)` |  |
| `IS_CONSENTED` | `BOOLEAN` | DEFAULT TRUE |

**Foreign keys**

- `SP_PURPOSE_ASSOC_ID` → [`CM_SP_PURPOSE_ASSOC`](#cm_sp_purpose_assoc) `ID`
- `PII_CATEGORY_ID` → [`CM_PII_CATEGORY`](#cm_pii_category) `ID`

## CM_SP_PURPOSE_PURPOSE_CAT_ASSC

*APIM DB (WSO2AM_DB)* · PK: `ID` · Unique: `SP_PURPOSE_ASSOC_ID, PURPOSE_CATEGORY_ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `SP_PURPOSE_ASSOC_ID` | `INTEGER` | FK → CM_SP_PURPOSE_ASSOC · NOT NULL |
| `PURPOSE_CATEGORY_ID` | `INTEGER` | FK → CM_PURPOSE_CATEGORY · NOT NULL |

**Foreign keys**

- `SP_PURPOSE_ASSOC_ID` → [`CM_SP_PURPOSE_ASSOC`](#cm_sp_purpose_assoc) `ID`
- `PURPOSE_CATEGORY_ID` → [`CM_PURPOSE_CATEGORY`](#cm_purpose_category) `ID`

