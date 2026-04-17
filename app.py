from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# This is the path where we will mount our Persistent Volume
DATA_FILE = "/var/data/storage.txt"

# Ensure the directory exists (to avoid errors during local testing)
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

HTML_TEMPLATE = """
<html>
    <body>
        <h1>OpenShift PV Logger</h1>
        <form method="POST">
            <input type="text" name="user_data" placeholder="Enter something to save ya a7a..." required>
            <button type="submit">Save to PV</button>
        </form>
        <h3>Saved Data:</h3>
        <pre>{{ saved_content }}</pre>
    </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_data')
        # Append data to the file in the PV
        with open(DATA_FILE, "a") as f:
            f.write(user_input )
            
    # Read the data back to show it works
    content = ""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            content = f.read()
            
    return render_template_string(HTML_TEMPLATE, saved_content=content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
