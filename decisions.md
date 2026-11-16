# Decisions

## D1. PostgreSQL + pgvector instead of a dedicated vector DB
One datastore means one backup, one access-control model, and one thing to
secure. pgvector is fast enough at this scale. Revisit at millions of chunks.

## D2. Configuration only through environment variables
Typed with pydantic-settings; the app refuses to start if a required secret
is missing. Only `.env.example` is committed.

## D3. Docker Compose with a DB healthcheck and a non-root API container
Reproducible one-command start; the database is not exposed outside the
Docker network.

## D4. Local LLM (Ollama) behind a swappable interface
Documents and questions never leave the infrastructure: embeddings and
generation both run locally. The model is a config value, so a hosted
provider can be plugged in later where the architecture allows it.
