"""Minimal Flask example app for DevSecOps pipeline demos."""

from flask import Flask, Response, jsonify


app = Flask(__name__)


def add_numbers(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def health_payload() -> dict[str, str]:
    """Return a simple service health payload."""
    return {"status": "ok", "service": "example-app"}


@app.get("/health")
@app.get("/healthz")
def health() -> tuple[Response, int]:
    """Return service health for local checks and container probes."""
    return jsonify(health_payload()), 200


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Run the development server for local demonstration."""
    app.run(host=host, port=port)


if __name__ == "__main__":
    run_server()
