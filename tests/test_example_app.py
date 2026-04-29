import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.example_app import app


def test_index():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "portfolio lab" in resp.get_data(as_text=True)


def test_healthz():
    client = app.test_client()
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert "status" in resp.get_data(as_text=True)
