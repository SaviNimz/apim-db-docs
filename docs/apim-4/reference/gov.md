# GOV_* — API governance

14 tables. Generated from the 4.7.0 DDL.

## GOV_ARTIFACT

*APIM DB (WSO2AM_DB)* · PK: `ARTIFACT_KEY` · Unique: `ARTIFACT_REF_ID, ARTIFACT_TYPE, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `ARTIFACT_KEY` | `VARCHAR(36)` | PK · NOT NULL |
| `ARTIFACT_REF_ID` | `VARCHAR(36)` | NOT NULL |
| `ARTIFACT_TYPE` | `VARCHAR(32)` | NOT NULL |
| `ORGANIZATION` | `VARCHAR(128)` | NOT NULL |

**Referenced by**

- [`GOV_POLICY_RUN`](#gov_policy_run) via `ARTIFACT_KEY`
- [`GOV_RULESET_RUN`](#gov_ruleset_run) via `ARTIFACT_KEY`

## GOV_POLICY

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID` · Unique: `NAME, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `VARCHAR(36)` | PK · NOT NULL |
| `NAME` | `VARCHAR(256)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1024)` |  |
| `ORGANIZATION` | `VARCHAR(128)` | NOT NULL |
| `CREATED_BY` | `VARCHAR(256)` |  |
| `CREATED_TIME` | `DATETIME` | DEFAULT CURRENT_TIMESTAMP |
| `UPDATED_BY` | `VARCHAR(256)` |  |
| `LAST_UPDATED_TIME` | `DATETIME` |  |
| `IS_GLOBAL` | `INT` | DEFAULT 0 |

**Referenced by**

- [`GOV_POLICY_GOVERNABLE_STATE`](#gov_policy_governable_state) via `POLICY_ID`
- [`GOV_POLICY_LABEL`](#gov_policy_label) via `POLICY_ID`
- [`GOV_POLICY_RULESET`](#gov_policy_ruleset) via `POLICY_ID`
- [`GOV_POLICY_RUN`](#gov_policy_run) via `POLICY_ID`
- [`GOV_REQUEST_POLICY`](#gov_request_policy) via `POLICY_ID`

## GOV_POLICY_ACTION

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID, STATE, SEVERITY, TYPE`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `VARCHAR(36)` | PK · FK → GOV_POLICY_GOVERNABLE_STATE · NOT NULL |
| `STATE` | `VARCHAR(128)` | PK · FK → GOV_POLICY_GOVERNABLE_STATE · NOT NULL |
| `SEVERITY` | `VARCHAR(32)` | PK · NOT NULL |
| `TYPE` | `VARCHAR(32)` | PK · NOT NULL |

**Foreign keys**

