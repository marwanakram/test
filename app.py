from flask import Flask, render_template

app = Flask(__name__)

# Make sure 'GET' is allowed (it is by default if you don't list any methods)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
