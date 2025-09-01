from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(message="Hello, DevOps!")

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    # Let containers/cloud set PORT; default to 8000
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
