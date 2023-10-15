import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

connex_app = connexion.App(__name__, specification_dir="./")
app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipe.db"

# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
