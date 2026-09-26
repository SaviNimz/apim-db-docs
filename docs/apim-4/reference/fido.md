# FIDO_* — FIDO devices

1 tables. Generated from the 4.7.0 DDL.

## FIDO_DEVICE_STORE

*APIM DB (WSO2AM_DB)* · PK: `TENANT_ID, DOMAIN_NAME, USER_NAME, KEY_HANDLE`

| Column | Type | Notes |
|---|---|---|
| `TENANT_ID` | `INTEGER` | PK |
| `DOMAIN_NAME` | `VARCHAR(255)` | PK · NOT NULL |
| `USER_NAME` | `VARCHAR(45)` | PK · NOT NULL |
| `TIME_REGISTERED` | `TIMESTAMP` |  |
| `KEY_HANDLE` | `VARCHAR(200)` | PK · NOT NULL |
| `DEVICE_DATA` | `VARCHAR(2048)` | NOT NULL |