- `POLICY_ID, STATE` → [`GOV_POLICY_GOVERNABLE_STATE`](#gov_policy_governable_state) `POLICY_ID, STATE`

## GOV_POLICY_GOVERNABLE_STATE

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID, STATE`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `VARCHAR(36)` | PK · FK → GOV_POLICY · NOT NULL |
| `STATE` | `VARCHAR(128)` | PK · NOT NULL |

**Foreign keys**

- `POLICY_ID` → [`GOV_POLICY`](#gov_policy) `POLICY_ID`

**Referenced by**

- [`GOV_POLICY_ACTION`](#gov_policy_action) via `POLICY_ID, STATE`

## GOV_POLICY_LABEL

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID, LABEL`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `VARCHAR(36)` | PK · FK → GOV_POLICY · NOT NULL |
| `LABEL` | `VARCHAR(128)` | PK · NOT NULL |

**Foreign keys**

- `POLICY_ID` → [`GOV_POLICY`](#gov_policy) `POLICY_ID`

## GOV_POLICY_RULESET

*APIM DB (WSO2AM_DB)* · PK: `POLICY_ID, RULESET_ID`

| Column | Type | Notes |
|---|---|---|
| `POLICY_ID` | `VARCHAR(36)` | PK · FK → GOV_POLICY · NOT NULL |
| `RULESET_ID` | `VARCHAR(36)` | PK · FK → GOV_RULESET · NOT NULL |

**Foreign keys**

- `POLICY_ID` → [`GOV_POLICY`](#gov_policy) `POLICY_ID`
- `RULESET_ID` → [`GOV_RULESET`](#gov_ruleset) `RULESET_ID`

## GOV_POLICY_RUN

*APIM DB (WSO2AM_DB)* · PK: `ARTIFACT_KEY, POLICY_ID`

| Column | Type | Notes |
|---|---|---|
| `ARTIFACT_KEY` | `VARCHAR(36)` | PK · FK → GOV_ARTIFACT · NOT NULL |
| `POLICY_ID` | `VARCHAR(36)` | PK · FK → GOV_POLICY · NOT NULL |
| `RUN_TIMESTAMP` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP |

**Foreign keys**

- `ARTIFACT_KEY` → [`GOV_ARTIFACT`](#gov_artifact) `ARTIFACT_KEY`
- `POLICY_ID` → [`GOV_POLICY`](#gov_policy) `POLICY_ID`

## GOV_REQUEST

*APIM DB (WSO2AM_DB)* · PK: `REQ_ID` · Unique: `STATUS, ARTIFACT_KEY`

| Column | Type | Notes |
|---|---|---|
| `REQ_ID` | `VARCHAR(36)` | PK · NOT NULL |
| `ARTIFACT_KEY` | `VARCHAR(36)` | NOT NULL |
| `STATUS` | `VARCHAR(32)` | NOT NULL DEFAULT 'PENDING' |
| `REQ_TIMESTAMP` | `DATETIME` | DEFAULT CURRENT_TIMESTAMP |
| `PROCESSING_TIMESTAMP` | `DATETIME` |  |

**Referenced by**

- [`GOV_REQUEST_POLICY`](#gov_request_policy) via `REQ_ID`

## GOV_REQUEST_POLICY

*APIM DB (WSO2AM_DB)* · PK: `REQ_ID, POLICY_ID`

| Column | Type | Notes |
|---|---|---|
| `REQ_ID` | `VARCHAR(36)` | PK · FK → GOV_REQUEST · NOT NULL |
| `POLICY_ID` | `VARCHAR(36)` | PK · FK → GOV_POLICY · NOT NULL |

**Foreign keys**

- `REQ_ID` → [`GOV_REQUEST`](#gov_request) `REQ_ID`
- `POLICY_ID` → [`GOV_POLICY`](#gov_policy) `POLICY_ID`

## GOV_RULESET

*APIM DB (WSO2AM_DB)* · PK: `RULESET_ID` · Unique: `NAME, ORGANIZATION`

| Column | Type | Notes |
|---|---|---|
| `RULESET_ID` | `VARCHAR(36)` | PK · NOT NULL |
| `NAME` | `VARCHAR(256)` | NOT NULL |
| `DESCRIPTION` | `VARCHAR(1024)` |  |
| `ARTIFACT_TYPE` | `VARCHAR(128)` | NOT NULL |
| `RULE_CATEGORY` | `VARCHAR(128)` | NOT NULL |
| `RULE_TYPE` | `VARCHAR(128)` | NOT NULL |
| `DOCUMENTATION_LINK` | `VARCHAR(1024)` |  |
| `PROVIDER` | `VARCHAR(256)` |  |
| `ORGANIZATION` | `VARCHAR(128)` | NOT NULL |
| `CREATED_BY` | `VARCHAR(256)` |  |
| `CREATED_TIME` | `DATETIME` | DEFAULT CURRENT_TIMESTAMP |
| `UPDATED_BY` | `VARCHAR(256)` |  |
| `LAST_UPDATED_TIME` | `DATETIME` |  |

**Referenced by**

- [`GOV_POLICY_RULESET`](#gov_policy_ruleset) via `RULESET_ID`
- [`GOV_RULESET_CONTENT`](#gov_ruleset_content) via `RULESET_ID`
- [`GOV_RULESET_RULE`](#gov_ruleset_rule) via `RULESET_ID`
- [`GOV_RULESET_RUN`](#gov_ruleset_run) via `RULESET_ID`

## GOV_RULESET_CONTENT

*APIM DB (WSO2AM_DB)* · PK: `RULESET_ID`

| Column | Type | Notes |
|---|---|---|
| `RULESET_ID` | `VARCHAR(36)` | PK · FK → GOV_RULESET · NOT NULL |
| `CONTENT` | `LONGBLOB` | NOT NULL |
| `CONTENT_TYPE` | `VARCHAR(128)` |  |
| `FILE_NAME` | `VARCHAR(256)` |  |

**Foreign keys**

- `RULESET_ID` → [`GOV_RULESET`](#gov_ruleset) `RULESET_ID`

## GOV_RULESET_RULE

*APIM DB (WSO2AM_DB)* · PK: `RULESET_RULE_ID` · Unique: `RULESET_ID, RULE_NAME`

| Column | Type | Notes |
|---|---|---|
| `RULESET_RULE_ID` | `VARCHAR(36)` | PK · NOT NULL |
| `RULESET_ID` | `VARCHAR(36)` | FK → GOV_RULESET · NOT NULL |
| `RULE_NAME` | `VARCHAR(256)` | NOT NULL |
| `RULE_DESCRIPTION` | `VARCHAR(1024)` |  |
| `SEVERITY` | `VARCHAR(32)` | NOT NULL |
| `RULE_CONTENT` | `BLOB` | NOT NULL |

**Foreign keys**

- `RULESET_ID` → [`GOV_RULESET`](#gov_ruleset) `RULESET_ID`

**Referenced by**

- [`GOV_RULE_VIOLATION`](#gov_rule_violation) via `RULESET_ID, RULE_NAME`

## GOV_RULESET_RUN

*APIM DB (WSO2AM_DB)* · PK: `RULESET_RUN_ID` · Unique: `ARTIFACT_KEY, RULESET_ID`

| Column | Type | Notes |
|---|---|---|
| `RULESET_RUN_ID` | `VARCHAR(36)` | PK · NOT NULL |
| `ARTIFACT_KEY` | `VARCHAR(36)` | FK → GOV_ARTIFACT · NOT NULL |
| `RULESET_ID` | `VARCHAR(36)` | FK → GOV_RULESET · NOT NULL |
| `RESULT` | `INT` | NOT NULL |
| `RUN_TIMESTAMP` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP |

**Foreign keys**

- `ARTIFACT_KEY` → [`GOV_ARTIFACT`](#gov_artifact) `ARTIFACT_KEY`
- `RULESET_ID` → [`GOV_RULESET`](#gov_ruleset) `RULESET_ID`

**Referenced by**

- [`GOV_RULE_VIOLATION`](#gov_rule_violation) via `RULESET_RUN_ID`

## GOV_RULE_VIOLATION

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR(36)` | PK · NOT NULL |
| `RULESET_RUN_ID` | `VARCHAR(36)` | FK → GOV_RULESET_RUN · NOT NULL |
| `RULESET_ID` | `VARCHAR(36)` | FK → GOV_RULESET_RULE · NOT NULL |
| `RULE_NAME` | `VARCHAR(256)` | FK → GOV_RULESET_RULE · NOT NULL |
| `MESSAGE` | `VARCHAR(1024)` |  |
| `VIOLATED_PATH` | `VARCHAR(1024)` | NOT NULL |

**Foreign keys**

- `RULESET_RUN_ID` → [`GOV_RULESET_RUN`](#gov_ruleset_run) `RULESET_RUN_ID`
- `RULESET_ID, RULE_NAME` → [`GOV_RULESET_RULE`](#gov_ruleset_rule) `RULESET_ID, RULE_NAME`

