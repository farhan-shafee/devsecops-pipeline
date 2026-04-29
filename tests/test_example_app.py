import json
import os
import threading
import urllib.request
from http.server import ThreadingHTTPServer

from src.example_app import AppHandler


def _start_server() -> tuple[ThreadingHTTPServer, int]:
    server = ThreadingHTTPServer(("127.0.0.1", 0), AppHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, server.server_address[1]


def _get_json(url: str) -> tuple[int, dict]:
    with urllib.request.urlopen(url, timeout=5) as response:
        payload = json.loads(response.read().decode("utf-8"))
        return response.status, payload


def test_index():
    server, port = _start_server()
    try:
        status, payload = _get_json(f"http://127.0.0.1:{port}/")
        assert status == 200
        assert "portfolio lab" in payload["message"]
    finally:
        server.shutdown()
        server.server_close()


def test_healthz():
    server, port = _start_server()
    os.environ["APP_MODE"] = "test"
    try:
        status, payload = _get_json(f"http://127.0.0.1:{port}/healthz")
        assert status == 200
        assert payload["status"] == "ok"
        assert payload["mode"] == "test"
    finally:
        os.environ.pop("APP_MODE", None)
        server.shutdown()
        server.server_close()
