from fastapi.testclient import TestClient

from ml_evaluation_platform.api.main import app

client = TestClient(app)


def test_health_endpoint_returns_service_metadata() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "ml-evaluation-platform",
        "version": "0.1.0",
    }
