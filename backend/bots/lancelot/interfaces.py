from os import getenv

from agno.agent import Agent
from agno.os.interfaces.slack import Slack


def build_interfaces(agent: Agent) -> list[Slack]:
    if getenv("SLACK_TOKEN") and getenv("SLACK_SIGNING_SECRET"):
        return [Slack(agent=agent)]

    return []
