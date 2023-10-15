from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import connexion

capp = connexion.App(__name__, specification_dir="./")
capp.add_api("swagger.yml")
app = capp.app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

if __name__ == "__main__":
    capp.run(host="0.0.0.0", port=8000, debug=True)