# WF_* — Workflow engine

7 tables in APIM 3.2.0.

## WF_BPS_PROFILE

*APIM DB (WSO2AM_DB)* · PK: `PROFILE_NAME, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `PROFILE_NAME` | `VARCHAR(45)` | PK |
| `HOST_URL_MANAGER` | `VARCHAR(255)` |  |
| `HOST_URL_WORKER` | `VARCHAR(255)` |  |
| `USERNAME` | `VARCHAR(45)` |  |
| `PASSWORD` | `VARCHAR(1023)` |  |
| `CALLBACK_HOST` | `VARCHAR (45)` |  |
| `CALLBACK_USERNAME` | `VARCHAR (45)` |  |
| `CALLBACK_PASSWORD` | `VARCHAR (255)` |  |
| `TENANT_ID` | `INTEGER` | PK · DEFAULT -1 |

## WF_REQUEST

*APIM DB (WSO2AM_DB)* · PK: `UUID`

| Column | Type | Notes |
|---|---|---|
| `UUID` | `VARCHAR (45)` | PK |
| `CREATED_BY` | `VARCHAR (255)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |
| `OPERATION_TYPE` | `VARCHAR (50)` |  |
| `CREATED_AT` | `TIMESTAMP` |  |
| `UPDATED_AT` | `TIMESTAMP` | DEFAULT CURRENT_TIMESTAMP |
| `STATUS` | `VARCHAR (30)` |  |
| `REQUEST` | `BLOB` |  |

**Referenced by**

- [`WF_REQUEST_ENTITY_RELATIONSHIP`](#wf_request_entity_relationship) via `REQUEST_ID`
- [`WF_WORKFLOW_REQUEST_RELATION`](#wf_workflow_request_relation) via `REQUEST_ID`

## WF_REQUEST_ENTITY_RELATIONSHIP

*APIM DB (WSO2AM_DB)* · PK: `REQUEST_ID, ENTITY_NAME, ENTITY_TYPE, TENANT_ID`

| Column | Type | Notes |
|---|---|---|
| `REQUEST_ID` | `VARCHAR (45)` | PK · FK → WF_REQUEST |
| `ENTITY_NAME` | `VARCHAR (255)` | PK |
| `ENTITY_TYPE` | `VARCHAR (50)` | PK |
| `TENANT_ID` | `INTEGER` | PK · DEFAULT -1 |

**Foreign keys**

- `REQUEST_ID` → [`WF_REQUEST`](#wf_request) `UUID` (on delete: CASCADE)

## WF_WORKFLOW

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `VARCHAR (45)` | PK |
| `WF_NAME` | `VARCHAR (45)` |  |
| `DESCRIPTION` | `VARCHAR (255)` |  |
| `TEMPLATE_ID` | `VARCHAR (45)` |  |
| `IMPL_ID` | `VARCHAR (45)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Referenced by**

- [`WF_WORKFLOW_ASSOCIATION`](#wf_workflow_association) via `WORKFLOW_ID`
- [`WF_WORKFLOW_CONFIG_PARAM`](#wf_workflow_config_param) via `WORKFLOW_ID`
- [`WF_WORKFLOW_REQUEST_RELATION`](#wf_workflow_request_relation) via `WORKFLOW_ID`

## WF_WORKFLOW_ASSOCIATION

*APIM DB (WSO2AM_DB)* · PK: `ID`

| Column | Type | Notes |
|---|---|---|
| `ID` | `INTEGER` | PK · NOT NULL AUTO_INCREMENT |
| `ASSOC_NAME` | `VARCHAR (45)` |  |
| `EVENT_ID` | `VARCHAR(45)` |  |
| `ASSOC_CONDITION` | `VARCHAR (2000)` |  |
| `WORKFLOW_ID` | `VARCHAR (45)` | FK → WF_WORKFLOW |
| `IS_ENABLED` | `CHAR (1)` | DEFAULT '1' |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `WORKFLOW_ID` → [`WF_WORKFLOW`](#wf_workflow) `ID` (on delete: CASCADE)

## WF_WORKFLOW_CONFIG_PARAM

*APIM DB (WSO2AM_DB)* · PK: `WORKFLOW_ID, PARAM_NAME, PARAM_QNAME, PARAM_HOLDER`

| Column | Type | Notes |
|---|---|---|
| `WORKFLOW_ID` | `VARCHAR (45)` | PK · FK → WF_WORKFLOW |
| `PARAM_NAME` | `VARCHAR (45)` | PK |
| `PARAM_VALUE` | `VARCHAR (1000)` |  |
| `PARAM_QNAME` | `VARCHAR (45)` | PK |
| `PARAM_HOLDER` | `VARCHAR (45)` | PK |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `WORKFLOW_ID` → [`WF_WORKFLOW`](#wf_workflow) `ID` (on delete: CASCADE)

## WF_WORKFLOW_REQUEST_RELATION

*APIM DB (WSO2AM_DB)* · PK: `RELATIONSHIP_ID`

| Column | Type | Notes |
|---|---|---|
| `RELATIONSHIP_ID` | `VARCHAR (45)` | PK |
| `WORKFLOW_ID` | `VARCHAR (45)` | FK → WF_WORKFLOW |
| `REQUEST_ID` | `VARCHAR (45)` | FK → WF_REQUEST |
| `UPDATED_AT` | `TIMESTAMP` |  |
| `STATUS` | `VARCHAR (30)` |  |
| `TENANT_ID` | `INTEGER` | DEFAULT -1 |

**Foreign keys**

- `WORKFLOW_ID` → [`WF_WORKFLOW`](#wf_workflow) `ID` (on delete: CASCADE)
- `REQUEST_ID` → [`WF_REQUEST`](#wf_request) `UUID` (on delete: CASCADE)

