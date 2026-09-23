---
name: Fine-tune a model
description: Upload training data, start a fine-tuning job, monitor it, cancel it if needed, and use or retire the resulting model.
api: openapi/openai-fine-tuning-api-openapi.yml
operations: [createFile, createFineTuningJob, retrieveFineTuningJob, listFineTuningEvents, cancelFineTuningJob, deleteModel]
generated: '2026-08-27'
method: generated
source: >-
  Grounded in operationIds verified verbatim in
  openapi/openai-fine-tuning-api-openapi.yml, openapi/openai-files-api-openapi.yml
  and openapi/openai-models-api-openapi.yml.
---

# Fine-tune a model

## Steps

1. **`createFile`** — `POST /files` with `purpose: fine-tune` for the training
   set, and again for a validation set if you have one.
2. **`createFineTuningJob`** — `POST /fine_tuning/jobs` with `model`,
   `training_file`, and optionally `validation_file`, `hyperparameters` and
   `suffix`. Returns an `ftjob-` id.
3. **`retrieveFineTuningJob`** — `GET /fine_tuning/jobs/{fine_tuning_job_id}`.
   Poll until `status` is `succeeded`, `failed` or `cancelled`.
   **`listFineTuningEvents`** gives the training log.
4. On success the job carries `fine_tuned_model` — a model id you pass to
   `createResponse` or `createChatCompletion` exactly like a base model.
5. **`cancelFineTuningJob`** — `POST /fine_tuning/jobs/{fine_tuning_job_id}/cancel`
   "immediately cancels" a running job. Compute already consumed is still billed.

## Irreversibility

`deleteModel` on a fine-tuned model is **permanent**. The training run cannot be
replayed for free — you would pay to train again, and the result is not
guaranteed to be identical. Never let an agent call `deleteModel` without a
human confirming.

## Rules

- Fine-tuning jobs are long. Never retry `createFineTuningJob` on a client
  timeout: there is no idempotency key and you would start a second paid run.
  Call `listFineTuningJobs` and look for your `suffix` instead.
