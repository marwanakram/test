from flask import Flask, render_template
import time

app = Flask(__name__)

# Simulate readiness delay (app "warms up" for 5 seconds after start)
START_TIME = time.time()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    # Liveness: is the process alive and not deadlocked?
    return "OK", 200

@app.route('/ready')
def ready():
    # Readiness: is the app warmed up and ready to serve traffic?
    if time.time() - START_TIME < 5:
        return "Not ready yet", 503   # <-- OpenShift won't route traffic until this returns 200
    return "Ready", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
