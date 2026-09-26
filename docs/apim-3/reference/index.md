# Table reference

Every table in the WSO2 API Manager **3.2.0** databases, grouped by name prefix. Each entry lists the table's columns, keys and relationships. The domain pages explain what each table is for.

!!! info "How to read a table entry"
    - **PK** is the primary key. **Unique** lists other column sets that must be unique.
    - **Foreign keys** are relationships the database enforces.
    - **Related tables (not enforced)** are tables that APIM links to by value. The database doesn't enforce these links with a foreign key.

**200 tables** in total.

| Prefix | Tables | Database |
|---|---|---|
| [AM_* — API Manager core](am.md) | 57 | APIM DB (WSO2AM_DB) |
| [CM_* — Consent management](cm.md) | 10 | APIM DB (WSO2AM_DB) |
| [FIDO_* — FIDO devices](fido.md) | 1 | APIM DB (WSO2AM_DB) |
| [FIDO2_* — FIDO2 devices](fido2.md) | 1 | APIM DB (WSO2AM_DB) |
| [IDN_* — Identity & OAuth](idn.md) | 59 | APIM DB (WSO2AM_DB) |
| [IDP_* — Identity providers](idp.md) | 12 | APIM DB (WSO2AM_DB) |
| [REG_* — Registry](reg.md) | 17 | Shared DB (WSO2SHARED_DB) |
| [SP_* — Service providers](sp.md) | 12 | APIM DB (WSO2AM_DB) |
| [UM_* — Users, roles, tenants](um.md) | 24 | Shared DB (WSO2SHARED_DB) |
| [WF_* — Workflow engine](wf.md) | 7 | APIM DB (WSO2AM_DB) |
