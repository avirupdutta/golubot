import os

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.os import AgentOS
from agno.os.interfaces.slack import Slack
from dotenv import load_dotenv
import uvicorn

load_dotenv()


def build_interfaces(agent: Agent) -> list[Slack]:
    if os.getenv("SLACK_TOKEN") and os.getenv("SLACK_SIGNING_SECRET"):
        return [Slack(agent=agent)]

    return []


agent = Agent(
    name="Assistant",
    model=OpenAIResponses(
        id=os.getenv("OPENAI_MODEL", "gpt-5.4-mini"), reasoning_effort="medium"
    ),
    debug_mode=True,
    debug_level=2,
)

agent_os = AgentOS(
    agents=[agent],
    interfaces=build_interfaces(agent),
)
app = agent_os.get_app()


@app.get("/healthz", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"service": "lancelot", "status": "ok"}


def main() -> None:
    uvicorn.run(
        "backend.lancelot:app",
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", "8000")),
        reload=os.getenv("RELOAD", "false").lower() == "true",
    )


if __name__ == "__main__":
    main()
