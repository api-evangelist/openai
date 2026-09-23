---
name: Run a bulk inference batch at half price
description: Submit a JSONL batch, poll it, cancel it inside the documented window, and pull the results — the cheapest path for high-volume inference.
api: openapi/openai-batch-api-openapi.yml
operations: [createFile, createBatch, retrieveBatch, cancelBatch, listBatches]
generated: '2026-08-27'
method: generated
source: >-
  Grounded in operationIds verified verbatim in openapi/openai-batch-api-openapi.yml
  and openapi/openai-files-api-openapi.yml. The cancellation window is quoted
  from the cancelBatch summary in openapi/_original/openai-openapi-master.yml.
---

# Run a bulk inference batch at half price

The Batch API is documented at a 50% discount to standard pricing
(`plans/openai-plans-pricing.yml`). It is asynchronous and it is the only
write path in this API with a **stated** cancellation window.

## Steps

1. **`createFile`** — `POST /files` with `purpose: batch` and a JSONL body where
   each line is one request. Returns the `input_file_id`.
2. **`createBatch`** — `POST /batches` with `input_file_id`, `endpoint`, and
   `completion_window`. Returns a `batch_` id.
3. **`retrieveBatch`** — `GET /batches/{batch_id}`. Poll until `status` is
   `completed`, `failed`, `expired` or `cancelled`.
4. **`cancelBatch`** — `POST /batches/{batch_id}/cancel` while in progress.
   The contract states the batch sits in `cancelling` **for up to 10 minutes**
   before reaching `cancelled`, and **partial results (if any) remain available
   in the output file**. Cancelling is not a refund — work already done was done.
5. Read results from `output_file_id`; errors from `error_file_id`. Both are
   File ids — fetch them through the Files API.

## Rules

- Do not resubmit a batch on a timeout. There is no idempotency key, and a
  duplicate batch is a duplicate bill.
- `listBatches` uses cursor pagination: `limit` + `after`, and loop while
  `has_more` is true.
