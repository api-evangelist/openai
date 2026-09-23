---
name: Upload a large file in parts
description: Use the multipart Upload flow for files too large for a single POST, and cancel cleanly inside the one-hour expiry window.
api: openapi/openai-uploads-api-openapi.yml
operations: [createUpload, addUploadPart, completeUpload, cancelUpload]
generated: '2026-08-27'
method: generated
source: >-
  Grounded in operationIds verified verbatim in openapi/openai-uploads-api-openapi.yml.
  The 8 GB ceiling and one-hour expiry are quoted from the createUpload summary
  in openapi/_original/openai-openapi-master.yml.
---

# Upload a large file in parts

## Steps

1. **`createUpload`** — `POST /uploads` with `filename`, `purpose`, `bytes` and
   `mime_type`. Returns an `upload_` id.
   The contract states an Upload **can accept at most 8 GB in total and expires
   an hour after you create it.**
2. **`addUploadPart`** — `POST /uploads/{upload_id}/parts`, once per chunk.
   Keep every returned part id.
3. **`completeUpload`** — `POST /uploads/{upload_id}/complete` with the ordered
   part ids. This materialises a real **File** object usable everywhere else in
   the platform.
4. **`cancelUpload`** — `POST /uploads/{upload_id}/cancel` to abandon it.
   No Parts may be added after cancellation.

## Rules

- **One hour is a hard window.** An Upload left incomplete past it expires and
  the parts are gone. If an agent is chunking a large file, budget for that.
- `mime_type` must be correct for certain `purpose` values — check the supported
  MIME types for your use case before starting, because a wrong type is only
  discovered at `completeUpload`, after every part has been sent.
- Cancelling an Upload is reversible in the useful sense (nothing was created).
  Deleting the resulting **File** is not — see `openai-ingest-and-search-documents.md`.
