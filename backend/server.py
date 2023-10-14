from flask import Flask
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
def home():
    return "<a href=\"api/ui\">Click here for API UI</a>"

if __name__ == "__main__":
    capp.run(host="0.0.0.0", port=8000, debug=True)