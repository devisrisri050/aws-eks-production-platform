from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "AWS EKS DevOps Platform is running!",
        "environment": os.getenv("ENVIRONMENT", "dev"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    }

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)