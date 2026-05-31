from os import getenv
from pathlib import Path

from agno.context.wiki import WikiContextProvider
from agno.context.wiki.backend import FileSystemBackend, GitBackend, WikiBackend, git_run
from agno.tools.websearch import WebSearchTools

BACKEND_DIR = Path(__file__).resolve().parents[2]
DEFAULT_WIKI_PATH = BACKEND_DIR / "./knowledge-bases/USASF-Brain"
DEFAULT_WIKI_REPO_URL = "https://github.com/CBD-Enterprise/USASF-Brain"
DEFAULT_WIKI_BRANCH = "main"
DEFAULT_GIT_CLONE_TIMEOUT = 600.0


def get_bool_env(name: str, default: bool) -> bool:
    value = getenv(name)
    if value is None:
        return default
    return value.lower() in {"1", "true", "yes", "on"}


class KnowledgeBaseGitBackend(GitBackend):
    def __init__(
        self,
        *,
        clone_timeout: float,
        shallow_clone: bool,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.clone_timeout = clone_timeout
        self.shallow_clone = shallow_clone

    async def _clone(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        clone_args = [
            "clone",
            "--branch",
            self.branch,
            "--single-branch",
        ]
        if self.shallow_clone:
            clone_args.extend(["--depth", "1"])
        clone_args.extend([self._authenticated_url, str(self.path)])

        await git_run(
            clone_args,
            cwd=self.path.parent,
            scrubber=self._scrubber,
            timeout=self.clone_timeout,
        )
        await git_run(
            ["remote", "set-url", "origin", self._authenticated_url],
            cwd=self.path,
            scrubber=self._scrubber,
            timeout=self.clone_timeout,
        )


def build_wiki_backend() -> WikiBackend:
    local_path = getenv("WIKI_LOCAL_PATH", str(DEFAULT_WIKI_PATH))
    if getenv("WIKI_BACKEND", "git").lower() == "filesystem":
        return FileSystemBackend(path=local_path)

    return KnowledgeBaseGitBackend(
        repo_url=getenv("WIKI_REPO_URL", DEFAULT_WIKI_REPO_URL),
        branch=getenv("WIKI_BRANCH", DEFAULT_WIKI_BRANCH),
        github_token=getenv("GITHUB_TOKEN"),
        local_path=local_path,
        force_clone=get_bool_env("WIKI_FORCE_CLONE", True),
        clone_timeout=float(getenv("WIKI_GIT_CLONE_TIMEOUT", DEFAULT_GIT_CLONE_TIMEOUT)),
        shallow_clone=get_bool_env("WIKI_SHALLOW_CLONE", True),
    )


wiki = WikiContextProvider(backend=build_wiki_backend())


async def setup_wiki() -> None:
    await wiki.asetup()


def build_tools() -> list:
    return [*wiki.get_tools(), WebSearchTools()]
