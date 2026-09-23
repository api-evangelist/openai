---
name: Transcribe audio and summarize it
description: Turn an audio file into text with the Audio API, then summarize the transcript with the Responses API, then speak the summary back.
api: openapi/openai-audio-api-openapi.yml
operations: [createTranscription, createTranslation, createResponse, createSpeech]
generated: '2026-08-27'
method: generated
source: >-
  Grounded in operationIds verified verbatim in openapi/openai-audio-api-openapi.yml
  and openapi/openai-responses-api-openapi.yml. Mirrors
  arazzo/openai-transcribe-then-summarize-workflow.yml.
---

# Transcribe audio and summarize it

## Steps

1. **`createTranscription`** — `POST /audio/transcriptions`, multipart, with the
   audio `file` and a transcription `model`. Use **`createTranslation`**
   (`POST /audio/translations`) instead when you want English output from
   non-English audio.
2. **`createResponse`** — `POST /responses` with the transcript as `input` and an
   instruction to summarize. See `openai-generate-a-response.md` for retry rules.
3. **`createSpeech`** — `POST /audio/speech` with the summary text, a `voice` and
   a `model`, to render the summary back as audio. The response is binary audio,
   not JSON.

## Rules

- All three steps are billed separately and none is idempotent. On a timeout,
  do not resend the audio — you will pay to transcribe it twice.
- For live, bidirectional speech use the **Realtime API** over WebSocket
  (`wss://api.openai.com/v1/realtime?model={model}`, header
  `OpenAI-Beta: realtime=v1`) rather than these REST operations. The event
  contract is modelled in `asyncapi/openai-realtime-asyncapi.yml`, and a Realtime
  connection is capped at **60 minutes** — reconnect to continue.
- Legacy audio, realtime and transcription models (`gpt-audio`, `gpt-realtime`)
  were announced for shutdown on 2027-01-20; prefer `gpt-audio-1.5` and
  `gpt-realtime-2.1`. See `lifecycle/openai-lifecycle.yml`.
