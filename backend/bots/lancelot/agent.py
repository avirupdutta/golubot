from os import getenv

from agno.agent import Agent
from agno.models.openai import OpenAIResponses

from backend.bots.lancelot.wiki import build_tools


def build_agent() -> Agent:
    return Agent(
        name="Assistant",
        model=OpenAIResponses(
            id=getenv("OPENAI_MODEL", "gpt-5.4-mini"), reasoning_effort="medium"
        ),
        debug_mode=True,
        debug_level=2,
        tools=build_tools(),
    )


agent = build_agent()
