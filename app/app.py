
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "AWS DevOps CI/CD Demo",
        "status": "Success",
        "message": "Flask application deployed successfully using Jenkins",
        "version": "7.0",
        "environment": "Development",
        "deployment": "Automated",
        "platform": "AWS EC2",
        "container": "Docker"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy",
        "message": "Application is running successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
