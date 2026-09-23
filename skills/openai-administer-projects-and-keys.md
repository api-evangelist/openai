---
name: Administer projects, users and API keys
description: Provision an isolated project with its own key and spend limit — the only containment boundary OpenAI offers — and revoke credentials safely.
api: openapi/openai-projects-api-openapi.yml
operations: [create-project, list-projects, modify-project, archive-project, create-project-api-key, list-project-api-keys, delete-project-api-key, create-project-service-account, delete-project-service-account, list-users, delete-user]
generated: '2026-08-27'
method: generated
source: >-
  Grounded in operationIds verified verbatim in
  openapi/openai-projects-api-openapi.yml, openapi/openai-users-api-openapi.yml
  and openapi/openai-organization-api-openapi.yml. Containment reasoning from
  sandbox/openai-sandbox.yml.
---

# Administer projects, users and API keys

**Every operation here requires `AdminApiKeyAuth` — an `sk-admin-` key, not a
project key.**

## Why this matters more at OpenAI than elsewhere

OpenAI has **no test mode**. There are no test keys, no fixtures, no sandbox
environment. The **project** is the only isolation primitive: its own API keys,
its own spend limit, its own rate limits, its own usage reporting. Provisioning a
dedicated project with a low spend limit is how you bound an agent's blast
radius, and it is the only automatic brake in the system.

## Steps

1. **`create-project`** — `POST /organization/projects`.
2. Set a **project spend limit** in the console. When it is crossed, calls
   return 429 with `project_spend_limit_exceeded` instead of continuing to spend.
3. **`create-project-api-key`** — issue a key scoped to that project only.
   For a non-human caller prefer **`create-project-service-account`**, which
   holds its own key and survives the departure of any individual.
4. **`list-project-api-keys`** to audit what is live.
5. **`archive-project`** when the workload ends.

## Irreversibility

- **`delete-project-api-key`** revokes a live credential *immediately*. Every
  integration using it fails on the next call. There is no undo and no grace
  period.
- **`delete-user`** removes an organization member. No restore.
- Group and user membership may be **SCIM-managed** (`is_scim_managed` /
  `scim_managed` on the schemas). If it is, change it in the IdP — a direct API
  delete will be reconciled back or will fight the provisioning sync.

## Rules

- Audit-log events exist for administrative actions, including `scim.enabled`
  and `scim.disabled`. Use them, not application logs, as the record of truth.
- Usage and cost are groupable by `api_key_id` (added 2026-08-04). Issue one key
  per workload so that attribution is possible at all.
