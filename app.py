from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Success!</h1><p>OpenShift is running my Python app.</p>"

if __name__ == "__main__":
    # OpenShift expects the app to listen on 0.0.0.0 and port 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
