from backend.bots.base import BotRegistration
from backend.bots.lancelot.agent import agent
from backend.bots.lancelot.interfaces import build_interfaces
from backend.bots.lancelot.wiki import DEFAULT_WIKI_PATH, build_tools, setup_wiki, wiki


async def setup_lancelot() -> None:
    await setup_wiki()
    agent.set_tools(build_tools())


registration = BotRegistration(
    name="lancelot",
    agent=agent,
    interfaces=build_interfaces(agent),
    setup=setup_lancelot,
)

__all__ = [
    "DEFAULT_WIKI_PATH",
    "agent",
    "registration",
    "setup_lancelot",
    "setup_wiki",
    "wiki",
]
