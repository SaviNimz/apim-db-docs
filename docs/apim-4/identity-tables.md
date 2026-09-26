# Identity Server tables

!!! abstract "In one sentence"
    APIM 4.7.0 embeds WSO2 Identity Server (IS) components, mainly for its built-in Resident Key Manager, and the platform's user store and registry. Those components bring many tables that APIM's own flows barely touch. They're listed here, one line each, so that **every table is accounted for**.

The IS tables that APIM *does* rely on are explained on the domain pages:

- OAuth clients, tokens and service providers: [Keys & tokens](domains/keys-tokens.md)
- OAuth scopes: [Scopes](domains/scopes.md)
- Revocation: [Revocation](domains/revocation.md)
- Users, roles, tenants and organizations: [Tenants & users](domains/tenancy-users.md)
- The main registry tables: [Registry](domains/registry.md)
- The workflow engine: [Workflows](domains/workflows.md)

Everything below is **peripheral**: it's used by IS features such as SSO, SAML, consent or account recovery. Most of it stays empty in a typical APIM deployment. Each entry links to its full column list.

## OAuth & OpenID Connect extras

### IDN_OAUTH1A_REQUEST_TOKEN
OAuth 1.0a request tokens (legacy protocol). FK to `IDN_OAUTH_CONSUMER_APPS`. [Columns](reference/idn.md#idn_oauth1a_request_token)

### IDN_OAUTH1A_ACCESS_TOKEN
OAuth 1.0a access tokens (legacy protocol). FK to `IDN_OAUTH_CONSUMER_APPS`. [Columns](reference/idn.md#idn_oauth1a_access_token)

### IDN_OAUTH2_CIBA_AUTH_CODE
Pending requests for the CIBA grant, where the user approves the login on a separate device. [Columns](reference/idn.md#idn_oauth2_ciba_auth_code)

### IDN_OAUTH2_CIBA_REQUEST_SCOPES
Scopes requested in a CIBA request. [Columns](reference/idn.md#idn_oauth2_ciba_request_scopes)

### IDN_OAUTH2_DEVICE_FLOW
Device-code grant requests (e.g. a smart TV shows a code for the user to enter elsewhere). [Columns](reference/idn.md#idn_oauth2_device_flow)

### IDN_OAUTH2_DEVICE_FLOW_SCOPES
Scopes requested in a device-flow request. [Columns](reference/idn.md#idn_oauth2_device_flow_scopes)

### IDN_OAUTH2_SCOPE_VALIDATORS
Which scope validators (e.g. role-based) are enabled for each OAuth client (`APP_ID` → `IDN_OAUTH_CONSUMER_APPS.ID`). [Columns](reference/idn.md#idn_oauth2_scope_validators)

### IDN_OAUTH2_TOKEN_BINDING
Binds a token to a client property such as a cookie or certificate, so a stolen token can't be reused. [Columns](reference/idn.md#idn_oauth2_token_binding)

### IDN_OAUTH2_USER_CONSENT
A user's recorded consent for an OAuth app. [Columns](reference/idn.md#idn_oauth2_user_consent)

### IDN_OAUTH2_USER_CONSENTED_SCOPES
The scopes covered by a user's consent. [Columns](reference/idn.md#idn_oauth2_user_consented_scopes)

### IDN_OIDC_PROPERTY
Extra OpenID Connect settings per OAuth client (`CONSUMER_KEY`), e.g. ID-token encryption and logout URLs. [Columns](reference/idn.md#idn_oidc_property)

### IDN_OIDC_JTI
Remembers used JWT IDs, to stop replay of signed request objects and client assertions. [Columns](reference/idn.md#idn_oidc_jti)

### IDN_OIDC_REQ_OBJECT_REFERENCE
Links an OIDC *request object* to the authorization code or token it produced. [Columns](reference/idn.md#idn_oidc_req_object_reference)

### IDN_OIDC_REQ_OBJECT_CLAIMS
Claims asked for in an OIDC request object. [Columns](reference/idn.md#idn_oidc_req_object_claims)

### IDN_OIDC_REQ_OBJ_CLAIM_VALUES
Requested values for those claims. [Columns](reference/idn.md#idn_oidc_req_obj_claim_values)

### IDN_OIDC_SCOPE_CLAIM_MAPPING
Which user claims each OIDC scope releases (e.g. `email` → the email claim). [Columns](reference/idn.md#idn_oidc_scope_claim_mapping)

## Sessions & authentication

### IDN_AUTH_SESSION_STORE
Serialized single-sign-on (SSO) login sessions. [Columns](reference/idn.md#idn_auth_session_store)

### IDN_AUTH_TEMP_SESSION_STORE
Short-lived authentication context used during a login. [Columns](reference/idn.md#idn_auth_temp_session_store)

### IDN_AUTH_SESSION_APP_INFO
Which applications take part in an SSO session. [Columns](reference/idn.md#idn_auth_session_app_info)

### IDN_AUTH_SESSION_META_DATA
Session metadata, such as the user agent and IP address. [Columns](reference/idn.md#idn_auth_session_meta_data)

### IDN_AUTH_USER
Users who have SSO sessions (local or federated). [Columns](reference/idn.md#idn_auth_user)

### IDN_AUTH_USER_SESSION_MAPPING
Maps users to their SSO sessions, e.g. to terminate all of a user's sessions. [Columns](reference/idn.md#idn_auth_user_session_mapping)

### IDN_AUTH_WAIT_STATUS
Status of long-running (asynchronous) login steps. [Columns](reference/idn.md#idn_auth_wait_status)

### IDN_FED_AUTH_SESSION_MAPPING
Maps a federated identity provider's session to the local session, for single logout. [Columns](reference/idn.md#idn_fed_auth_session_mapping)

### IDN_THRIFT_SESSION
Sessions for the legacy Thrift-based authentication service. [Columns](reference/idn.md#idn_thrift_session)

### IDN_STS_STORE
Tokens issued by the WS-Trust Security Token Service (legacy SOAP security). [Columns](reference/idn.md#idn_sts_store)

## SAML & OpenID 2.0

### IDN_SAML2_ASSERTION_STORE
Stored SAML2 assertions. [Columns](reference/idn.md#idn_saml2_assertion_store)

### IDN_SAML2_ARTIFACT_STORE
SAML2 artifacts for artifact-binding SSO. [Columns](reference/idn.md#idn_saml2_artifact_store)

### IDN_OPENID_ASSOCIATIONS
OpenID 2.0 association handles (legacy). [Columns](reference/idn.md#idn_openid_associations)

### IDN_OPENID_REMEMBER_ME
OpenID 2.0 "remember me" cookies (legacy). [Columns](reference/idn.md#idn_openid_remember_me)

### IDN_OPENID_USER_RPS
Relying parties each user has visited with OpenID 2.0 (legacy). [Columns](reference/idn.md#idn_openid_user_rps)

## Claims

### IDN_CLAIM_DIALECT
Claim dialects (namespaces), such as local, OIDC and SCIM. [Columns](reference/idn.md#idn_claim_dialect)

### IDN_CLAIM
Claims, each in a dialect. FK to `IDN_CLAIM_DIALECT`. [Columns](reference/idn.md#idn_claim)

### IDN_CLAIM_MAPPED_ATTRIBUTE
Which user-store attribute backs each local claim. [Columns](reference/idn.md#idn_claim_mapped_attribute)

### IDN_CLAIM_PROPERTY
Properties of local claims, such as display name and whether it's required. [Columns](reference/idn.md#idn_claim_property)

### IDN_CLAIM_MAPPING
Maps external-dialect claims to local claims. [Columns](reference/idn.md#idn_claim_mapping)

## User account management

### IDN_IDENTITY_USER_DATA
Key/value identity data per user, such as account-lock state and failed-login counts. [Columns](reference/idn.md#idn_identity_user_data)

### IDN_IDENTITY_META_DATA
Identity metadata per user, such as confirmation codes. [Columns](reference/idn.md#idn_identity_meta_data)

### IDN_RECOVERY_DATA
Password-reset and account-recovery codes in progress. [Columns](reference/idn.md#idn_recovery_data)

### IDN_PASSWORD_HISTORY_DATA
Previous password hashes, to stop users reusing a password. [Columns](reference/idn.md#idn_password_history_data)

### IDN_ASSOCIATED_ID
Links a local user to their identity at a federated IdP. [Columns](reference/idn.md#idn_associated_id)

### IDN_USER_ACCOUNT_ASSOCIATION
Links several local accounts that belong to the same person. [Columns](reference/idn.md#idn_user_account_association)

### IDN_USER_FUNCTIONALITY_MAPPING
Per-user locks on specific functions, such as a locked OTP login. [Columns](reference/idn.md#idn_user_functionality_mapping)

### IDN_USER_FUNCTIONALITY_PROPERTY
Properties of those per-user function locks. [Columns](reference/idn.md#idn_user_functionality_property)

### IDN_SCIM_GROUP
SCIM attributes of groups and roles. [Columns](reference/idn.md#idn_scim_group)

## User-managed access (UMA)

### IDN_UMA_RESOURCE
Resources registered for UMA 2.0 (user-managed access). [Columns](reference/idn.md#idn_uma_resource)

### IDN_UMA_RESOURCE_META_DATA
Metadata of UMA resources. [Columns](reference/idn.md#idn_uma_resource_meta_data)

### IDN_UMA_RESOURCE_SCOPE
Scopes of UMA resources. [Columns](reference/idn.md#idn_uma_resource_scope)

### IDN_UMA_PERMISSION_TICKET
UMA permission tickets. [Columns](reference/idn.md#idn_uma_permission_ticket)

### IDN_UMA_PT_RESOURCE
Resources covered by a permission ticket. [Columns](reference/idn.md#idn_uma_pt_resource)

### IDN_UMA_PT_RESOURCE_SCOPE
Scopes covered by a permission ticket. [Columns](reference/idn.md#idn_uma_pt_resource_scope)

## Configuration, secrets & misc

### IDN_BASE_TABLE
A marker row (`PRODUCT_NAME`) showing that the identity schema has been created. [Columns](reference/idn.md#idn_base_table)

### IDN_CONFIG_TYPE
Types of configuration resources in the IS configuration store. [Columns](reference/idn.md#idn_config_type)

### IDN_CONFIG_RESOURCE
Configuration resources, e.g. email-sender settings. FK to `IDN_CONFIG_TYPE`. [Columns](reference/idn.md#idn_config_resource)

### IDN_CONFIG_ATTRIBUTE
Key/value attributes of a configuration resource. [Columns](reference/idn.md#idn_config_attribute)

### IDN_CONFIG_FILE
Files attached to a configuration resource. [Columns](reference/idn.md#idn_config_file)

### IDN_SECRET_TYPE
Types of stored secrets. [Columns](reference/idn.md#idn_secret_type)

### IDN_SECRET
Encrypted secrets used by IS features. [Columns](reference/idn.md#idn_secret)

### IDN_REMOTE_FETCH_CONFIG
Settings for pulling IS configuration from a remote repository (e.g. Git). [Columns](reference/idn.md#idn_remote_fetch_config)

### IDN_REMOTE_FETCH_REVISIONS
Deployment history of remotely fetched configuration files. [Columns](reference/idn.md#idn_remote_fetch_revisions)

### IDN_FUNCTION_LIBRARY
Reusable script functions for adaptive-authentication scripts. [Columns](reference/idn.md#idn_function_library)

### IDN_CERTIFICATE
Certificates stored by IS, e.g. for applications. [Columns](reference/idn.md#idn_certificate)

### IDN_CORS_ORIGIN
Allowed CORS origins per tenant. [Columns](reference/idn.md#idn_cors_origin)

### IDN_CORS_ASSOCIATION
Which service provider allows which CORS origin. [Columns](reference/idn.md#idn_cors_association)

## Service providers (other SP tables)

### SP_AUTH_STEP
Login steps configured for a service provider. FK to `SP_APP`. [Columns](reference/sp.md#sp_auth_step)

### SP_FEDERATED_IDP
Federated authenticators used in a login step. FK to `SP_AUTH_STEP`. [Columns](reference/sp.md#sp_federated_idp)

### SP_AUTH_SCRIPT
Adaptive-authentication script of a service provider. [Columns](reference/sp.md#sp_auth_script)

### SP_CLAIM_DIALECT
Claim dialects a service provider uses. FK to `SP_APP`. [Columns](reference/sp.md#sp_claim_dialect)

### SP_CLAIM_MAPPING
Claim mappings requested by a service provider. FK to `SP_APP`. [Columns](reference/sp.md#sp_claim_mapping)

### SP_ROLE_MAPPING
Role mappings for a service provider. FK to `SP_APP`. [Columns](reference/sp.md#sp_role_mapping)

### SP_REQ_PATH_AUTHENTICATOR
Request-path authenticators (e.g. Basic auth in the request) for a service provider. [Columns](reference/sp.md#sp_req_path_authenticator)

### SP_PROVISIONING_CONNECTOR
Outbound provisioning connectors for a service provider. [Columns](reference/sp.md#sp_provisioning_connector)

### SP_METADATA
Key/value metadata of a service provider. [Columns](reference/sp.md#sp_metadata)

### SP_TEMPLATE
Service-provider templates. [Columns](reference/sp.md#sp_template)

### SP_SHARED_APP
Applications shared from a parent organization with a sub-organization. [Columns](reference/sp.md#sp_shared_app)

## Identity providers

### IDP
Identity providers (federated login sources), per tenant. [Columns](reference/idp.md#idp)

### IDP_AUTHENTICATOR
Authenticators (e.g. OIDC or SAML) configured for an IdP. [Columns](reference/idp.md#idp_authenticator)

### IDP_AUTHENTICATOR_PROPERTY
Settings of an IdP authenticator. [Columns](reference/idp.md#idp_authenticator_property)

### IDP_METADATA
Key/value metadata of an IdP. [Columns](reference/idp.md#idp_metadata)

### IDP_CLAIM
Claims an IdP sends. [Columns](reference/idp.md#idp_claim)

### IDP_CLAIM_MAPPING
Maps IdP claims to local claims. [Columns](reference/idp.md#idp_claim_mapping)

### IDP_LOCAL_CLAIM
Local claims requested from an IdP. [Columns](reference/idp.md#idp_local_claim)

### IDP_ROLE
Roles an IdP sends. [Columns](reference/idp.md#idp_role)

### IDP_ROLE_MAPPING
Maps IdP roles to local roles. [Columns](reference/idp.md#idp_role_mapping)

### IDP_PROVISIONING_CONFIG
Outbound provisioning settings of an IdP. [Columns](reference/idp.md#idp_provisioning_config)

### IDP_PROV_CONFIG_PROPERTY
Properties of an IdP provisioning connector. [Columns](reference/idp.md#idp_prov_config_property)

### IDP_PROVISIONING_ENTITY
Users and groups provisioned to an IdP, with their remote IDs. [Columns](reference/idp.md#idp_provisioning_entity)

## Consent management

### CM_PII_CATEGORY
Categories of personal data (PII). [Columns](reference/cm.md#cm_pii_category)

### CM_PURPOSE
Purposes for which personal data is collected. [Columns](reference/cm.md#cm_purpose)

### CM_PURPOSE_CATEGORY
Groups of purposes. [Columns](reference/cm.md#cm_purpose_category)

### CM_PURPOSE_PII_CAT_ASSOC
Which PII categories each purpose uses. [Columns](reference/cm.md#cm_purpose_pii_cat_assoc)

### CM_RECEIPT
Consent receipts: a record that a person gave consent. [Columns](reference/cm.md#cm_receipt)

### CM_CONSENT_RECEIPT_PROPERTY
Extra properties of a consent receipt. [Columns](reference/cm.md#cm_consent_receipt_property)

### CM_RECEIPT_SP_ASSOC
The service providers covered by a receipt. [Columns](reference/cm.md#cm_receipt_sp_assoc)

### CM_SP_PURPOSE_ASSOC
Purposes agreed for a service provider in a receipt. [Columns](reference/cm.md#cm_sp_purpose_assoc)

### CM_SP_PURPOSE_PURPOSE_CAT_ASSC
Purpose categories of those purposes. [Columns](reference/cm.md#cm_sp_purpose_purpose_cat_assc)

### CM_SP_PURPOSE_PII_CAT_ASSOC
The PII categories consented to for a purpose. [Columns](reference/cm.md#cm_sp_purpose_pii_cat_assoc)

## FIDO

### FIDO_DEVICE_STORE
Registered U2F (FIDO 1) security keys. [Columns](reference/fido.md#fido_device_store)

### FIDO2_DEVICE_STORE
Registered FIDO2 / WebAuthn authenticators (passkeys). [Columns](reference/fido2.md#fido2_device_store)

## User store: other tables

### UM_DOMAIN
User-store domains per tenant, such as `PRIMARY` and `INTERNAL`. [Columns](reference/um.md#um_domain)

### UM_SYSTEM_USER
Internal system users. [Columns](reference/um.md#um_system_user)

### UM_SYSTEM_ROLE
Internal system roles. [Columns](reference/um.md#um_system_role)

### UM_SYSTEM_USER_ROLE
System-user role assignments. [Columns](reference/um.md#um_system_user_role)

### UM_HYBRID_GROUP_ROLE
Internal roles assigned to groups. [Columns](reference/um.md#um_hybrid_group_role)

### UM_HYBRID_REMEMBER_ME
"Remember me" login cookies. [Columns](reference/um.md#um_hybrid_remember_me)

### UM_SHARED_USER_ROLE
Cross-tenant shared-role assignments. [Columns](reference/um.md#um_shared_user_role)

### UM_PERMISSION
Permission resources and actions (e.g. `/permission/admin/manage/api/publish`). [Columns](reference/um.md#um_permission)

### UM_ROLE_PERMISSION
Which permissions each role has. [Columns](reference/um.md#um_role_permission)

### UM_USER_PERMISSION
Permissions granted directly to a user. [Columns](reference/um.md#um_user_permission)

### UM_MODULE
Permission modules. [Columns](reference/um.md#um_module)

### UM_MODULE_ACTIONS
Actions available in a permission module. [Columns](reference/um.md#um_module_actions)

### UM_USER_ATTRIBUTE
User profile attributes (email, first name and so on) in the JDBC user store. [Columns](reference/um.md#um_user_attribute)

### UM_DIALECT
Claim dialects in the user store (legacy claim model). [Columns](reference/um.md#um_dialect)

### UM_CLAIM
Claims in the user store (legacy claim model). [Columns](reference/um.md#um_claim)

### UM_PROFILE_CONFIG
User profile configurations. [Columns](reference/um.md#um_profile_config)

### UM_CLAIM_BEHAVIOR
How each claim behaves in each profile. [Columns](reference/um.md#um_claim_behavior)

### UM_ACCOUNT_MAPPING
Links between user accounts. [Columns](reference/um.md#um_account_mapping)

### UM_UUID_DOMAIN_MAPPER
Maps user UUIDs to their user-store domain. [Columns](reference/um.md#um_uuid_domain_mapper)

### UM_GROUP_UUID_DOMAIN_MAPPER
Maps group UUIDs to their user-store domain. [Columns](reference/um.md#um_group_uuid_domain_mapper)

## Registry: other tables

### REG_CONTENT_HISTORY
Content of older resource versions. [Columns](reference/reg.md#reg_content_history)

### REG_RESOURCE_HISTORY
Older versions of registry resources. [Columns](reference/reg.md#reg_resource_history)

### REG_SNAPSHOT
Snapshots of a resource's version set. [Columns](reference/reg.md#reg_snapshot)

### REG_COMMENT
Comments on registry resources (not the Developer Portal comments, which are in `AM_API_COMMENTS`). [Columns](reference/reg.md#reg_comment)

### REG_RESOURCE_COMMENT
Links comments to resources. [Columns](reference/reg.md#reg_resource_comment)

### REG_RATING
Ratings of registry resources. [Columns](reference/reg.md#reg_rating)

### REG_RESOURCE_RATING
Links ratings to resources. [Columns](reference/reg.md#reg_resource_rating)

### REG_TAG
Tags. APIM stores **API tags** here. [Columns](reference/reg.md#reg_tag)

### REG_RESOURCE_TAG
Links tags to resources, for example tags to an API artifact. [Columns](reference/reg.md#reg_resource_tag)

### REG_LOG
An audit log of registry changes. [Columns](reference/reg.md#reg_log)

### REG_CLUSTER_LOCK
A lock used while the registry schema is being initialized. [Columns](reference/reg.md#reg_cluster_lock)
