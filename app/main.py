from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import socket
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "dev")
GIT_COMMIT = os.getenv("GIT_COMMIT", "unknown")

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests to the Flask application"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()

    return jsonify({
        "message": os.getenv("APP_MESSAGE", "Hello from Kubernetes"),
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "local"),
        "version": APP_VERSION,
        "git_commit": GIT_COMMIT,
        "api_key_loaded": bool(os.getenv("API_KEY"))
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/version")
def version():
    return jsonify({
        "version": APP_VERSION,
        "git_commit": GIT_COMMIT
    })

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)