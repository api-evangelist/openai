# OpenAI (openai)
APIs for accessing OpenAI's artificial intelligence models including GPT, DALL-E, Whisper, and Embeddings.

**URL:** [Visit APIs.json URL](https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/apis.yml)

**Run:** [Capabilities Using Naftiko](https://github.com/naftiko/fleet?utm_source=api-evangelist&utm_medium=readme&utm_campaign=company-api-evangelist&utm_content=repo)

## Scope

- **Type:** Contract
- **Position:** Consuming
- **Access:** 3rd-Party

## Tags:

 - AI, Artificial Intelligence, Large Language Models, T1

## Timestamps

- **Created:** 2024-04-14
- **Modified:** 2026-04-18

## APIs

### OpenAI Assistants API
The Assistants API allows you to build AI assistants within your own applications with instructions, tools, and knowledge.

**Human URL:** [https://platform.openai.com/docs/assistants/overview](https://platform.openai.com/docs/assistants/overview)

#### Tags:

 - Assistants

#### Properties

- [Documentation](https://platform.openai.com/docs/assistants/overview)
- [OpenAPI](openapi/assistants-openapi-original.yml)

### OpenAI Audio API
The Audio API provides speech to text and text to speech endpoints based on Whisper and TTS models.

**Human URL:** [https://platform.openai.com/docs/guides/text-to-speech](https://platform.openai.com/docs/guides/text-to-speech)

#### Tags:

 - Audio

#### Properties

- [Documentation](https://platform.openai.com/docs/guides/text-to-speech)
- [OpenAPI](openapi/audio-openapi-original.yml)
- [JSONLD](json-ld/openai-context.jsonld)

### OpenAI Chat API
Given a list of messages comprising a conversation, the model will return a response.

**Human URL:** [https://platform.openai.com/docs/api-reference/chat](https://platform.openai.com/docs/api-reference/chat)

#### Tags:

 - Chat

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/chat)
- [OpenAPI](openapi/chat-openapi-original.yml)
- [JSONSchema](json-schema/openai-chat-completion-schema.json)
- [JSONLD](json-ld/openai-context.jsonld)

### OpenAI Chat Completions API
Chat models take a list of messages as input and return a model-generated message as output.

**Human URL:** [https://platform.openai.com/docs/api-reference/chat](https://platform.openai.com/docs/api-reference/chat)

#### Tags:

 - Chat, Completions

#### Properties

- [OpenAPI](openapi/openai-chat-completions-openapi.yml)
- [JSONSchema](json-schema/openai-chat-completion-schema.json)

### OpenAI Embeddings API
Text embeddings measure the relatedness of text strings as vector representations.

**Human URL:** [https://platform.openai.com/docs/guides/embeddings](https://platform.openai.com/docs/guides/embeddings)

#### Tags:

 - Embeddings, Vectors

#### Properties

- [OpenAPI](openapi/embeddings-openapi-original.yml)
- [JSONSchema](json-schema/openai-embedding-schema.json)

### OpenAI Files API
Files are used to upload documents for features like Assistants and Fine-tuning.

**Human URL:** [https://platform.openai.com/docs/api-reference/files](https://platform.openai.com/docs/api-reference/files)

#### Properties

- [OpenAPI](openapi/files-openapi-original.yml)

### OpenAI Fine Tuning API
Manage fine-tuning jobs to tailor a model to your specific training data.

**Human URL:** [https://platform.openai.com/docs/guides/fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)

#### Properties

- [OpenAPI](openapi/fine-tuning-openapi-original.yml)

### OpenAI Images API
Generate or manipulate images with DALL-E.

**Human URL:** [https://platform.openai.com/docs/guides/images](https://platform.openai.com/docs/guides/images)

#### Properties

- [OpenAPI](openapi/images-openapi-original.yml)
- [JSONLD](json-ld/openai-context.jsonld)

### OpenAI Models API
List and describe the various models available in the API.

**Human URL:** [https://platform.openai.com/docs/models](https://platform.openai.com/docs/models)

#### Properties

- [OpenAPI](openapi/models-openapi-original.yml)

### OpenAI Threads API
Create threads that assistants can interact with.

**Human URL:** [https://platform.openai.com/docs/assistants/how-it-works/managing-threads-and-messages](https://platform.openai.com/docs/assistants/how-it-works/managing-threads-and-messages)

#### Properties

- [OpenAPI](openapi/threads-openapi-original.yml)

### OpenAI Responses API
The most advanced interface for generating model responses with built-in tools.

**Human URL:** [https://platform.openai.com/docs/api-reference/responses](https://platform.openai.com/docs/api-reference/responses)

#### Properties

- [Documentation](https://platform.openai.com/docs/api-reference/responses)

### OpenAI Moderations API
Check whether text or images are potentially harmful.

**Human URL:** [https://platform.openai.com/docs/api-reference/moderations](https://platform.openai.com/docs/api-reference/moderations)

### OpenAI Batch API
Asynchronous processing of requests with 50% cost discount.

**Human URL:** [https://platform.openai.com/docs/api-reference/batch](https://platform.openai.com/docs/api-reference/batch)

### OpenAI Vector Stores API
Managed document storage with automatic chunking, embedding, and semantic search.

**Human URL:** [https://platform.openai.com/docs/api-reference/vector-stores](https://platform.openai.com/docs/api-reference/vector-stores)

### OpenAI Realtime API
Low-latency bidirectional communication for speech-to-speech interactions.

**Human URL:** [https://platform.openai.com/docs/api-reference/realtime](https://platform.openai.com/docs/api-reference/realtime)

### OpenAI Evals API
Programmatically configure and run evaluations to test model outputs.

**Human URL:** [https://platform.openai.com/docs/api-reference/evals](https://platform.openai.com/docs/api-reference/evals)

### OpenAI Completions API
Legacy freeform text completion interface.

**Human URL:** [https://platform.openai.com/docs/api-reference/completions](https://platform.openai.com/docs/api-reference/completions)

#### Properties

- [OpenAPI](openapi/completions-openapi-original.yml)

### OpenAI Videos API
Create, extend, and remix videos using Sora models.

**Human URL:** [https://platform.openai.com/docs/api-reference/videos](https://platform.openai.com/docs/api-reference/videos)

### OpenAI Conversations API
Create and manage stateful conversations for the Responses API.

**Human URL:** [https://platform.openai.com/docs/api-reference/conversations/create](https://platform.openai.com/docs/api-reference/conversations/create)

### OpenAI Containers API
Manage sandboxed containers for Code Interpreter.

**Human URL:** [https://platform.openai.com/docs/api-reference/containers](https://platform.openai.com/docs/api-reference/containers)

### OpenAI ChatKit API
Build agentic chat experiences with session and thread management.

**Human URL:** [https://platform.openai.com/docs/api-reference/chatkit](https://platform.openai.com/docs/api-reference/chatkit)

## Common Properties

- [Portal](https://platform.openai.com/docs/overview)
- [GettingStarted](https://platform.openai.com/docs/quickstart)
- [SDK](https://platform.openai.com/docs/libraries)
- [RateLimits](https://platform.openai.com/docs/guides/rate-limits)
- [TermsOfService](https://openai.com/policies/)
- [PrivacyPolicy](https://openai.com/policies/privacy-policy/)
- [Documentation](https://platform.openai.com/docs/overview)
- [Support](https://help.openai.com/en)
- [StatusPage](https://status.openai.com/)
- [Authentication](https://platform.openai.com/docs/api-reference/authentication)
- [GitHubOrganization](https://github.com/openai)
- [GitHubRepository](https://github.com/openai/openai-openapi)
- [GitHubRepository](https://github.com/openai/openai-python)
- [GitHubRepository](https://github.com/openai/openai-node)
- [SignUp](https://platform.openai.com/signup)
- [Login](https://platform.openai.com/login)
- [ChangeLog](https://developers.openai.com/changelog/)
- [Blog](https://developers.openai.com/blog/)
- [BestPractices](https://platform.openai.com/docs/guides/production-best-practices)
- [Security](https://openai.com/security-and-privacy/)

## Features

| Name | Description |
|------|-------------|
| Chat Completions | Generate conversational responses using GPT models with multi-turn message history, function calling, and structured outputs. |
| Responses API | Advanced model response interface combining Chat Completions and Assistants with built-in tools like web search and code interpreter. |
| Assistants | Build AI assistants with persistent threads, code interpreter, file search, and function calling capabilities. |
| Realtime API | Low-latency bidirectional communication for speech-to-speech interactions via WebRTC, WebSocket, and SIP connections. |
| Image Generation | Create, edit, and generate variations of images using DALL-E models from text prompts. |
| Audio and Speech | Text-to-speech synthesis and speech-to-text transcription and translation using Whisper and TTS models. |
| Embeddings | Generate vector representations of text for semantic search, clustering, and recommendation use cases. |
| Fine-Tuning | Customize models on your own training data to improve performance for specific tasks and domains. |
| Batch Processing | Asynchronous processing of up to 50,000 requests at 50% cost discount with 24-hour completion window. |
| Evals | Programmatically configure and run evaluations to test model outputs against quality and content criteria. |
| Video Generation | Create, extend, and remix videos using Sora models from text prompts via the Videos API. |
| Vector Stores | Managed document storage with automatic chunking, embedding, and semantic search for file_search tool. |

## Use Cases

| Name | Description |
|------|-------------|
| Conversational AI | Build chatbots, virtual assistants, and customer support agents using Chat Completions or Responses API. |
| Content Generation | Generate marketing copy, articles, product descriptions, and creative writing with controllable tone and style. |
| Code Generation | Automate code writing, debugging, refactoring, and documentation generation across programming languages. |
| Document Analysis | Extract, summarize, and answer questions from uploaded documents using Assistants with file search. |
| Voice Agents | Build real-time voice-based AI agents for customer service, sales, and interactive experiences. |
| Semantic Search | Implement intelligent search using embeddings and vector stores for knowledge bases and document retrieval. |
| Content Moderation | Automatically classify and filter harmful content across text and images using the Moderations API. |
| Data Extraction | Extract structured data from unstructured text using function calling and structured outputs. |

## Integrations

| Name | Description |
|------|-------------|
| Python SDK | Official Python client library for accessing all OpenAI API endpoints with async support and streaming. |
| Node.js SDK | Official TypeScript and JavaScript client library for server-side and edge runtime OpenAI API integration. |
| Microsoft Azure OpenAI | Run OpenAI models on Azure infrastructure with enterprise security, compliance, and regional data residency. |
| LangChain | Framework integration for building LLM-powered applications with chains, agents, and retrieval-augmented generation. |
| Vercel AI SDK | Integration with Vercel AI SDK for building streaming AI-powered web applications with React and Next.js. |
| Zapier | No-code automation integration connecting OpenAI to thousands of apps for automated AI-powered workflows. |

## Artifacts

Machine-readable API specifications organized by format.

### OpenAPI

- [Assistants](openapi/assistants-openapi-original.yml)
- [Audio](openapi/audio-openapi-original.yml)
- [Chat](openapi/chat-openapi-original.yml)
- [Chat Completions](openapi/openai-chat-completions-openapi.yml)
- [Completions](openapi/completions-openapi-original.yml)
- [Embeddings](openapi/embeddings-openapi-original.yml)
- [Files](openapi/files-openapi-original.yml)
- [Fine Tuning](openapi/fine-tuning-openapi-original.yml)
- [Images](openapi/images-openapi-original.yml)
- [Models](openapi/models-openapi-original.yml)
- [Threads](openapi/threads-openapi-original.yml)

## Capabilities

Naftiko capabilities organized as shared per-API definitions composed into customer-facing workflows.

### Shared Per-API Definitions

- [Chat](capabilities/shared/chat.yaml) -- 1 operation for chat completions
- [Images](capabilities/shared/images.yaml) -- 3 operations for image generation and editing
- [Audio](capabilities/shared/audio.yaml) -- 3 operations for speech and transcription
- [Embeddings](capabilities/shared/embeddings.yaml) -- 1 operation for vector embeddings
- [Models](capabilities/shared/models.yaml) -- 3 operations for model management

### Workflow Capabilities

| Workflow | APIs Combined | Tools | Persona |
|----------|--------------|-------|---------|
| [Content Generation](capabilities/content-generation.yaml) | Chat + Images + Audio + Embeddings + Models | 10 | Developer |

## Rules

- [OpenAI Spectral Rules](rules/openai-spectral-rules.yml)

## Vocabulary

- [OpenAI Vocabulary](vocabulary/openai-vocabulary.yaml)

## Maintainers

**FN:** Kin Lane

**Email:** kin@apievangelist.com
