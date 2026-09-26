# Approval workflows

!!! abstract "What happens"
    An admin can put an approval step in front of certain actions, such as creating an application or subscribing to an API. When someone performs the action, APIM saves it in a "waiting" state and records a **workflow** row in `AM_WORKFLOWS`. When an approver approves or rejects it in the Admin Portal, APIM finishes (or cancels) the original action.

**Who:** The person doing the action, then an approver (Admin Portal) · **Tables written:** [`AM_WORKFLOWS`](../reference/am.md#am_workflows), plus the status column of the gated table · **Tables read:** the gated table

## The flow at a glance

This diagram uses subscription approval as the example. The other workflow types follow the same pattern.

```mermaid
sequenceDiagram
    actor Dev as Developer
    participant Portal as Dev Portal
    participant DB as APIM DB
    actor Approver
    participant Admin as Admin Portal
    Dev->>Portal: Subscribe (Gold)
    Portal->>DB: insert AM_SUBSCRIPTION (ON_HOLD)
    Portal->>DB: insert AM_WORKFLOWS (CREATED)
    Approver->>Admin: Approve task
    Admin->>DB: update AM_WORKFLOWS (APPROVED)
    Admin->>DB: update AM_SUBSCRIPTION (UNBLOCKED)
```

- The gated row always exists *before* approval, so the workflow row can point at it.
- If there's no workflow configured, the "simple" executor approves instantly, and no row may be kept.

## Step by step

1. **The action is saved "pending".** The gated table gets its row with a waiting status, e.g. `AM_SUBSCRIPTION.SUB_STATUS = 'ON_HOLD'` or `AM_APPLICATION.APPLICATION_STATUS = 'CREATED'`.

2. **Workflow row.** One row goes into [`AM_WORKFLOWS`](../reference/am.md#am_workflows):
    - `WF_TYPE` says *what* is waiting (see the table below).
    - `WF_REFERENCE` is the id of the waiting thing.
    - `WF_STATUS` is `CREATED`, then `APPROVED` or `REJECTED`.
    - `WF_EXTERNAL_REFERENCE` is a unique id used by the approval engine.
    - `WF_METADATA` / `WF_PROPERTIES` hold details shown to the approver.
    - `WF_STATUS_DESC` holds the approver's comment.

    | WF_ID | WF_TYPE | WF_REFERENCE | WF_STATUS | WF_EXTERNAL_REFERENCE | TENANT_DOMAIN |
    |---|---|---|---|---|---|
    | 3 | AM_SUBSCRIPTION_CREATION | 31 | APPROVED | `7c2d…` | carbon.super |

3. **Decision.** The approver acts in the Admin Portal (or an external BPMN engine calls back). `WF_STATUS` and `WF_UPDATED_TIME` are updated, and APIM completes or cancels the original action.

## Workflow types and what they point at

`WF_TYPE` decides which table `WF_REFERENCE` refers to. This is a *polymorphic* reference: one column pointing at different tables depending on the type.

| WF_TYPE | Gates | WF_REFERENCE points to | Status column in the gated table |
|---|---|---|---|
| `AM_APPLICATION_CREATION` | Create an application | `AM_APPLICATION.APPLICATION_ID` | `APPLICATION_STATUS` |
| `AM_APPLICATION_UPDATE` | Update an application | `AM_APPLICATION.APPLICATION_ID` | `APPLICATION_STATUS` |
| `AM_APPLICATION_DELETION` | Delete an application | `AM_APPLICATION.APPLICATION_ID` | `APPLICATION_STATUS` |
| `AM_SUBSCRIPTION_CREATION` | Subscribe | `AM_SUBSCRIPTION.SUBSCRIPTION_ID` | `SUB_STATUS` |
| `AM_SUBSCRIPTION_UPDATE` | Change tier | `AM_SUBSCRIPTION.SUBSCRIPTION_ID` | `SUB_STATUS`, `TIER_ID_PENDING` |
| `AM_SUBSCRIPTION_DELETION` | Unsubscribe | `AM_SUBSCRIPTION.SUBSCRIPTION_ID` | `SUBS_CREATE_STATE` |
| `AM_APPLICATION_REGISTRATION_PRODUCTION` / `_SANDBOX` | Generate keys | `AM_APPLICATION_REGISTRATION.REG_ID` (via `WF_REF`) | `AM_APPLICATION_KEY_MAPPING.STATE` |
| `AM_API_STATE` / `AM_API_PRODUCT_STATE` | Lifecycle change | the API | registry lifecycle state |
| `AM_REVISION_DEPLOYMENT` | Deploy a revision | the revision | `AM_DEPLOYMENT_REVISION_MAPPING.REVISION_STATUS` |
| `AM_USER_SIGNUP` | Self sign-up | the username | user account state |

*The `WF_TYPE` values come from APIM's workflow constants. They're not defined in the database scripts, so check them against your version's documentation.*

!!! warning "Logical link (no foreign key)"
    `WF_REFERENCE` is a plain string that holds a number, a UUID or a username, depending on `WF_TYPE`. Deleting the gated row doesn't delete the workflow row. APIM's code cleans up pending ones.

!!! info "The `WF_*` tables"
    The `WF_*` tables (`WF_REQUEST`, `WF_WORKFLOW`, `WF_WORKFLOW_ASSOCIATION` and so on) belong to the embedded Identity Server's own workflow engine, which is used for user-management approvals. APIM's API-side approvals use only `AM_WORKFLOWS`. See [Workflows](../domains/workflows.md).

## Try it

This query lists pending approvals with the application or subscription each one refers to.

```sql
SELECT w.WF_ID, w.WF_TYPE, w.WF_STATUS, w.WF_CREATED_TIME,
       ap.NAME AS APPLICATION, sub.TIER_ID
FROM AM_WORKFLOWS w
LEFT JOIN AM_APPLICATION ap
       ON w.WF_TYPE LIKE 'AM_APPLICATION_%' AND w.WF_TYPE NOT LIKE 'AM_APPLICATION_REGISTRATION%'
      AND CAST(ap.APPLICATION_ID AS CHAR) = w.WF_REFERENCE
LEFT JOIN AM_SUBSCRIPTION sub
       ON w.WF_TYPE LIKE 'AM_SUBSCRIPTION_%'
      AND CAST(sub.SUBSCRIPTION_ID AS CHAR) = w.WF_REFERENCE
WHERE w.WF_STATUS = 'CREATED';
```

!!! note "Different in 3.x"
    3.x uses the same `AM_WORKFLOWS` table. It doesn't have the revision-deployment workflow type, because it has no revisions. See [3.x: Approval workflows](../../apim-3/flows/13-approval-workflows.md).

**Related domains:** [Workflows](../domains/workflows.md) · [Applications & subscriptions](../domains/applications-subscriptions.md)
