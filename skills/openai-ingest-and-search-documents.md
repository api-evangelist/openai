---
name: Ingest documents and search them
description: Upload files, build a vector store, attach the files, and run a semantic search — the retrieval-augmented flow, with its irreversible steps called out.
api: openapi/openai-vector-stores-api-openapi.yml
operations: [createFile, createVectorStore, createVectorStoreFile, createVectorStoreFileBatch, cancelVectorStoreFileBatch, searchVectorStore, deleteVectorStoreFile, deleteVectorStore, deleteFile]
generated: '2026-08-27'
method: generated
source: >-
  Grounded in operationIds verified verbatim in
  openapi/openai-vector-stores-api-openapi.yml and
  openapi/openai-files-api-openapi.yml. Reversibility notes from
  conventions/openai-conventions.yml.
---

# Ingest documents and search them

## Steps

1. **`createFile`** — `POST /files` with `purpose: assistants`. Returns a
   `file-` id. For anything over the multipart threshold use the Upload flow
   instead (see `openai-upload-a-large-file.md`).
2. **`createVectorStore`** — `POST /vector_stores`. Returns a `vs_` id.
   Optionally set `expires_after` (between 3600 seconds and 2592000 seconds).
3. **Attach the files.** One of:
   - **`createVectorStoreFile`** — `POST /vector_stores/{vector_store_id}/files`
     for a single file.
   - **`createVectorStoreFileBatch`** — `POST /vector_stores/{vector_store_id}/file_batches`
     for many. Poll it; **`cancelVectorStoreFileBatch`** stops further processing
     on a best-effort basis. Files already processed stay processed.
4. **`searchVectorStore`** — `POST /vector_stores/{vector_store_id}/search` with
   your query. This is the retrieval step.

## Irreversibility — read before any cleanup

`deleteVectorStore`, `deleteVectorStoreFile` and `deleteFile` are **permanent**.
There is no restore operation, no trash, and no retention window anywhere in this
API. `deleteFile` is the highest-consequence delete in the whole OpenAI contract
because Batch, FineTuningJob, VectorStore, Assistant, Container and Upload all
reference File by id — deleting one breaks every reference to it silently.

Re-ingesting is the only recovery, and re-embedding is billable.

Confirm with a human, or persist the ids somewhere recoverable, before deleting.
