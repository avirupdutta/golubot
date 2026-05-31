from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass

from agno.agent import Agent
from agno.os.interfaces.base import BaseInterface


@dataclass(frozen=True)
class BotRegistration:
    name: str
    agent: Agent
    interfaces: Sequence[BaseInterface]
    setup: Callable[[], Awaitable[None]]
