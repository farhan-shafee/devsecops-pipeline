import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class AppHandler(BaseHTTPRequestHandler):
    def _send_json(self, payload: dict, status_code: int = 200) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/":
            self._send_json({"message": "Hello from the DevSecOps portfolio lab"})
            return

        if self.path == "/healthz":
            api_mode = os.getenv("APP_MODE", "lab")
            self._send_json({"status": "ok", "mode": api_mode})
            return

        self._send_json({"error": "not found"}, status_code=404)

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return


def create_server(host: str = "0.0.0.0", port: int = 8000) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), AppHandler)


def run_server() -> None:
    server = create_server()
    server.serve_forever()


if __name__ == "__main__":
    run_server()
