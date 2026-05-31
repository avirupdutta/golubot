from fastapi.testclient import TestClient

import backend
from backend.app import app
from backend.bots.lancelot import DEFAULT_WIKI_PATH, agent, wiki
from agno.context.wiki.backend import GitBackend


def test_backend_package_exports_asgi_app():
    assert backend.app is app


def test_health_check_reports_service_status():
    response = TestClient(app).get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"service": "lancelot", "status": "ok"}


def test_agent_registers_wiki_tools_flat():
    tool_names = [getattr(tool, "name", None) for tool in agent.tools]

    assert "query_wiki" in tool_names
    assert "update_wiki" in tool_names


def test_wiki_backend_uses_project_local_path():
    assert wiki.backend.path == DEFAULT_WIKI_PATH
    assert not str(wiki.backend.path).startswith("/repos")


def test_wiki_backend_defaults_to_git_clone():
    assert isinstance(wiki.backend, GitBackend)
    assert getattr(wiki.backend, "clone_timeout") > 120
    assert getattr(wiki.backend, "shallow_clone") is True


def test_app_startup_sets_up_wiki(monkeypatch):
    calls = 0

    async def fake_asetup():
        nonlocal calls
        calls += 1

    monkeypatch.setattr(wiki, "asetup", fake_asetup)

    with TestClient(app) as client:
        response = client.get("/healthz")

    assert response.status_code == 200
    assert calls == 1
