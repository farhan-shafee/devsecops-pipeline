"""Minimal standard-library example app for DevSecOps pipeline demos."""

from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps


def add_numbers(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def health_payload() -> dict[str, str]:
    """Return a simple service health payload."""
    return {"status": "ok", "service": "example-app"}


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - method name required by BaseHTTPRequestHandler
        if self.path == "/health":
            payload = dumps(health_payload()).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format: str, *args) -> None:  # noqa: A003 - required override name
        # Intentionally no server-side request logging for this demo app.
        return


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Run a tiny HTTP server for local demonstration."""
    server = HTTPServer((host, port), _Handler)
    server.serve_forever()


if __name__ == "__main__":
    run_server()
