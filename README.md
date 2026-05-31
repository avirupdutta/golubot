# Lancelot

A Slack bot backend built with FastAPI and Agno AgentOS.

## Python Backend

Install and run the backend with UV:

```bash
uv sync
uv run uvicorn backend.lancelot:app --reload
```

The shorter module entrypoint also works:

```bash
uv run uvicorn backend
```

This project wraps that shorthand to run `backend.lancelot:app` with `--reload`.

You can also use the module entrypoint:

```bash
uv run python -m backend.lancelot
```

The app exposes:

- `GET /health` from Agno AgentOS
- `GET /healthz` app-specific health check
- `POST /slack/events` when `SLACK_TOKEN` and `SLACK_SIGNING_SECRET` are set

Copy `.env.example` to `.env` and fill in the values before connecting Slack:

```bash
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-5.4-mini
SLACK_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
```

Run tests:

```bash
uv run pytest
```

## Node/GolemBot

The existing gateway command is still available:

```bash
pnpm start
```
