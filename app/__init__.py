from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config  # imprting Config class from config.py which is in app

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # this is come from config file which is in app

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from app.api.employee_api import employee_bp

    app.register_blueprint(employee_bp, url_prefix="/api/employees")

    return app
