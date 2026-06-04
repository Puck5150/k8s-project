from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": os.getenv("APP_MESSAGE", "Hello from Kubernetes"),
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "local"),
        "api_key_loaded": bool(os.getenv("API_KEY"))
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)