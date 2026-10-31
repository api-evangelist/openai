# OpenAI

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
> **Not from the company, and here with a question?** You are welcome here — we would rather be the
> front line and point you the right way than have a good report go nowhere. What this repository
> can answer is narrow, though, so it is worth knowing who you are actually looking for:
>
> - **A question about how the API works, an account, billing, or a bug in the service** — that is
>   the company's own support, not us. We profile this API; we do not operate it and cannot see
>   your account.
> - **A bug in an open-source project we only catalog** — file it on that project's own repository.
>   This has happened with a real and correct bug report that reached us instead of the people who
>   could fix it, which helped nobody.
> - **Anything about this listing itself** — the description, the tags, the rating, a missing or
>   wrong artifact — is ours. Open an issue here.
> - **Not sure, or something general about API Evangelist or APIs.io** — open an issue on the
>   [APIs.io Inbox](https://github.com/api-search/inbox) and we will route it.
>
> **This repository contains no software, and we will never ask you to download anything.** There is
> no build, release, installer, or binary here — only text and machine-readable API descriptions, so
> there is nothing here that can be "corrupt" or need "repairing". Any issue, comment, or email
> claiming otherwise and offering a download link is not from us and is hostile. Do not follow the
> link; it is a lure. Report it to GitHub and, if you like, tell us at
> [info@apievangelist.com](mailto:info@apievangelist.com) so we can take it down.
>
> **On a security or compliance team?** Email
> [info@apievangelist.com](mailto:info@apievangelist.com) with *security* in the subject line and
> you will get a person, not a form. We will tell you exactly which public URLs this profile was
> built from so your team can see the same surface we did, and we will take the listing down on
> request while you work through it.
>
> Full detail: **[Where this data comes from](https://apievangelist.com/about/where-our-data-comes-from)**
<!-- API-EVANGELIST-PROVENANCE:END -->

OpenAI publishes a single unversioned REST API at https://api.openai.com/v1 covering text and reasoning (Responses, Chat Completions), embeddings, images, audio and speech, video, moderation, file storage, vector stores and file search, containers, batch inference at half price, fine-tuning, evals, ChatKit, agent skills, and a full organization administration plane for projects, users, groups, roles, API keys, certificates, usage and audit logs. The contract is OpenAPI 3.1.0 with 242 operations, published by OpenAI itself under MIT at github.com/openai/openai-openapi. Realtime is a separate WebSocket surface at wss://api.openai.com/v1/realtime. Authentication is a project-scoped bearer API key; OAuth 2.0 / OIDC at auth.openai.com grants user identity only, not API authority. First-party SDKs ship for Python, JavaScript, Go, Java, .NET and Ruby, alongside the Codex CLI and an anonymous documentation MCP server at developers.openai.com/mcp.

**Areas:** LLM · OpenAI · Artificial Intelligence · Generative AI · Chatbots · Foundation Models · T1

## OpenAI on APIs.io

Everything profiled for OpenAI is published on APIs.io rather than in this repository. Start at the provider page — **[apis.io/providers/openai/](https://apis.io/providers/openai/)** — or go straight to one of the APIs or properties below.

### APIs (63)

- [OpenAI Responses API](https://apis.io/apis/openai/openai-responses-api/) — The Responses API is OpenAI's most advanced interface for generating model responses. It combines the strengths of the Chat Completions and Assistants APIs…
- [OpenAI Moderations API](https://apis.io/apis/openai/openai-moderations-api/) — The Moderations API can be used to check whether text or images are potentially harmful. It classifies content across several categories including…
- [OpenAI Batch API](https://apis.io/apis/openai/openai-batch-api/) — The Batch API enables asynchronous processing of requests with 50% cost discount, higher rate limits, and completion within 24 hours. It supports…
- [OpenAI Vector Stores API](https://apis.io/apis/openai/openai-vector-stores-api/) — Vector stores are collections of processed files that power semantic search for the file_search tool in the Responses and Assistants APIs. When you add a…
- [OpenAI Uploads API](https://apis.io/apis/openai/openai-uploads-api/) — The Uploads API creates an intermediate Upload object that you can add Parts to, enabling large file uploads. Currently an Upload can accept at most 8 GB in…
- [OpenAI Realtime API](https://apis.io/apis/openai/openai-realtime-api/) — The Realtime API enables low-latency, bidirectional communication with models that natively support speech-to-speech interactions as well as multimodal…
- [OpenAI Evals API](https://apis.io/apis/openai/openai-evals-api/) — The Evals API allows you to programmatically configure and run evaluations to test model outputs against your expectations. Evaluations ensure model…
- [OpenAI Videos API](https://apis.io/apis/openai/openai-videos-api/) — The Videos API enables programmatic creation, extension, and remixing of videos using Sora models. It provides endpoints for creating a new render job from…
- [OpenAI Conversations API](https://apis.io/apis/openai/openai-conversations-api/) — The Conversations API allows you to create and manage stateful conversations for use with the Responses API. A conversation object contains an id, a…
- [OpenAI Containers API](https://apis.io/apis/openai/openai-containers-api/) — The Containers API manages sandboxed containers used by Code Interpreter for running Python, data work, file transforms, and iterative debugging. Containers…
- [OpenAI ChatKit API](https://apis.io/apis/openai/openai-chatkit-api/) — ChatKit is the best way to build agentic chat experiences. It provides session and thread management for building internal knowledge base assistants,…
- [OpenAI Skills API](https://apis.io/apis/openai/openai-skills-api/) — The Skills API surfaces OpenAI's Agent Skills — discoverable folders of instructions, scripts, and resources that agents (notably Codex) can use to perform…
- [OpenAI Agents SDK](https://apis.io/apis/openai/openai-agents-sdk/) — The OpenAI Agents SDK is a lightweight framework for building multi-agent workflows in Python and TypeScript. Primitives include agents (LLMs with…
- [OpenAI Codex](https://apis.io/apis/openai/openai-codex/) — OpenAI Codex is a lightweight coding agent that runs in the terminal, with companion IDE extensions, a desktop app, and a web experience at…
- [OpenAI Assistants API](https://apis.io/apis/openai/openai-assistants-api/) — Build Assistants that can call models and use tools.
- [OpenAI Audio API](https://apis.io/apis/openai/openai-audio-api/) — Learn how to turn audio into text or text into audio.
- [OpenAI Audit Logs API](https://apis.io/apis/openai/openai-audit-logs-api/) — List user actions and configuration changes within this organization.
- [OpenAI Batch API](https://apis.io/apis/openai/openai-batch-api/) — Create large batches of API requests to run asynchronously.
- [OpenAI Certificates API](https://apis.io/apis/openai/openai-certificates-api/) — The Certificates API from OpenAI — 7 operation(s) for certificates.
- [OpenAI Chatkit API](https://apis.io/apis/openai/openai-chatkit-api/) — The Chatkit API from OpenAI — 5 operation(s) for chatkit.
- [OpenAI Completions API](https://apis.io/apis/openai/openai-completions-api/) — Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position.
- [OpenAI Containers API](https://apis.io/apis/openai/openai-containers-api/) — The Containers API from OpenAI — 5 operation(s) for containers.
- [OpenAI Conversations API](https://apis.io/apis/openai/openai-conversations-api/) — Manage conversations and conversation items.
- [OpenAI Embeddings API](https://apis.io/apis/openai/openai-embeddings-api/) — Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.
- [OpenAI Evals API](https://apis.io/apis/openai/openai-evals-api/) — Manage and run evals in the OpenAI platform.
- [OpenAI Files API](https://apis.io/apis/openai/openai-files-api/) — Files are used to upload documents that can be used with features like Assistants and Fine-tuning.
- [OpenAI Fine Tuning API](https://apis.io/apis/openai/openai-fine-tuning-api/) — The Fine Tuning API from OpenAI — 11 operation(s) for fine tuning.
- [OpenAI Group organization role assignments API](https://apis.io/apis/openai/openai-group-organization-role-assignments-api/) — The Group organization role assignments API from OpenAI — 2 operation(s) for group organization role assignments.
- [OpenAI Group users API](https://apis.io/apis/openai/openai-group-users-api/) — The Group users API from OpenAI — 2 operation(s) for group users.
- [OpenAI Groups API](https://apis.io/apis/openai/openai-groups-api/) — The Groups API from OpenAI — 2 operation(s) for groups.
- [OpenAI Images API](https://apis.io/apis/openai/openai-images-api/) — Given a prompt and/or an input image, the model will generate a new image.
- [OpenAI Invites API](https://apis.io/apis/openai/openai-invites-api/) — The Invites API from OpenAI — 2 operation(s) for invites.
- [OpenAI Models API](https://apis.io/apis/openai/openai-models-api/) — List and describe the various models available in the API.
- [OpenAI Moderations API](https://apis.io/apis/openai/openai-moderations-api/) — Given text and/or image inputs, classifies if those inputs are potentially harmful.
- [OpenAI Organization API](https://apis.io/apis/openai/openai-organization-api/) — The Organization API from OpenAI — 2 operation(s) for organization.
- [OpenAI Project group role assignments API](https://apis.io/apis/openai/openai-project-group-role-assignments-api/) — The Project group role assignments API from OpenAI — 2 operation(s) for project group role assignments.
- [OpenAI Project groups API](https://apis.io/apis/openai/openai-project-groups-api/) — The Project groups API from OpenAI — 2 operation(s) for project groups.
- [OpenAI Project user role assignments API](https://apis.io/apis/openai/openai-project-user-role-assignments-api/) — The Project user role assignments API from OpenAI — 2 operation(s) for project user role assignments.
- [OpenAI Projects API](https://apis.io/apis/openai/openai-projects-api/) — The Projects API from OpenAI — 11 operation(s) for projects.
- [OpenAI Realtime API](https://apis.io/apis/openai/openai-realtime-api/) — The Realtime API from OpenAI — 9 operation(s) for realtime.
- [OpenAI Responses API](https://apis.io/apis/openai/openai-responses-api/) — The Responses API from OpenAI — 6 operation(s) for responses.
- [OpenAI Roles API](https://apis.io/apis/openai/openai-roles-api/) — The Roles API from OpenAI — 4 operation(s) for roles.
- [OpenAI Skills API](https://apis.io/apis/openai/openai-skills-api/) — The Skills API from OpenAI — 6 operation(s) for skills.
- [OpenAI Threads API](https://apis.io/apis/openai/openai-threads-api/) — The Threads API from OpenAI — 13 operation(s) for threads.
- [OpenAI Uploads API](https://apis.io/apis/openai/openai-uploads-api/) — Use Uploads to upload large files in multiple parts.
- [OpenAI Usage API](https://apis.io/apis/openai/openai-usage-api/) — The Usage API from OpenAI — 9 operation(s) for usage.
- [OpenAI User organization role assignments API](https://apis.io/apis/openai/openai-user-organization-role-assignments-api/) — The User organization role assignments API from OpenAI — 2 operation(s) for user organization role assignments.
- [OpenAI Users API](https://apis.io/apis/openai/openai-users-api/) — The Users API from OpenAI — 2 operation(s) for users.
- [OpenAI Vector stores API](https://apis.io/apis/openai/openai-vector-stores-api/) — The Vector stores API from OpenAI — 10 operation(s) for vector stores.
- [OpenAI Videos API](https://apis.io/apis/openai/openai-videos-api/) — The Videos API from OpenAI — 8 operation(s) for videos.
- [OpenAI Agents API](https://apis.io/apis/openai/openai-agents-api/) — The Agents API from OpenAI — 21 operation(s) for agents.
- [OpenAI Content Provenance Checks API](https://apis.io/apis/openai/openai-content-provenance-checks-api/) — The Content Provenance Checks API from OpenAI — 1 operation(s) for content provenance checks.
- [OpenAI Data retention API](https://apis.io/apis/openai/openai-data-retention-api/) — The Data retention API from OpenAI — 2 operation(s) for data retention.
- [OpenAI Hosted tools API](https://apis.io/apis/openai/openai-hosted-tools-api/) — The Hosted tools API from OpenAI — 1 operation(s) for hosted tools.
- [OpenAI Live API](https://apis.io/apis/openai/openai-live-api/) — The Live API from OpenAI — 7 operation(s) for live.
- [OpenAI OpenAI API](https://apis.io/apis/openai/openai-openai-api-api/) — The OpenAI API API from OpenAI — 0 operation(s) for openai api.
- [OpenAI Safety API](https://apis.io/apis/openai/openai-safety-api/) — The Safety API from OpenAI — 2 operation(s) for safety.
- [OpenAI Spend alerts API](https://apis.io/apis/openai/openai-spend-alerts-api/) — The Spend alerts API from OpenAI — 4 operation(s) for spend alerts.
- [OpenAI Vaults API](https://apis.io/apis/openai/openai-vaults-api/) — The Vaults API from OpenAI — 4 operation(s) for vaults.
- [OpenAI Webhook Endpoints API](https://apis.io/apis/openai/openai-webhook-endpoints-api/) — The Webhook Endpoints API from OpenAI — 4 operation(s) for webhook endpoints.
- [OpenAI Webhook Event Types API](https://apis.io/apis/openai/openai-webhook-event-types-api/) — The Webhook Event Types API from OpenAI — 1 operation(s) for webhook event types.
- [OpenAI Decisions API](https://apis.io/apis/openai/openai-decisions-api/) — The Decisions API from OpenAI — 1 operation(s) for decisions. Ask classification or scoring questions about the same input and get the answers back in order…
- [OpenAI Chat Completions API](https://apis.io/apis/openai/openai-chat-completions-api/) — Given a list of messages comprising a conversation, the model will return a response.

### Published properties

Each property below is a page on APIs.io carrying the machine-readable artifact and what it says.

#### Arazzo workflows (17)

Multi-step workflows that chain operations into a business task.

- [OpenAI Assistant Run](https://apis.io/arazzos/openai/openai-assistant-run-workflow/)
- [OpenAI Batch Job](https://apis.io/arazzos/openai/openai-batch-job-workflow/)
- [OpenAI Cancel Fine-Tuning Job](https://apis.io/arazzos/openai/openai-cancel-fine-tuning-job-workflow/)
- [OpenAI Chat then Speak](https://apis.io/arazzos/openai/openai-chat-then-speak-workflow/)
- [OpenAI Create Embedding](https://apis.io/arazzos/openai/openai-create-embedding-workflow/)
- [OpenAI Download Batch Results](https://apis.io/arazzos/openai/openai-download-batch-results-workflow/)
- [OpenAI Fine-Tuning Job](https://apis.io/arazzos/openai/openai-fine-tuning-job-workflow/)
- [OpenAI Moderate then Generate Image](https://apis.io/arazzos/openai/openai-generate-image-workflow/)
- [OpenAI List Models then Create Chat Completion](https://apis.io/arazzos/openai/openai-list-models-then-chat-workflow/)
- [OpenAI Moderate then Chat](https://apis.io/arazzos/openai/openai-moderate-then-chat-workflow/)
- [OpenAI Retrieve and Delete Fine-Tuned Model](https://apis.io/arazzos/openai/openai-retrieve-and-delete-model-workflow/)
- [OpenAI Create Thread and Run](https://apis.io/arazzos/openai/openai-thread-and-run-workflow/)
- [OpenAI Transcribe then Summarize](https://apis.io/arazzos/openai/openai-transcribe-then-summarize-workflow/)
- [OpenAI Upload and Verify File](https://apis.io/arazzos/openai/openai-upload-and-verify-file-workflow/)
- [OpenAI Vector Store File Batch](https://apis.io/arazzos/openai/openai-vector-store-file-batch-workflow/)
- [OpenAI Vector Store Ingest File](https://apis.io/arazzos/openai/openai-vector-store-ingest-file-workflow/)
- [OpenAI Vector Store Search](https://apis.io/arazzos/openai/openai-vector-store-search-workflow/)

#### AsyncAPI (1)

Event-driven and webhook contracts.

- [OpenAI Realtime API](https://apis.io/asyncapis/openai/openai-realtime-asyncapi/)

#### Event channels (37)

Individual events and webhooks the provider emits.

- [conversation.created](https://apis.io/channels/openai/conversation-created/)
- [conversation.item.create](https://apis.io/channels/openai/conversation-item-create/)
- [conversation.item.created](https://apis.io/channels/openai/conversation-item-created/)
- [conversation.item.delete](https://apis.io/channels/openai/conversation-item-delete/)
- [conversation.item.deleted](https://apis.io/channels/openai/conversation-item-deleted/)
- [conversation.item.input_audio_transcription.completed](https://apis.io/channels/openai/conversation-item-input-audio-transcription-completed/)
- [conversation.item.input_audio_transcription.failed](https://apis.io/channels/openai/conversation-item-input-audio-transcription-failed/)
- [conversation.item.truncate](https://apis.io/channels/openai/conversation-item-truncate/)
- [conversation.item.truncated](https://apis.io/channels/openai/conversation-item-truncated/)
- [error](https://apis.io/channels/openai/error/)
- [input_audio_buffer.append](https://apis.io/channels/openai/input-audio-buffer-append/)
- [input_audio_buffer.clear](https://apis.io/channels/openai/input-audio-buffer-clear/)
- [input_audio_buffer.cleared](https://apis.io/channels/openai/input-audio-buffer-cleared/)
- [input_audio_buffer.commit](https://apis.io/channels/openai/input-audio-buffer-commit/)
- [input_audio_buffer.committed](https://apis.io/channels/openai/input-audio-buffer-committed/)
- [input_audio_buffer.speech_started](https://apis.io/channels/openai/input-audio-buffer-speech-started/)
- [input_audio_buffer.speech_stopped](https://apis.io/channels/openai/input-audio-buffer-speech-stopped/)
- [rate_limits.updated](https://apis.io/channels/openai/rate-limits-updated/)
- [response.audio.delta](https://apis.io/channels/openai/response-audio-delta/)
- [response.audio.done](https://apis.io/channels/openai/response-audio-done/)
- [response.audio_transcript.delta](https://apis.io/channels/openai/response-audio-transcript-delta/)
- [response.audio_transcript.done](https://apis.io/channels/openai/response-audio-transcript-done/)
- [response.cancel](https://apis.io/channels/openai/response-cancel/)
- [response.content_part.added](https://apis.io/channels/openai/response-content-part-added/)
- [response.content_part.done](https://apis.io/channels/openai/response-content-part-done/)
- …and 12 more published on APIs.io

#### GraphQL (1)

GraphQL schemas.

- [Moved to /providers/openai/](https://apis.io/graphqls/openai/openai-graphql/)

#### MCP servers (1)

Model Context Protocol servers that expose the API to agents.

- [openai-docs-mcp](https://apis.io/servers/openai/openai-docs-mcp/)

#### Agent skills (44)

Agent skills built on the API.

- [aspnet-core](https://apis.io/agent-skills/openai/aspnet-core/)
- [chatgpt-apps](https://apis.io/agent-skills/openai/chatgpt-apps/)
- [cli-creator](https://apis.io/agent-skills/openai/cli-creator/)
- [cloudflare-deploy](https://apis.io/agent-skills/openai/cloudflare-deploy/)
- [define-goal](https://apis.io/agent-skills/openai/define-goal/)
- [figma](https://apis.io/agent-skills/openai/figma/)
- [figma-code-connect-components](https://apis.io/agent-skills/openai/figma-code-connect-components/)
- [figma-create-design-system-rules](https://apis.io/agent-skills/openai/figma-create-design-system-rules/)
- [figma-create-new-file](https://apis.io/agent-skills/openai/figma-create-new-file/)
- [figma-generate-design](https://apis.io/agent-skills/openai/figma-generate-design/)
- [figma-generate-library](https://apis.io/agent-skills/openai/figma-generate-library/)
- [figma-implement-design](https://apis.io/agent-skills/openai/figma-implement-design/)
- [figma-use](https://apis.io/agent-skills/openai/figma-use/)
- [gh-address-comments](https://apis.io/agent-skills/openai/gh-address-comments/)
- [gh-fix-ci](https://apis.io/agent-skills/openai/gh-fix-ci/)
- [hatch-pet](https://apis.io/agent-skills/openai/hatch-pet/)
- [imagegen](https://apis.io/agent-skills/openai/imagegen/)
- [jupyter-notebook](https://apis.io/agent-skills/openai/jupyter-notebook/)
- [linear](https://apis.io/agent-skills/openai/linear/)
- [migrate-to-codex](https://apis.io/agent-skills/openai/migrate-to-codex/)
- [netlify-deploy](https://apis.io/agent-skills/openai/netlify-deploy/)
- [notion-knowledge-capture](https://apis.io/agent-skills/openai/notion-knowledge-capture/)
- [notion-meeting-intelligence](https://apis.io/agent-skills/openai/notion-meeting-intelligence/)
- [notion-research-documentation](https://apis.io/agent-skills/openai/notion-research-documentation/)
- [notion-spec-to-implementation](https://apis.io/agent-skills/openai/notion-spec-to-implementation/)
- …and 19 more published on APIs.io

#### Agentic access (1)

Which operations an agent can call, which act, and which need a human in the loop.

- [Openai Agentic Access](https://apis.io/agentic-access/openai/openai-agentic-access/)

#### JSON Schema (67)

The data models the API reads and writes.

- [AgentResource](https://apis.io/schemas/openai/openai-agent-resource/)
- [CreateSpeechRequest](https://apis.io/schemas/openai/openai-audio-create-speech-request/)
- [CreateTranscriptionRequest](https://apis.io/schemas/openai/openai-audio-create-transcription-request/)
- [CreateTranslationRequest](https://apis.io/schemas/openai/openai-audio-create-translation-request/)
- [TranscriptionResponse](https://apis.io/schemas/openai/openai-audio-transcription-response/)
- [TranslationResponse](https://apis.io/schemas/openai/openai-audio-translation-response/)
- [OpenAI Chat Completion](https://apis.io/schemas/openai/openai-chat-completion/)
- [ChatCompletionChoice](https://apis.io/schemas/openai/openai-chat-completions-chat-completion-choice/)
- [ChatCompletionMessage](https://apis.io/schemas/openai/openai-chat-completions-chat-completion-message/)
- [ChatCompletionTool](https://apis.io/schemas/openai/openai-chat-completions-chat-completion-tool/)
- [CompletionUsage](https://apis.io/schemas/openai/openai-chat-completions-completion-usage/)
- [ContentPart](https://apis.io/schemas/openai/openai-chat-completions-content-part/)
- [CreateChatCompletionRequest](https://apis.io/schemas/openai/openai-chat-completions-create-chat-completion-request/)
- [CreateChatCompletionResponse](https://apis.io/schemas/openai/openai-chat-completions-create-chat-completion-response/)
- [ToolCall](https://apis.io/schemas/openai/openai-chat-completions-tool-call/)
- [CreateContentProvenanceBody](https://apis.io/schemas/openai/openai-create-content-provenance-body/)
- [CreateEnvironmentTemplateParams](https://apis.io/schemas/openai/openai-create-environment-template-params/)
- [CreateSpendAlertBody](https://apis.io/schemas/openai/openai-create-spend-alert-body/)
- [CreateVaultCredentialParams](https://apis.io/schemas/openai/openai-create-vault-credential-params/)
- [DecisionRequest](https://apis.io/schemas/openai/openai-decision-request/)
- [DecisionResponse](https://apis.io/schemas/openai/openai-decision-response/)
- [OpenAI Embedding Response](https://apis.io/schemas/openai/openai-embedding/)
- [CreateEmbeddingRequest](https://apis.io/schemas/openai/openai-embeddings-create-embedding-request/)
- [CreateEmbeddingResponse](https://apis.io/schemas/openai/openai-embeddings-create-embedding-response/)
- [Embedding](https://apis.io/schemas/openai/openai-embeddings-embedding/)
- …and 42 more published on APIs.io

#### JSON Structure (22)

Data models expressed in JSON Structure.

- [Openai Audio Create Speech Request Structure](https://apis.io/json-structure/openai/openai-audio-create-speech-request-structure/)
- [Openai Audio Create Transcription Request Structure](https://apis.io/json-structure/openai/openai-audio-create-transcription-request-structure/)
- [Openai Audio Create Translation Request Structure](https://apis.io/json-structure/openai/openai-audio-create-translation-request-structure/)
- [Openai Audio Transcription Response Structure](https://apis.io/json-structure/openai/openai-audio-transcription-response-structure/)
- [Openai Audio Translation Response Structure](https://apis.io/json-structure/openai/openai-audio-translation-response-structure/)
- [Openai Chat Completions Chat Completion Choice Structure](https://apis.io/json-structure/openai/openai-chat-completions-chat-completion-choice-structure/)
- [Openai Chat Completions Chat Completion Message Structure](https://apis.io/json-structure/openai/openai-chat-completions-chat-completion-message-structure/)
- [Openai Chat Completions Chat Completion Tool Structure](https://apis.io/json-structure/openai/openai-chat-completions-chat-completion-tool-structure/)
- [Openai Chat Completions Completion Usage Structure](https://apis.io/json-structure/openai/openai-chat-completions-completion-usage-structure/)
- [Openai Chat Completions Content Part Structure](https://apis.io/json-structure/openai/openai-chat-completions-content-part-structure/)
- [Openai Chat Completions Create Chat Completion Request Structure](https://apis.io/json-structure/openai/openai-chat-completions-create-chat-completion-request-structure/)
- [Openai Chat Completions Create Chat Completion Response Structure](https://apis.io/json-structure/openai/openai-chat-completions-create-chat-completion-response-structure/)
- [Openai Chat Completions Tool Call Structure](https://apis.io/json-structure/openai/openai-chat-completions-tool-call-structure/)
- [Openai Embeddings Create Embedding Request Structure](https://apis.io/json-structure/openai/openai-embeddings-create-embedding-request-structure/)
- [Openai Embeddings Create Embedding Response Structure](https://apis.io/json-structure/openai/openai-embeddings-create-embedding-response-structure/)
- [Openai Embeddings Embedding Structure](https://apis.io/json-structure/openai/openai-embeddings-embedding-structure/)
- [Openai Embeddings Embedding Usage Structure](https://apis.io/json-structure/openai/openai-embeddings-embedding-usage-structure/)
- [Openai Images Create Image Edit Request Structure](https://apis.io/json-structure/openai/openai-images-create-image-edit-request-structure/)
- [Openai Images Create Image Request Structure](https://apis.io/json-structure/openai/openai-images-create-image-request-structure/)
- [Openai Images Create Image Variation Request Structure](https://apis.io/json-structure/openai/openai-images-create-image-variation-request-structure/)
- [Openai Images Image Structure](https://apis.io/json-structure/openai/openai-images-image-structure/)
- [Openai Images Images Response Structure](https://apis.io/json-structure/openai/openai-images-images-response-structure/)

#### JSON-LD (5)

Linked-data contexts for the provider's vocabulary.

- [Openai Audio Context](https://apis.io/jsonld/openai/openai-audio-context/)
- [Openai Chat Completions Context](https://apis.io/jsonld/openai/openai-chat-completions-context/)
- [Openai Context](https://apis.io/jsonld/openai/openai-context/)
- [Openai Embeddings Context](https://apis.io/jsonld/openai/openai-embeddings-context/)
- [Openai Images Context](https://apis.io/jsonld/openai/openai-images-context/)

#### Vocabulary (1)

The provider's domain terms, defined.

- [openai API Vocabulary](https://apis.io/vocabularies/openai/openai-vocabulary/)

#### Examples (22)

Example requests and responses.

- [Openai Audio Create Speech Request Example](https://apis.io/examples/openai/openai-audio-create-speech-request-example/)
- [Openai Audio Create Transcription Request Example](https://apis.io/examples/openai/openai-audio-create-transcription-request-example/)
- [Openai Audio Create Translation Request Example](https://apis.io/examples/openai/openai-audio-create-translation-request-example/)
- [Openai Audio Transcription Response Example](https://apis.io/examples/openai/openai-audio-transcription-response-example/)
- [Openai Audio Translation Response Example](https://apis.io/examples/openai/openai-audio-translation-response-example/)
- [Openai Chat Completions Chat Completion Choice Example](https://apis.io/examples/openai/openai-chat-completions-chat-completion-choice-example/)
- [Openai Chat Completions Chat Completion Message Example](https://apis.io/examples/openai/openai-chat-completions-chat-completion-message-example/)
- [Openai Chat Completions Chat Completion Tool Example](https://apis.io/examples/openai/openai-chat-completions-chat-completion-tool-example/)
- [Openai Chat Completions Completion Usage Example](https://apis.io/examples/openai/openai-chat-completions-completion-usage-example/)
- [Openai Chat Completions Content Part Example](https://apis.io/examples/openai/openai-chat-completions-content-part-example/)
- [Openai Chat Completions Create Chat Completion Request Example](https://apis.io/examples/openai/openai-chat-completions-create-chat-completion-request-example/)
- [Openai Chat Completions Create Chat Completion Response Example](https://apis.io/examples/openai/openai-chat-completions-create-chat-completion-response-example/)
- [Openai Chat Completions Tool Call Example](https://apis.io/examples/openai/openai-chat-completions-tool-call-example/)
- [Openai Embeddings Create Embedding Request Example](https://apis.io/examples/openai/openai-embeddings-create-embedding-request-example/)
- [Openai Embeddings Create Embedding Response Example](https://apis.io/examples/openai/openai-embeddings-create-embedding-response-example/)
- [Openai Embeddings Embedding Example](https://apis.io/examples/openai/openai-embeddings-embedding-example/)
- [Openai Embeddings Embedding Usage Example](https://apis.io/examples/openai/openai-embeddings-embedding-usage-example/)
- [Openai Images Create Image Edit Request Example](https://apis.io/examples/openai/openai-images-create-image-edit-request-example/)
- [Openai Images Create Image Request Example](https://apis.io/examples/openai/openai-images-create-image-request-example/)
- [Openai Images Create Image Variation Request Example](https://apis.io/examples/openai/openai-images-create-image-variation-request-example/)
- [Openai Images Image Example](https://apis.io/examples/openai/openai-images-image-example/)
- [Openai Images Images Response Example](https://apis.io/examples/openai/openai-images-images-response-example/)

#### Collections (56)

Postman and Open Collection request collections.

- [OpenAI Assistants API](https://apis.io/collections/openai/open-openai-assistants-api/)
- [OpenAI Audio API](https://apis.io/collections/openai/open-openai-audio/)
- [OpenAI Assistants Audio API](https://apis.io/collections/openai/open-openai-audio-api/)
- [OpenAI Assistants Audit Logs API](https://apis.io/collections/openai/open-openai-audit-logs-api/)
- [OpenAI Assistants Batch API](https://apis.io/collections/openai/open-openai-batch-api/)
- [OpenAI Assistants Certificates API](https://apis.io/collections/openai/open-openai-certificates-api/)
- [OpenAI Assistants Chat API](https://apis.io/collections/openai/open-openai-chat-api/)
- [OpenAI Chat Completions API](https://apis.io/collections/openai/open-openai-chat-completions/)
- [OpenAI Assistants Chatkit API](https://apis.io/collections/openai/open-openai-chatkit-api/)
- [OpenAI Assistants Completions API](https://apis.io/collections/openai/open-openai-completions-api/)
- [OpenAI Assistants Containers API](https://apis.io/collections/openai/open-openai-containers-api/)
- [OpenAI Assistants Conversations API](https://apis.io/collections/openai/open-openai-conversations-api/)
- [OpenAI Embeddings API](https://apis.io/collections/openai/open-openai-embeddings/)
- [OpenAI Assistants Embeddings API](https://apis.io/collections/openai/open-openai-embeddings-api/)
- [OpenAI Assistants Evals API](https://apis.io/collections/openai/open-openai-evals-api/)
- [OpenAI Assistants Files API](https://apis.io/collections/openai/open-openai-files-api/)
- [OpenAI Assistants Fine Tuning API](https://apis.io/collections/openai/open-openai-fine-tuning-api/)
- [OpenAI Assistants Group organization role assignments API](https://apis.io/collections/openai/open-openai-group-organization-role-assignments-api/)
- [OpenAI Assistants Group users API](https://apis.io/collections/openai/open-openai-group-users-api/)
- [OpenAI Assistants Groups API](https://apis.io/collections/openai/open-openai-groups-api/)
- [OpenAI Images API](https://apis.io/collections/openai/open-openai-images/)
- [OpenAI Assistants Images API](https://apis.io/collections/openai/open-openai-images-api/)
- [OpenAI Assistants Invites API](https://apis.io/collections/openai/open-openai-invites-api/)
- [OpenAI Assistants Models API](https://apis.io/collections/openai/open-openai-models-api/)
- [OpenAI Assistants Moderations API](https://apis.io/collections/openai/open-openai-moderations-api/)
- …and 31 more published on APIs.io

#### Overlays (75)

OpenAPI overlays, including conversational phrasing for each operation.

- [Openai Assistants Api Phrasing Overlay](https://apis.io/overlays/openai/openai-assistants-api-phrasing-overlay/)
- [Openai Assistants Overlay](https://apis.io/overlays/openai/openai-assistants-overlay/)
- [Openai Audio Api Phrasing Overlay](https://apis.io/overlays/openai/openai-audio-api-phrasing-overlay/)
- [Openai Audio Overlay](https://apis.io/overlays/openai/openai-audio-overlay/)
- [Openai Audit Logs Api Phrasing Overlay](https://apis.io/overlays/openai/openai-audit-logs-api-phrasing-overlay/)
- [Openai Audit Logs Overlay](https://apis.io/overlays/openai/openai-audit-logs-overlay/)
- [Openai Batch Api Phrasing Overlay](https://apis.io/overlays/openai/openai-batch-api-phrasing-overlay/)
- [Openai Batch Overlay](https://apis.io/overlays/openai/openai-batch-overlay/)
- [Openai Certificates Api Phrasing Overlay](https://apis.io/overlays/openai/openai-certificates-api-phrasing-overlay/)
- [Openai Certificates Overlay](https://apis.io/overlays/openai/openai-certificates-overlay/)
- [Openai Chat Api Phrasing Overlay](https://apis.io/overlays/openai/openai-chat-api-phrasing-overlay/)
- [Openai Chat Overlay](https://apis.io/overlays/openai/openai-chat-overlay/)
- [Openai Chatkit Api Phrasing Overlay](https://apis.io/overlays/openai/openai-chatkit-api-phrasing-overlay/)
- [Openai Chatkit Overlay](https://apis.io/overlays/openai/openai-chatkit-overlay/)
- [Openai Completions Api Phrasing Overlay](https://apis.io/overlays/openai/openai-completions-api-phrasing-overlay/)
- [Openai Completions Overlay](https://apis.io/overlays/openai/openai-completions-overlay/)
- [Openai Containers Api Phrasing Overlay](https://apis.io/overlays/openai/openai-containers-api-phrasing-overlay/)
- [Openai Containers Overlay](https://apis.io/overlays/openai/openai-containers-overlay/)
- [Openai Conversations Api Phrasing Overlay](https://apis.io/overlays/openai/openai-conversations-api-phrasing-overlay/)
- [Openai Conversations Overlay](https://apis.io/overlays/openai/openai-conversations-overlay/)
- [Openai Embeddings Api Phrasing Overlay](https://apis.io/overlays/openai/openai-embeddings-api-phrasing-overlay/)
- [Openai Embeddings Overlay](https://apis.io/overlays/openai/openai-embeddings-overlay/)
- [Openai Evals Api Phrasing Overlay](https://apis.io/overlays/openai/openai-evals-api-phrasing-overlay/)
- [Openai Evals Overlay](https://apis.io/overlays/openai/openai-evals-overlay/)
- [Openai Files Api Phrasing Overlay](https://apis.io/overlays/openai/openai-files-api-phrasing-overlay/)
- …and 50 more published on APIs.io

#### Governance rules (4)

Spectral rulesets for the provider's contracts.

- [OpenAI — asyncapi rules](https://apis.io/rules/openai/openai-asyncapi-spectral-rules/)
- [OpenAI — jsonschema rules](https://apis.io/rules/openai/openai-jsonschema-spectral-rules/)
- [Moved to /providers/openai/](https://apis.io/rules/openai/openai-rules/)
- [OpenAI API Rules](https://apis.io/rules/openai/openai-spectral-rules/)

#### Security (4)

Authentication, trust centre, and vulnerability disclosure.

- [Openai Authentication](https://apis.io/security/openai/openai-authentication/)
- [Openai Domain Security](https://apis.io/security/openai/openai-domain-security/)
- [Openai Trust Center](https://apis.io/security/openai/openai-trust-center/)
- [Openai Vulnerability Disclosure](https://apis.io/security/openai/openai-vulnerability-disclosure/)

#### OAuth scopes (1)

The permissions the API asks for.

- [Openai Scopes](https://apis.io/scopes/openai/openai-scopes/)

#### Plans and pricing (1)

Published plans, tiers and prices.

- [Openai Plans Pricing](https://apis.io/plans/openai/openai-plans-pricing/)

#### Rate limits (1)

Published request limits.

- [Openai Rate Limits](https://apis.io/rate-limits/openai/openai-rate-limits/)

#### FinOps (1)

What the API costs to run, by operation.

- [Openai Finops](https://apis.io/finops/openai/openai-finops/)

## Where to find this API

Links to the company's own pages. This repository publishes no copy of their specifications — the canonical document is theirs and lives at the URLs below.

- [Website](https://openai.com/)
- [Documentation](https://platform.openai.com/docs/overview)
- [Getting started](https://platform.openai.com/docs/quickstart)
- [API reference](https://developers.openai.com/api/reference/)
- [Pricing](https://developers.openai.com/api/docs/pricing.md)
- [Support](https://help.openai.com/en)
- [Changelog](https://developers.openai.com/changelog/)
- [Blog](https://developers.openai.com/blog/)
- [Security](https://openai.com/security-and-privacy/)
- [Terms of service](https://openai.com/policies/)
- [Privacy policy](https://openai.com/policies/privacy-policy/)
- [GitHub](https://github.com/openai)
- [Status](https://status.openai.com/)

## API Evangelist rating

**Kin Score 84.5** — exemplar · rubric 0.25.0 · scored 2026-10-23

| Facet | Score |
|---|---|
| Discoverability | 65.0 |
| Contract quality | 72.2 |
| Contract governance | 45.5 |
| Operational transparency | 94.7 |
| Developer ergonomics | 96.4 |
| Access clarity | 100.0 |

**Agent readiness 58.4** — agent-native

| Agent-readiness dimension | Result |
|---|---|
| Spec Presence | yes |
| Agentic Access | derived (partial credit) |
| Reversibility Documented | documented (partial credit) |
| MCP Server | platform (partial credit) |
| Auth Clarity | served (partial credit) |
| Idempotency | verified |
| Error Semantics | verified |
| OpenAPI Examples | partial |
| Rate Limit Signal | verified |
| Event Surface Described | yes |
| Agent Skills | yes |
| Well Known Catalog | — |
| Consent Identity | — |
| Agent Card | — |
| Dry Run Mode | — |
| Delegated Identity | served (partial credit) |
| Protected Resource Metadata | — |
| Dynamic Client Registration | — |
| Agentic Commerce | — |
| Pagination Ratio | paginated |
| Operation Distinctiveness | mostly |

**Regulatory alignment 41.8** — AI & Biometrics

The rubric is published at [github.com/api-evangelist/kin-score](https://github.com/api-evangelist/kin-score). The per-check breakdown behind these numbers — which checks were earned, partial or missed — along with score history and how this provider compares to its peers, is available at [apis.io/providers/openai/](https://apis.io/providers/openai/).

## How this profile is made

API Evangelist profiles a company's public API surface the way a developer would find it: the website, developer portal and documentation, the specifications it publishes, its public repositories, and its pricing, status and changelog pages. From that it derives the properties above — contracts split per API, workflows, schemas, collections, governance rules, plans and rate limits — and scores them against the published [Kin Score rubric](https://github.com/api-evangelist/kin-score).

The artifacts are published on [APIs.io](https://apis.io), not in this repository. This repository is the public record for OpenAI: the place to say something is wrong, missing or out of date, and to ask for a re-score or a removal.

## Open an issue

- **Something about this listing** — a wrong description, a missing API, a stale artifact or a question about the rating: [open an issue on this repository](https://github.com/api-evangelist/openai/issues/new).
- **A new API, or one that is not in the catalog yet** — [submit it on APIs.io](https://apis.io/add/).
- **Anything else** — [the APIs.io inbox](https://github.com/api-search/inbox/issues/new) or [info@apievangelist.com](mailto:info@apievangelist.com).
