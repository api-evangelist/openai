# OpenAI (openai)

<!-- API-EVANGELIST-PROVENANCE:BEGIN -->
> ### About this repository
>
> **This is not our API.** This repository is an independent, third-party profile of a company's
> **publicly available** API surface, maintained by [API Evangelist](https://apievangelist.com).
> API Evangelist does not operate, host, resell, or support this company's APIs, and is not
> affiliated with or endorsed by the company unless stated on the profile.
>
> **Where the information came from.** Everything here is assembled from material a member of the
> public can reach with a browser and no credentials — the company's own website, developer portal
> and documentation, the specifications it publishes for public use (OpenAPI, AsyncAPI, JSON Schema,
> `apis.json`, `llms.txt` and similar), its public repositories, and its public status, pricing and
> changelog pages. **Nothing here is obtained by breaching a system, defeating an access control, or
> using credentials of any kind.**
>
> **The rating is an independent assessment.** The Kin Score and Agent Readiness rating are
> independently calculated scores of a company's *public* API artifacts, produced by API Evangelist
> against a published rubric. They are not certifications, endorsements, security assessments, or
> audits, and they score published artifacts — not the quality, safety, or security of the software.
>
> **Corrections, re-scores, and removal are free.** No partnership, contract, or purchase is
> required, and you do not need to justify the request.
>
> - **Something wrong?** Open an issue on this repository, or email
>   [info@apievangelist.com](mailto:info@apievangelist.com).
> - **Published something new?** Ask for a re-score and we will re-run the rating.
> - **Want the listing taken down?** Say so and we will honor it. The profile is reduced to your
>   company name, a factual description, and a link to your own site, and the company is recorded as
>   **unrated** — never scored zero for having asked.
>
> **Response times.** Acknowledgement within **one business day**; removal or restriction within
> **two business days**; corrections and re-scores within **five business days**.
>
> **On a security or compliance team?** Email
> [info@apievangelist.com](mailto:info@apievangelist.com) with *security* in the subject line and
> you will get a person, not a form. We will tell you exactly which public URLs this profile was
> built from so your team can see the same surface we did, and we will take the listing down on
> request while you work through it.
>
> Full detail: **[Where this data comes from](https://apievangelist.com/about/where-our-data-comes-from)**
<!-- API-EVANGELIST-PROVENANCE:END -->

APIs for accessing OpenAI's artificial intelligence models including GPT, DALL-E, Whisper, and Embeddings.

**APIs.json:** [https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/apis.yml](https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/apis.yml)

## Scope

- **Position:** Consuming
- **Access:** 3rd-Party

## Tags

- AI
- Artificial Intelligence
- Large Language Models
- T1

## Timestamps

- **Created:** 2024-04-14
- **Modified:** 2026-05-29

## APIs

### OpenAI Assistants API

The Assistants API allows you to build AI assistants within your own applications. An Assistant has instructions and can leverage models, tools, and knowledge to respond to user queries. The Assistants API currently supports three types of tools - Code Interpreter, Retrieval, and Function calling. In the future, we plan to release more OpenAI-built tools, and allow you to provide your own tools on our platform.

- **Human URL:** [https://platform.openai.com/docs/assistants/overview](https://platform.openai.com/docs/assistants/overview)
- **Base URL:** `https://api.openai.com`

#### Tags

- Assistants

#### Properties

- [Documentation](https://platform.openai.com/docs/assistants/overview)
- [Documentation](https://platform.openai.com/docs/api-reference/assistants)
- [OpenAPI](openapi/assistants-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

### OpenAI Audio API

The Audio API provides two speech to text endpoints, transcriptions and translations, based on our state-of-the-art open source large-v2 Whisper model.

- **Human URL:** [https://platform.openai.com/docs/guides/text-to-speech](https://platform.openai.com/docs/guides/text-to-speech)
- **Base URL:** `https://api.openai.com`

#### Tags

- Audio

#### Properties

- [Documentation](https://platform.openai.com/docs/guides/text-to-speech)
- [Documentation](https://platform.openai.com/docs/api-reference/audio)
- [Documentation](https://platform.openai.com/docs/guides/speech-to-text)
- [Documentation](https://developers.openai.com/api/docs/guides/audio/)
- [Documentation](https://developers.openai.com/api/docs/guides/voice-agents/)
- [OpenAPI](openapi/audio-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [OpenAPI](openapi/openai-audio-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON-LD](json-ld/openai-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)

### OpenAI Chat API

Given a list of messages comprising a conversation, the model will return a response., providing an AI chat interface you can use to engage with users.

- **Human URL:** [https://platform.openai.com/docs/api-reference/chat](https://platform.openai.com/docs/api-reference/chat)
- **Base URL:** `https://api.openai.com`

#### Tags

- Chat

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/chat)
- [OpenAPI](openapi/chat-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [OpenAPI](openapi/openai-chat-completions-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/openai-chat-completion-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON-LD](json-ld/openai-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)

### OpenAI Chat Completions API

Chat models take a list of messages as input and return a model-generated message as output. Although the chat format is designed to make multi-turn conversations easy, it's just as useful for single-turn tasks without any conversation.

- **Human URL:** [https://platform.openai.com/docs/api-reference/chat](https://platform.openai.com/docs/api-reference/chat)
- **Base URL:** `https://api.openai.com`

#### Tags

- Chat
- Completions

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/chat)
- [OpenAPI](properties/openai-chat-completions-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [OpenAPI](openapi/openai-chat-completions-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/openai-chat-completion-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON-LD](json-ld/openai-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)

### OpenAI Embeddings API

Learn how to turn text into numbers, unlocking use cases like search. OpenAI's text embeddings measure the relatedness of text strings.

- **Human URL:** [https://platform.openai.com/docs/guides/embeddings](https://platform.openai.com/docs/guides/embeddings)
- **Base URL:** `https://api.openai.com`

#### Tags

- Embedding
- Embeddings
- Inputs
- Representing
- Text
- Vectors

#### Properties

- [Documentation](https://platform.openai.com/docs/guides/embeddings)
- [Documentation](https://platform.openai.com/docs/api-reference/embeddings)
- [OpenAPI](openapi/embeddings-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [OpenAPI](openapi/openai-embeddings-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/openai-embedding-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON-LD](json-ld/openai-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)

### OpenAI Files API

Files are used to upload documents that can be used with features like Assistants and Fine-tuning. Upload a file that can be used across various endpoints. The size of all the files uploaded by one organization can be up to 100 GB.

- **Human URL:** [https://platform.openai.com/docs/api-reference/files](https://platform.openai.com/docs/api-reference/files)
- **Base URL:** `https://api.openai.com`

#### Tags

- AI
- Artificial Intelligence
- Files

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/files)
- [OpenAPI](openapi/files-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

### OpenAI Fine Tuning API

Manage fine-tuning jobs to tailor a model to your specific training data. Creates a fine-tuning job which begins the process of creating a new model from a given dataset.Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

- **Human URL:** [https://platform.openai.com/docs/guides/fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)
- **Base URL:** `https://api.openai.com`

#### Tags

- Fine Tune
- Fine Tuning

#### Properties

- [Documentation](https://platform.openai.com/docs/guides/fine-tuning)
- [Documentation](https://platform.openai.com/docs/api-reference/fine-tuning)
- [OpenAPI](openapi/fine-tuning-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

### OpenAI Images API

Learn how to generate or manipulate images with DALL_E in the API. The Images API provides three methods for interacting with images - creating images from scratch based on a text prompt, creating edited versions of images by having the model replace some areas of a pre-existing image, based on a new text prompt, Creating variations of an existing image.

- **Human URL:** [https://platform.openai.com/docs/guides/images](https://platform.openai.com/docs/guides/images)
- **Base URL:** `https://api.openai.com`

#### Tags

- Images

#### Properties

- [Documentation](https://platform.openai.com/docs/guides/images)
- [Documentation](https://platform.openai.com/docs/api-reference/images)
- [Documentation](https://platform.openai.com/docs/guides/image-generation)
- [Documentation](https://platform.openai.com/docs/guides/images-vision)
- [OpenAPI](openapi/images-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [OpenAPI](openapi/openai-images-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON-LD](json-ld/openai-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)

### OpenAI Models API

List and describe the various models available in the API. You can refer to the Models documentation to understand what models are available and the differences between them.

- **Human URL:** [https://platform.openai.com/docs/models](https://platform.openai.com/docs/models)
- **Base URL:** `https://api.openai.com`

#### Tags

- Large Language Models
- Models

#### Properties

- [Documentation](https://platform.openai.com/docs/models)
- [Documentation](https://platform.openai.com/docs/api-reference/models)
- [OpenAPI](openapi/models-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

### OpenAI Threads API

Create threads that assistants can interact with.

- **Human URL:** [https://platform.openai.com/docs/assistants/how-it-works/managing-threads-and-messages](https://platform.openai.com/docs/assistants/how-it-works/managing-threads-and-messages)
- **Base URL:** `https://api.openai.com`

#### Tags

- Assistants
- Threads

#### Properties

- [Documentation](https://platform.openai.com/docs/assistants/how-it-works/managing-threads-and-messages)
- [Documentation](https://platform.openai.com/docs/api-reference/threads)
- [OpenAPI](openapi/threads-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

### OpenAI Responses API

The Responses API is OpenAI's most advanced interface for generating model responses. It combines the strengths of the Chat Completions and Assistants APIs into a single streamlined interface, supporting text and image inputs, text outputs, and built-in tools like web search, file search, computer use, code interpreter, and image generation. The upstream OpenAI OpenAPI spec exposes Responses as a dedicated tag group with create/retrieve/list/cancel/delete/stream operations plus input items management. Recommended for all new projects.

- **Human URL:** [https://platform.openai.com/docs/api-reference/responses](https://platform.openai.com/docs/api-reference/responses)
- **Base URL:** `https://api.openai.com`

#### Tags

- Agents
- Responses
- Text Generation
- Reasoning
- Tools

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/responses)
- [Documentation](https://platform.openai.com/docs/guides/text)
- [Documentation](https://developers.openai.com/api/docs/guides/deep-research/)
- [Documentation](https://developers.openai.com/api/docs/guides/conversation-state/)
- [Documentation](https://developers.openai.com/api/docs/guides/migrate-to-responses/)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Moderations API

The Moderations API can be used to check whether text or images are potentially harmful. It classifies content across several categories including harassment, hate speech, sexual content, self-harm, violence, and illicit content. The moderation endpoint is free to use and supports the omni-moderation-latest model for multi-modal inputs.

- **Human URL:** [https://platform.openai.com/docs/api-reference/moderations](https://platform.openai.com/docs/api-reference/moderations)
- **Base URL:** `https://api.openai.com`

#### Tags

- Content Safety
- Moderation

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/moderations)
- [Documentation](https://platform.openai.com/docs/guides/moderation)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Batch API

The Batch API enables asynchronous processing of requests with 50% cost discount, higher rate limits, and completion within 24 hours. It supports /v1/responses, /v1/chat/completions, /v1/embeddings, /v1/completions, and /v1/moderations endpoints. A single batch may include up to 50,000 requests with a batch input file size up to 200 MB.

- **Human URL:** [https://platform.openai.com/docs/api-reference/batch](https://platform.openai.com/docs/api-reference/batch)
- **Base URL:** `https://api.openai.com`

#### Tags

- Async
- Batch

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/batch)
- [Documentation](https://platform.openai.com/docs/guides/batch)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Vector Stores API

Vector stores are collections of processed files that power semantic search for the file_search tool in the Responses and Assistants APIs. When you add a file to a vector store it is automatically chunked, embedded, and indexed. You can query a vector store using natural language to retrieve relevant chunks with similarity scores.

- **Human URL:** [https://platform.openai.com/docs/api-reference/vector-stores](https://platform.openai.com/docs/api-reference/vector-stores)
- **Base URL:** `https://api.openai.com`

#### Tags

- Retrieval
- Search
- Vector Stores

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/vector-stores)
- [Documentation](https://platform.openai.com/docs/guides/retrieval)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Uploads API

The Uploads API creates an intermediate Upload object that you can add Parts to, enabling large file uploads. Currently an Upload can accept at most 8 GB in total and expires after an hour. Once you complete the Upload, a File object is created that can be used across the platform.

- **Human URL:** [https://platform.openai.com/docs/api-reference/uploads](https://platform.openai.com/docs/api-reference/uploads)
- **Base URL:** `https://api.openai.com`

#### Tags

- Files
- Uploads

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/uploads)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Realtime API

The Realtime API enables low-latency, bidirectional communication with models that natively support speech-to-speech interactions as well as multimodal inputs (audio, images, and text) and outputs (audio and text). It supports WebRTC, WebSocket, and SIP connection methods for real-time voice agents and conversational interfaces. The Realtime API is represented as a dedicated tag group in the upstream OpenAI OpenAPI specification with operations covering client/server events, translation client secrets, and voice call lifecycle (accept, hangup, refer, reject).

- **Human URL:** [https://platform.openai.com/docs/api-reference/realtime](https://platform.openai.com/docs/api-reference/realtime)
- **Base URL:** `https://api.openai.com`

#### Tags

- Audio
- Realtime
- Streaming
- Voice
- SIP
- WebRTC

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/realtime)
- [Documentation](https://platform.openai.com/docs/guides/realtime)
- [Documentation](https://platform.openai.com/docs/guides/realtime-webrtc)
- [Documentation](https://platform.openai.com/docs/guides/realtime-server-controls)
- [Documentation](https://developers.openai.com/api/docs/guides/realtime-conversations/)
- [GitHub Repository](https://github.com/openai/openai-realtime-agents)
- [AsyncAPI](asyncapi/openai-realtime-asyncapi.yml) — [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Evals API

The Evals API allows you to programmatically configure and run evaluations to test model outputs against your expectations. Evaluations ensure model responses meet style and content criteria you specify, and are essential for building reliable LLM applications, especially when upgrading or trying new models.

- **Human URL:** [https://platform.openai.com/docs/api-reference/evals](https://platform.openai.com/docs/api-reference/evals)
- **Base URL:** `https://api.openai.com`

#### Tags

- Evals
- Evaluation
- Testing

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/evals)
- [Documentation](https://platform.openai.com/docs/guides/evals)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Completions API

The legacy Completions API endpoint provides a freeform text completion interface using a text prompt. Unlike the Chat Completions endpoint which uses a list of messages, the Completions API input is a freeform text string called a prompt. This endpoint received its last update in July 2023.

- **Human URL:** [https://platform.openai.com/docs/api-reference/completions](https://platform.openai.com/docs/api-reference/completions)
- **Base URL:** `https://api.openai.com`

#### Tags

- Completions
- Legacy

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/completions)
- [OpenAPI](openapi/completions-openapi-original.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

### OpenAI Videos API

The Videos API enables programmatic creation, extension, and remixing of videos using Sora models. It provides endpoints for creating a new render job from a text prompt, checking video status, downloading finished MP4 files, listing videos with pagination, and deleting videos from storage. Supported models include sora-2 and sora-2-pro.

- **Human URL:** [https://platform.openai.com/docs/api-reference/videos](https://platform.openai.com/docs/api-reference/videos)
- **Base URL:** `https://api.openai.com`

#### Tags

- Sora
- Video Generation
- Videos

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/videos)
- [Documentation](https://platform.openai.com/docs/guides/video-generation)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Conversations API

The Conversations API allows you to create and manage stateful conversations for use with the Responses API. A conversation object contains an id, a created_at timestamp, and metadata. Because conversations are stateful, managing context across conversations is handled automatically, and the /responses/compact endpoint can shrink context for long-running conversations.

- **Human URL:** [https://platform.openai.com/docs/api-reference/conversations/create](https://platform.openai.com/docs/api-reference/conversations/create)
- **Base URL:** `https://api.openai.com`

#### Tags

- Conversations
- State Management

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/conversations/create)
- [Documentation](https://developers.openai.com/api/docs/guides/conversation-state/)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Containers API

The Containers API manages sandboxed containers used by Code Interpreter for running Python, data work, file transforms, and iterative debugging. Containers can be created explicitly or auto-managed, with configurable memory limits of 1g, 4g, 16g, or 64g. Container files can be uploaded, listed, retrieved, and downloaded. Containers expire after 20 minutes of inactivity.

- **Human URL:** [https://platform.openai.com/docs/api-reference/containers](https://platform.openai.com/docs/api-reference/containers)
- **Base URL:** `https://api.openai.com`

#### Tags

- Code Interpreter
- Containers
- Sandbox

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/containers)
- [Documentation](https://platform.openai.com/docs/api-reference/container-files)
- [Documentation](https://developers.openai.com/api/docs/guides/tools-code-interpreter/)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI ChatKit API

ChatKit is the best way to build agentic chat experiences. It provides session and thread management for building internal knowledge base assistants, research companions, support agents, and more. ChatKit sessions include resolved feature configuration for automatic thread titling, file upload, and history settings. Threads have statuses including active, locked, and closed.

- **Human URL:** [https://platform.openai.com/docs/api-reference/chatkit](https://platform.openai.com/docs/api-reference/chatkit)
- **Base URL:** `https://api.openai.com`

#### Tags

- Agents
- Chat
- ChatKit

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/chatkit)
- [Documentation](https://platform.openai.com/docs/guides/chatkit)
- [GitHub Repository](https://github.com/openai/chatkit-js)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Skills API

The Skills API surfaces OpenAI's Agent Skills — discoverable folders of instructions, scripts, and resources that agents (notably Codex) can use to perform specific tasks. Operations cover creating, retrieving, updating, deleting, and versioning skills as well as retrieving skill content. The companion github.com/openai/skills repository hosts a catalog of system, curated, and experimental skills.

- **Human URL:** [https://platform.openai.com/docs/api-reference](https://platform.openai.com/docs/api-reference)
- **Base URL:** `https://api.openai.com`

#### Tags

- Agents
- Codex
- Skills

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference)
- [GitHub Repository](https://github.com/openai/skills)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Agents SDK

The OpenAI Agents SDK is a lightweight framework for building multi-agent workflows in Python and TypeScript. Primitives include agents (LLMs with instructions, tools, guardrails), handoffs between specialists, guardrails for safety checks, sessions for conversation history, tracing for run observability, and realtime agents for voice workflows. The SDK is provider-agnostic and supports OpenAI Responses and Chat Completions plus other LLM providers.

- **Human URL:** [https://github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- **Base URL:** `https://api.openai.com`

#### Tags

- Agents
- SDK
- Voice
- Sandbox

#### Properties

- [GitHub Repository](https://github.com/openai/openai-agents-python)
- [GitHub Repository](https://github.com/openai/openai-agents-js)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### OpenAI Codex

OpenAI Codex is a lightweight coding agent that runs in the terminal, with companion IDE extensions, a desktop app, and a web experience at chatgpt.com/codex. Codex authenticates with a ChatGPT Plus/Pro/Business/Edu/Enterprise account or an API key, and integrates with the Skills catalog for repeatable task workflows.

- **Human URL:** [https://developers.openai.com/codex](https://developers.openai.com/codex)
- **Base URL:** `https://api.openai.com`

#### Tags

- Agents
- Codex
- Coding Agent

#### Properties

- [Documentation](https://developers.openai.com/codex)
- [GitHub Repository](https://github.com/openai/codex)
- [Postman Collection](collections/openai-audio.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-audio.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-chat-completions.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-chat-completions.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-embeddings.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-embeddings.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-images.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-images.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/openai-openapi-master.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/openai-openapi-master.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

## Common Properties

- [Arazzo Workflows](arazzo/) — [Arazzo Specification](https://spec.openapis.org/arazzo/latest.html)
- [LinkedIn](https://www.linkedin.com/company/openai)
- [Portal](https://platform.openai.com/docs/overview)
- [Getting Started](https://platform.openai.com/docs/quickstart)
- [S D Ks](https://platform.openai.com/docs/libraries)
- [Forums](https://community.openai.com/categories)
- [Rate Limits](https://platform.openai.com/docs/guides/rate-limits)
- [Deprecations](https://platform.openai.com/docs/deprecations)
- [Terms of Service](https://openai.com/policies/)
- [Terms of Service](https://openai.com/policies/terms-of-use/)
- [Privacy Policy](https://openai.com/policies/privacy-policy/)
- [Documentation](https://platform.openai.com/docs/overview)
- [Support](https://help.openai.com/en)
- [Status Page](https://status.openai.com/)
- [Authentication](https://platform.openai.com/docs/api-reference/authentication)
- [Webhooks](https://platform.openai.com/docs/api-reference/webhook_events/response)
- [OpenAPI](properties/openai-openapi) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [JSON Schema](json-schema/openai-chat-completion-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/openai-embedding-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON-LD](json-ld/openai-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [GitHub Organization](https://github.com/openai)
- [Plans](https://openai.com/api/pricing/)
- [Pricing](https://openai.com/api/pricing/)
- [Tiers](https://openai.com/api/pricing/)
- [Rate Limits](https://example.com/rate-limits)
- [Status Page](https://status.openai.com/)
- [A P I  Keys](https://platform.openai.com/api-keys)
- [Sign Up](https://platform.openai.com/signup)
- [Login](https://platform.openai.com/login)
- [Changelog](https://developers.openai.com/changelog/)
- [Blog](https://developers.openai.com/blog/)
- [Cookbook](https://cookbook.openai.com/)
- [Safety Best Practices](https://platform.openai.com/docs/guides/safety-best-practices)
- [Best Practices](https://platform.openai.com/docs/guides/production-best-practices)
- [Security](https://openai.com/security-and-privacy/)
- [Documentation](https://platform.openai.com/docs/api-reference/administration)
- [Documentation](https://platform.openai.com/docs/api-reference/audit-logs)
- [Documentation](https://platform.openai.com/docs/api-reference/usage)
- [Documentation](https://platform.openai.com/docs/guides/function-calling)
- [Documentation](https://platform.openai.com/docs/guides/structured-outputs)
- [GitHub Repository](https://github.com/openai/openai-openapi)
- [OpenAPI](openapi/openai-openapi-master.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [GitHub Repository](https://github.com/openai/openai-python)
- [GitHub Repository](https://github.com/openai/openai-node)
- [GitHub Repository](https://github.com/openai/openai-go)
- [GitHub Repository](https://github.com/openai/openai-dotnet)
- [GitHub Repository](https://github.com/openai/openai-java)
- [GitHub Repository](https://github.com/openai/openai-ruby)
- [GitHub Repository](https://github.com/openai/openai-agents-python)
- [GitHub Repository](https://github.com/openai/openai-agents-js)
- [GitHub Repository](https://github.com/openai/codex)
- [GitHub Repository](https://github.com/openai/skills)
- [GitHub Repository](https://github.com/openai/gpt-oss)
- [GitHub Repository](https://github.com/openai/openai-realtime-agents)
- [GitHub Repository](https://github.com/openai/whisper)
- [GitHub Repository](https://github.com/openai/tiktoken)
- [Terms of Service](https://openai.com/policies/service-terms/)
- [Documentation](https://platform.openai.com/docs/guides/webhooks)
- [Documentation](https://platform.openai.com/docs/api-reference/webhook-events)
- [Documentation](https://developers.openai.com/api/docs/guides/deep-research/)
- [Documentation](https://developers.openai.com/api/docs/guides/voice-agents/)
- [Documentation](https://developers.openai.com/api/docs/guides/code-generation/)
- [Documentation](https://platform.openai.com/docs/guides/images-vision)
- [Documentation](https://developers.openai.com/api/docs/guides/conversation-state/)
- [Documentation](https://developers.openai.com/api/docs/guides/migrate-to-responses/)
- [Documentation](https://platform.openai.com/docs/api-reference/containers)
- [Documentation](https://platform.openai.com/docs/api-reference/container-files)
- [Documentation](https://platform.openai.com/docs/api-reference/chatkit)
- [Documentation](https://platform.openai.com/docs/api-reference/videos)
- [Documentation](https://platform.openai.com/docs/api-reference/conversations/create)
- [Portal](https://developers.openai.com/)
- [Documentation](https://developers.openai.com/api/reference/)
- [Documentation](https://developers.openai.com/codex)
- [GitHub Repository](https://github.com/openai/chatkit-js)
- [Spectral Rules](rules/openai-spectral-rules.yml)
- [Vocabulary](vocabulary/openai-vocabulary.yaml)
- [Features](https://platform.openai.com/docs/overview)
- [Use Cases](https://openai.com/api/)
- [Integrations](https://platform.openai.com/docs/libraries)
- [Agent Skill](https://github.com/openai/skills)
- [L L Ms Txt](https://developers.openai.com/llms.txt)

## Maintainers

**FN:** Kin Lane
**Email:** kin@apievangelist.com
