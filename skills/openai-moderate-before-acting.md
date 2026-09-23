---
name: Moderate input before acting on it
description: Screen user-supplied content with the Moderations API before passing it to a model or acting on it.
api: openapi/openai-moderations-api-openapi.yml
operations: [createModeration, createResponse]
generated: '2026-08-27'
method: generated
source: >-
  Grounded in operationIds verified verbatim in
  openapi/openai-moderations-api-openapi.yml and
  openapi/openai-responses-api-openapi.yml. Mirrors
  arazzo/openai-moderate-then-chat-workflow.yml.
---

# Moderate input before acting on it

## Steps

1. **`createModeration`** — `POST /moderations` with the untrusted `input`
   (text, or image URLs for a multimodal moderation model).
2. Read `results[0].flagged` and the per-category `categories` / `category_scores`.
3. Only if not flagged, **`createResponse`** — `POST /responses` with the input.

## Rules

- Moderation is the cheapest call in this API and the only pre-flight check it
  offers. There is **no dry-run mode** on any other operation
  (`conventions/openai-conventions.yml`), so this is the closest thing to
  rehearsing an action that exists.
- Moderating is advisory. It does not stop a downstream call — your code has to.
- Do not treat a moderation pass as authorisation to take a real-world action.
  It classifies content; it says nothing about consequence.
