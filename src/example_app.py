import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "Hello from the DevSecOps portfolio lab"})


@app.route("/healthz")
def healthcheck():
    api_mode = os.getenv("APP_MODE", "lab")
    return jsonify({"status": "ok", "mode": api_mode})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
