---
name: Generate a model response
description: Call the Responses API for a single- or multi-turn model response, streaming or in the background, with correct retry and cancellation behaviour.
api: openapi/openai-responses-api-openapi.yml
operations: [createResponse, getResponse, cancelResponse, deleteResponse]
generated: '2026-08-27'
method: generated
source: >-
  Grounded in operationIds verified verbatim in
  openapi/openai-responses-api-openapi.yml. Cross-cutting rules from
  conventions/openai-conventions.yml and errors/openai-problem-types.yml.
---

# Generate a model response

Base URL `https://api.openai.com/v1`. Auth: `Authorization: Bearer sk-proj-...`.

## Steps

1. **`createResponse`** — `POST /responses`. Send `model` and `input`.
   - For a multi-turn exchange, set `previous_response_id` to the id of the last
     response rather than resending history.
   - Set `stream: true` for Server-Sent Events (`text/event-stream`).
   - Set `background: true` if the call may be long. **This is the only way to
     get a cancellable response** — a synchronous call cannot be cancelled.
2. **`getResponse`** — `GET /responses/{response_id}` to poll a background response.
3. **`cancelResponse`** — `POST /responses/{response_id}/cancel`. Works only when
   the response was created with `background: true`.
4. **`deleteResponse`** — `DELETE /responses/{response_id}` when you no longer
   want the stored response. **Permanent — there is no restore.**

## Rules that apply to every call

- **There is no idempotency key.** A retried `createResponse` is a second
  billable inference, not a deduplicated no-op. Never blind-retry a POST.
- **429 means five different things.** Read `error.code` before backing off:
  - no code / rate-limit shape → back off, honour `Retry-After`, retry
  - `credit_balance_exhausted`, `organization_spend_limit_exceeded`,
    `project_spend_limit_exceeded`, `organization_usage_limit_exceeded` →
    **do not retry**; a human must change a billing setting
- **503 has two meanings.** "Engine overloaded" is a normal backoff.
  "Slow Down" asks for a *sustained* 15-minute rate reduction.
- Record `x-request-id` from every response. It is the only handle support accepts.
- Pace against `x-ratelimit-remaining-requests` and `x-ratelimit-remaining-tokens`.
- Carry your own correlation id in `metadata` (up to 16 key/value pairs), since
  there is no idempotency key to correlate on.
