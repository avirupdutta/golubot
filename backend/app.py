from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from os import getenv

from agno.os import AgentOS
from dotenv import load_dotenv

import uvicorn

load_dotenv()

from backend.bots.lancelot import registration as lancelot_registration  # noqa: E402

BOT_REGISTRATIONS = [lancelot_registration]


@asynccontextmanager
async def lifespan(_: AgentOS) -> AsyncIterator[None]:
    for registration in BOT_REGISTRATIONS:
        await registration.setup()
    yield


agent_os = AgentOS(
    agents=[registration.agent for registration in BOT_REGISTRATIONS],
    interfaces=[
        interface
        for registration in BOT_REGISTRATIONS
        for interface in registration.interfaces
    ],
    lifespan=lifespan,
)
app = agent_os.get_app()


@app.get("/healthz", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"service": "lancelot", "status": "ok"}


def main() -> None:
    uvicorn.run(
        "backend.app:app",
        host=getenv("HOST", "127.0.0.1"),
        port=int(getenv("PORT", "8000")),
        reload=getenv("RELOAD", "false").lower() == "true",
    )


if __name__ == "__main__":
    main()
