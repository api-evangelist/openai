# OpenAI GraphQL

## Description

OpenAI does not offer a native public GraphQL endpoint. All official API access is provided through the OpenAI REST API at `https://api.openai.com/v1`. This schema is a comprehensive conceptual GraphQL representation derived from the OpenAI REST API surface, covering models, chat completions, embeddings, images, audio, files, fine-tuning, batches, assistants, threads, messages, runs, vector stores, uploads, moderations, and administration resources.

The schema is intended for use in tooling, documentation generation, type-safe client generation, schema federation experiments, and API design reference — not for direct execution against an OpenAI endpoint.

## Endpoint

None. OpenAI has no public GraphQL endpoint.

## Docs

- API Reference: https://platform.openai.com/docs/api-reference
- GitHub (OpenAI OpenAPI spec): https://github.com/openai/openai-openapi
- Developer Portal: https://developers.openai.com/

## Note

This is a **conceptual schema** hand-derived from the OpenAI REST API. Types map 1:1 to REST response objects documented at https://platform.openai.com/docs/api-reference. Mutations represent POST/DELETE REST operations; queries represent GET operations. All field names follow the snake_case conventions used by the OpenAI JSON API.
