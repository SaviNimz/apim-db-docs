# Identity Server tables (3.x)

APIM 3.x embeds WSO2 Identity Server so that it can act as a key manager and handle logins. With that comes a large set of Identity Server tables, plus the remaining registry and user-management tables. APIM's own flows barely touch them, so this page gives **one line per table**. Each name links to its full column list.

!!! info "Which identity tables are core?"
    The identity tables APIM relies on (OAuth clients, tokens, scopes, service providers, users, roles and the main registry tables) are explained in full on the domain pages: [Keys & tokens](domains/keys-tokens.md), [Scopes](domains/scopes.md), [Tenants & users](domains/tenancy-users.md) and [Registry](domains/registry.md).

## IDN_* — authentication sessions

Login sessions for the portals and single sign-on. Used during login, never during API calls.

### IDN_AUTH_SESSION_STORE

Serialized authentication session objects (SSO session context), keyed by session id and type. [Columns](reference/idn.md#idn_auth_session_store)

### IDN_AUTH_TEMP_SESSION_STORE

Short-lived session data kept only while a multi-step login is in progress. [Columns](reference/idn.md#idn_auth_temp_session_store)

### IDN_AUTH_USER

A user who has an active SSO session: id, name, tenant, user-store domain and identity provider. [Columns](reference/idn.md#idn_auth_user)

### IDN_AUTH_USER_SESSION_MAPPING

Links an authenticated user (`IDN_AUTH_USER`) to their session ids. [Columns](reference/idn.md#idn_auth_user_session_mapping)

### IDN_AUTH_SESSION_APP_INFO

Which service providers (apps) a session has logged in to, and the subject used for each. [Columns](reference/idn.md#idn_auth_session_app_info)

### IDN_AUTH_SESSION_META_DATA

Name–value metadata of a session, e.g. last access time, IP address and user agent. [Columns](reference/idn.md#idn_auth_session_meta_data)

### IDN_AUTH_WAIT_STATUS

Tracks logins that are paused waiting for an external step, e.g. a long-wait or asynchronous authenticator. [Columns](reference/idn.md#idn_auth_wait_status)

### IDN_FED_AUTH_SESSION_MAPPING

Maps a federated identity provider's session index to the local session, for federated logout. [Columns](reference/idn.md#idn_fed_auth_session_mapping)

## IDN_* — OAuth extras

OAuth and OIDC features that APIM applications rarely use. The main OAuth tables are on [Keys & tokens](domains/keys-tokens.md) and [Scopes](domains/scopes.md).

### IDN_OAUTH1A_REQUEST_TOKEN

OAuth 1.0a request tokens (legacy protocol). [Columns](reference/idn.md#idn_oauth1a_request_token)

### IDN_OAUTH1A_ACCESS_TOKEN

OAuth 1.0a access tokens (legacy protocol). [Columns](reference/idn.md#idn_oauth1a_access_token)

### IDN_OAUTH2_SCOPE_VALIDATORS

Which scope validators (e.g. role-based, XACML) an OAuth client uses. FK to `IDN_OAUTH_CONSUMER_APPS`. [Columns](reference/idn.md#idn_oauth2_scope_validators)

### IDN_OAUTH2_CIBA_AUTH_CODE

Requests in the Client-Initiated Backchannel Authentication (CIBA) grant. [Columns](reference/idn.md#idn_oauth2_ciba_auth_code)

### IDN_OAUTH2_CIBA_REQUEST_SCOPES

Scopes requested in a CIBA request. [Columns](reference/idn.md#idn_oauth2_ciba_request_scopes)

### IDN_OAUTH2_DEVICE_FLOW

Requests in the device authorization grant (device code, user code, status). [Columns](reference/idn.md#idn_oauth2_device_flow)

### IDN_OAUTH2_DEVICE_FLOW_SCOPES

Scopes requested in a device-flow request. [Columns](reference/idn.md#idn_oauth2_device_flow_scopes)

### IDN_OIDC_JTI

Token ids (`jti`) of JWTs already used, e.g. JWT bearer grants or private-key-JWT client authentication, to stop replay. [Columns](reference/idn.md#idn_oidc_jti)

### IDN_OIDC_PROPERTY

OIDC settings of an OAuth client, e.g. the ID token audience and encryption options, as name–value pairs. [Columns](reference/idn.md#idn_oidc_property)

### IDN_OIDC_REQ_OBJECT_REFERENCE

An OIDC *request object* sent with an authorize request, linked to its code or token. [Columns](reference/idn.md#idn_oidc_req_object_reference)

### IDN_OIDC_REQ_OBJECT_CLAIMS

Claims requested inside an OIDC request object. [Columns](reference/idn.md#idn_oidc_req_object_claims)

### IDN_OIDC_REQ_OBJ_CLAIM_VALUES

Allowed values for a claim requested in an OIDC request object. [Columns](reference/idn.md#idn_oidc_req_obj_claim_values)

### IDN_OIDC_SCOPE_CLAIM_MAPPING

Which user claims each OIDC scope (e.g. `email`, `profile`) releases in ID tokens. [Columns](reference/idn.md#idn_oidc_scope_claim_mapping)

### IDN_STS_STORE

Tokens issued by the WS-Trust Security Token Service (SOAP). Not used by APIM APIs. [Columns](reference/idn.md#idn_sts_store)

## IDN_* — OpenID 2.0 & SAML

Stores for older single sign-on protocols.

### IDN_OPENID_ASSOCIATIONS

OpenID 2.0 associations (shared secrets with relying parties). [Columns](reference/idn.md#idn_openid_associations)

### IDN_OPENID_REMEMBER_ME

OpenID 2.0 "remember me" cookies. [Columns](reference/idn.md#idn_openid_remember_me)

### IDN_OPENID_USER_RPS

OpenID 2.0 relying parties each user has trusted. [Columns](reference/idn.md#idn_openid_user_rps)

### IDN_SAML2_ARTIFACT_STORE

SAML 2.0 artifacts waiting to be resolved (artifact binding). [Columns](reference/idn.md#idn_saml2_artifact_store)

### IDN_SAML2_ASSERTION_STORE

Issued SAML 2.0 assertions, kept for query and logout. [Columns](reference/idn.md#idn_saml2_assertion_store)

## IDN_* — UMA

User-Managed Access 2.0: resource owners sharing protected resources. Not used by APIM out of the box.

### IDN_UMA_RESOURCE

A registered UMA protected resource. [Columns](reference/idn.md#idn_uma_resource)

### IDN_UMA_RESOURCE_META_DATA

Name–value metadata of a UMA resource. [Columns](reference/idn.md#idn_uma_resource_meta_data)

### IDN_UMA_RESOURCE_SCOPE

Scopes defined on a UMA resource. [Columns](reference/idn.md#idn_uma_resource_scope)

### IDN_UMA_PERMISSION_TICKET

A UMA permission ticket issued to a client. [Columns](reference/idn.md#idn_uma_permission_ticket)

### IDN_UMA_PT_RESOURCE

Which resources a permission ticket covers. [Columns](reference/idn.md#idn_uma_pt_resource)

### IDN_UMA_PT_RESOURCE_SCOPE

Which scopes of those resources a permission ticket covers. [Columns](reference/idn.md#idn_uma_pt_resource_scope)

## IDN_* — users, claims & identity data

User-related features of Identity Server: claims, account recovery and self-service.

### IDN_BASE_TABLE

A marker table with one row (`WSO2 Identity Server`), used to detect whether the schema exists. [Columns](reference/idn.md#idn_base_table)

### IDN_CLAIM_DIALECT

A claim dialect (namespace), e.g. `http://wso2.org/claims` or the SCIM and OIDC dialects. [Columns](reference/idn.md#idn_claim_dialect)

### IDN_CLAIM

One claim URI within a dialect. [Columns](reference/idn.md#idn_claim)

### IDN_CLAIM_MAPPED_ATTRIBUTE

Which user-store attribute a local claim maps to, per user-store domain. [Columns](reference/idn.md#idn_claim_mapped_attribute)

### IDN_CLAIM_PROPERTY

Properties of a claim, e.g. display name, required, read-only. [Columns](reference/idn.md#idn_claim_property)

### IDN_CLAIM_MAPPING

Maps an external-dialect claim to a local claim. [Columns](reference/idn.md#idn_claim_mapping)

### IDN_IDENTITY_USER_DATA

Per-user identity attributes kept outside the user store, e.g. account locked, failed login attempts. [Columns](reference/idn.md#idn_identity_user_data)

### IDN_IDENTITY_META_DATA

Per-user security metadata, e.g. used one-time codes. [Columns](reference/idn.md#idn_identity_meta_data)

### IDN_RECOVERY_DATA

Password-reset and account-confirmation codes sent to users. [Columns](reference/idn.md#idn_recovery_data)

### IDN_PASSWORD_HISTORY_DATA

Hashes of users' previous passwords, to stop them reusing one. [Columns](reference/idn.md#idn_password_history_data)

### IDN_ASSOCIATED_ID

Links a local user to their identity at a federated identity provider. [Columns](reference/idn.md#idn_associated_id)

### IDN_USER_ACCOUNT_ASSOCIATION

Links several local user accounts that belong to the same person (account linking). [Columns](reference/idn.md#idn_user_account_association)

### IDN_SCIM_GROUP

SCIM attributes (id, created, location) of user-store groups. [Columns](reference/idn.md#idn_scim_group)

### IDN_THRIFT_SESSION

Sessions for the Thrift-based authentication service (legacy). [Columns](reference/idn.md#idn_thrift_session)

### IDN_CERTIFICATE

Certificates stored by Identity Server, e.g. for service providers. [Columns](reference/idn.md#idn_certificate)

### IDN_FUNCTION_LIBRARY

Reusable JavaScript functions for adaptive authentication scripts. [Columns](reference/idn.md#idn_function_library)

## IDP_* — identity providers

External (federated) identity providers, e.g. Google or a corporate SAML IdP, that users can log in with, plus the resident IdP settings.

### IDP

One identity provider: name, tenant, whether it's enabled, and its home realm. [Columns](reference/idp.md#idp)

### IDP_AUTHENTICATOR

An authenticator configured for an IdP, e.g. SAML SSO or OIDC. [Columns](reference/idp.md#idp_authenticator)

### IDP_AUTHENTICATOR_PROPERTY

Settings of an IdP authenticator, e.g. client ID and endpoint URLs. [Columns](reference/idp.md#idp_authenticator_property)

### IDP_METADATA

Name–value metadata of an IdP. [Columns](reference/idp.md#idp_metadata)

### IDP_CLAIM

Claims an IdP sends. [Columns](reference/idp.md#idp_claim)

### IDP_CLAIM_MAPPING

Maps an IdP claim to a local claim. [Columns](reference/idp.md#idp_claim_mapping)

### IDP_LOCAL_CLAIM

Local claims requested from an IdP, with default values. [Columns](reference/idp.md#idp_local_claim)

### IDP_ROLE

Roles an IdP sends. [Columns](reference/idp.md#idp_role)

### IDP_ROLE_MAPPING

Maps an IdP role to a local role. [Columns](reference/idp.md#idp_role_mapping)

### IDP_PROVISIONING_CONFIG

Outbound provisioning connector configured for an IdP. [Columns](reference/idp.md#idp_provisioning_config)

### IDP_PROV_CONFIG_PROPERTY

Settings of an IdP provisioning connector. [Columns](reference/idp.md#idp_prov_config_property)

### IDP_PROVISIONING_ENTITY

Users and groups that were provisioned to an IdP, with the remote id. [Columns](reference/idp.md#idp_provisioning_entity)

## SP_* — service providers

Settings for Identity Server service providers. APIM creates one service provider per OAuth client. [`SP_APP`](domains/keys-tokens.md#sp_app) and [`SP_INBOUND_AUTH`](domains/keys-tokens.md#sp_inbound_auth) are explained on Keys & tokens. The rest are mostly left at their defaults.

### SP_AUTH_STEP

A step in a service provider's login flow (for multi-factor login). FK to `SP_APP`. [Columns](reference/sp.md#sp_auth_step)

### SP_FEDERATED_IDP

Which identity providers and authenticators a login step can use. [Columns](reference/sp.md#sp_federated_idp)

### SP_REQ_PATH_AUTHENTICATOR

Request-path authenticators (e.g. Basic auth in the request) enabled for a service provider. [Columns](reference/sp.md#sp_req_path_authenticator)

### SP_AUTH_SCRIPT

The adaptive authentication script of a service provider. [Columns](reference/sp.md#sp_auth_script)

### SP_CLAIM_DIALECT

Which claim dialect a service provider uses. [Columns](reference/sp.md#sp_claim_dialect)

### SP_CLAIM_MAPPING

Claims a service provider requests, and how they map to local claims. [Columns](reference/sp.md#sp_claim_mapping)

### SP_ROLE_MAPPING

Maps local roles to service-provider roles. [Columns](reference/sp.md#sp_role_mapping)

### SP_PROVISIONING_CONNECTOR

Outbound provisioning connectors for a service provider. [Columns](reference/sp.md#sp_provisioning_connector)

### SP_METADATA

Name–value metadata of a service provider. [Columns](reference/sp.md#sp_metadata)

### SP_TEMPLATE

Reusable service-provider templates. [Columns](reference/sp.md#sp_template)

## CM_* — consent management

Records of what personal data users agreed to share, and for what purpose (GDPR). The script seeds one `DEFAULT` purpose and purpose category.

### CM_PII_CATEGORY

A category of personal data, e.g. email address. [Columns](reference/cm.md#cm_pii_category)

### CM_PURPOSE

A purpose for collecting data, e.g. `DEFAULT`. [Columns](reference/cm.md#cm_purpose)

### CM_PURPOSE_CATEGORY

A group of purposes. [Columns](reference/cm.md#cm_purpose_category)

### CM_PURPOSE_PII_CAT_ASSOC

Which personal-data categories a purpose covers. [Columns](reference/cm.md#cm_purpose_pii_cat_assoc)

### CM_RECEIPT

A consent receipt: one user's consent record. [Columns](reference/cm.md#cm_receipt)

### CM_CONSENT_RECEIPT_PROPERTY

Extra properties of a consent receipt. [Columns](reference/cm.md#cm_consent_receipt_property)

### CM_RECEIPT_SP_ASSOC

Which service provider a receipt is for. [Columns](reference/cm.md#cm_receipt_sp_assoc)

### CM_SP_PURPOSE_ASSOC

Which purposes a receipt's service-provider entry covers. [Columns](reference/cm.md#cm_sp_purpose_assoc)

### CM_SP_PURPOSE_PURPOSE_CAT_ASSC

Purpose categories attached to a receipt's service-provider purpose. [Columns](reference/cm.md#cm_sp_purpose_purpose_cat_assc)

### CM_SP_PURPOSE_PII_CAT_ASSOC

Personal-data categories the user consented to for that purpose, with validity. [Columns](reference/cm.md#cm_sp_purpose_pii_cat_assoc)

## FIDO — security keys

Registered hardware security keys for passwordless or second-factor login.

### FIDO_DEVICE_STORE

Registered FIDO U2F devices per user. [Columns](reference/fido.md#fido_device_store)

## FIDO2 — security keys

Registered FIDO2/WebAuthn credentials.

### FIDO2_DEVICE_STORE

Registered FIDO2/WebAuthn credentials per user: credential id, public key and signature count. [Columns](reference/fido2.md#fido2_device_store)

## REG_* — registry (other tables)

The main registry tables are on [Registry](domains/registry.md). These hold history and social features.

### REG_RESOURCE_HISTORY

Older versions of registry resources, with a `REG_DELETED` flag. It has the same columns as `REG_RESOURCE`. [Columns](reference/reg.md#reg_resource_history)

### REG_CONTENT_HISTORY

Content of older resource versions. [Columns](reference/reg.md#reg_content_history)

### REG_COMMENT

Registry-level comments. APIM uses `AM_API_COMMENTS` instead. [Columns](reference/reg.md#reg_comment)

### REG_RESOURCE_COMMENT

Links a registry comment to a resource. [Columns](reference/reg.md#reg_resource_comment)

### REG_RATING

Registry-level ratings. APIM uses `AM_API_RATINGS` instead. [Columns](reference/reg.md#reg_rating)

### REG_RESOURCE_RATING

Links a registry rating to a resource. [Columns](reference/reg.md#reg_resource_rating)

### REG_SNAPSHOT

A checkpoint (snapshot) of a collection's resource versions. [Columns](reference/reg.md#reg_snapshot)

### REG_LOG

Audit log of registry actions: path, user, action and time. [Columns](reference/reg.md#reg_log)

### REG_CLUSTER_LOCK

A lock row used so that only one node in a cluster runs a registry task at a time. [Columns](reference/reg.md#reg_cluster_lock)

## UM_* — user management (other tables)

The main user and role tables are on [Tenants & users](domains/tenancy-users.md). These cover permissions, claims, system users and user-store domains.

### UM_DOMAIN

A user-store domain, e.g. `PRIMARY` or `INTERNAL`, per tenant. Referenced by hybrid-role and permission tables. [Columns](reference/um.md#um_domain)

### UM_UUID_DOMAIN_MAPPER

Maps a user's unique id to their user-store domain. [Columns](reference/um.md#um_uuid_domain_mapper)

### UM_PERMISSION

A permission resource path plus action, e.g. `/permission/admin/manage/api/create` with `ui.execute`. [Columns](reference/um.md#um_permission)

### UM_ROLE_PERMISSION

Which roles have which permissions (allowed or denied). [Columns](reference/um.md#um_role_permission)

### UM_USER_PERMISSION

Permissions granted directly to a user. [Columns](reference/um.md#um_user_permission)

### UM_MODULE

Groups permissions into modules. [Columns](reference/um.md#um_module)

### UM_MODULE_ACTIONS

Actions available in a permission module. [Columns](reference/um.md#um_module_actions)

### UM_USER_ATTRIBUTE

Claim values of a JDBC user, per profile, e.g. email and first name. [Columns](reference/um.md#um_user_attribute)

### UM_DIALECT

Claim dialects of the user store (legacy claim model). [Columns](reference/um.md#um_dialect)

### UM_CLAIM

Claims and their attribute mappings (legacy claim model). [Columns](reference/um.md#um_claim)

### UM_CLAIM_BEHAVIOR

Per-profile claim behaviour, e.g. hidden or read-only (legacy claim model). [Columns](reference/um.md#um_claim_behavior)

### UM_PROFILE_CONFIG

User profile configurations (legacy). [Columns](reference/um.md#um_profile_config)

### UM_SYSTEM_USER

System users that aren't in the normal user store, e.g. `wso2.system.user`. [Columns](reference/um.md#um_system_user)

### UM_SYSTEM_ROLE

System roles. [Columns](reference/um.md#um_system_role)

### UM_SYSTEM_USER_ROLE

Which system users have which system roles. [Columns](reference/um.md#um_system_user_role)

### UM_SHARED_USER_ROLE

Role assignments across tenants (shared roles). [Columns](reference/um.md#um_shared_user_role)

### UM_ACCOUNT_MAPPING

Links user accounts across tenants. It has the only FK to `UM_TENANT`. [Columns](reference/um.md#um_account_mapping)

### UM_HYBRID_REMEMBER_ME

"Remember me" tokens for portal logins. [Columns](reference/um.md#um_hybrid_remember_me)
