from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.example_app import add_numbers, app, health_payload, run_server


def test_add_numbers_returns_sum() -> None:
    assert add_numbers(2, 3) == 5


def test_health_payload_is_stable() -> None:
    assert health_payload() == {"status": "ok", "service": "example-app"}


def test_health_route_returns_payload() -> None:
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json() == health_payload()


def test_healthz_route_matches_container_probe() -> None:
    response = app.test_client().get("/healthz")

    assert response.status_code == 200
    assert response.get_json() == health_payload()


def test_unknown_route_returns_404() -> None:
    response = app.test_client().get("/missing")

    assert response.status_code == 404


def test_run_server_delegates_to_flask_app(monkeypatch) -> None:
    called_with = {}

    def fake_run(*, host: str, port: int) -> None:
        called_with["host"] = host
        called_with["port"] = port

    monkeypatch.setattr(app, "run", fake_run)

    run_server(host="0.0.0.0", port=8080)

    assert called_with == {"host": "0.0.0.0", "port": 8080}
