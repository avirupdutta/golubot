from fastapi.testclient import TestClient

import backend
from backend.lancelot import app


def test_backend_package_exports_asgi_app():
    assert backend.app is app


def test_health_check_reports_service_status():
    response = TestClient(app).get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"service": "lancelot", "status": "ok"}
