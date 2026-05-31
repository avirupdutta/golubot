import sys

from uvicorn.main import main as uvicorn_main


def uvicorn() -> None:
    if sys.argv[1:] == ["backend"]:
        sys.argv = [sys.argv[0], "backend.app:app", "--reload"]

    uvicorn_main()
