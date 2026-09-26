# Table reference

Every table defined in the APIM **4.7.0** database scripts, grouped by name prefix. These pages are generated from `dbscripts/**/mysql.sql`, so they list every column and key. Each table's purpose is explained on the domain pages.

!!! info "How to read a table entry"
    - **PK** is the primary key. **Unique** lists other column sets that must be unique.
    - **Foreign keys** are relationships the database enforces.
    - **Likely links (no FK)** are joins the application makes in code but the database does not enforce. They're inferred from column names, so treat them as hints.

**298 tables** in total.

| Prefix | Tables | Database |
|---|---|---|
| [AM_* — API Manager core](am.md) | 112 | APIM DB (WSO2AM_DB) |
| [CM_* — Consent management](cm.md) | 10 | APIM DB (WSO2AM_DB) |
| [FIDO_* — FIDO devices](fido.md) | 1 | APIM DB (WSO2AM_DB) |
| [FIDO2_* — FIDO2 devices](fido2.md) | 1 | APIM DB (WSO2AM_DB) |
| [GOV_* — API governance](gov.md) | 14 | APIM DB (WSO2AM_DB) |
| [IDN_* — Identity & OAuth](idn.md) | 77 | APIM DB (WSO2AM_DB) |
| [IDP_* — Identity providers](idp.md) | 12 | APIM DB (WSO2AM_DB) |
| [REG_* — Registry](reg.md) | 17 | Shared DB (WSO2SHARED_DB) |
| [SP_* — Service providers](sp.md) | 13 | APIM DB (WSO2AM_DB) |
| [UM_* — Users, roles, tenants](um.md) | 34 | Shared DB (WSO2SHARED_DB) |
| [WF_* — Workflow engine](wf.md) | 7 | APIM DB (WSO2AM_DB) |
