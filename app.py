from config import app, connex_app, db
from flask import send_from_directory
import os

connex_app.add_api("src/swagger.yml")

@app.route("/")
def base():
    print(app.root_path)
    return send_from_directory(os.path.join(app.root_path, 'client/public'), 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

