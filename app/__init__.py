"""INITIALIZE APP"""
# pylint: disable=E0401
from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
session = Session()

def create_buu():
    """ CREATE, REGISTER AND COMPILE """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    session.init_app(app)

    # pylint: disable=C0415
    with app.app_context():
        # Import app/home/routes.py
        from .home.routes import main_blueprint
        # Import app/auth/routes.py
        from .auth.routes import auth_blueprint
        # Initialize assets from app/assets.py
        from .assets import compile_static_assets

        # Register the blueprints that are describe in the routes.py
        app.register_blueprint(main_blueprint)
        app.register_blueprint(auth_blueprint)

        # Print the message in the cli that these blueprints have been enabled.
        for blueprint_name, blueprint in app.blueprints.items():
            print(f"Blueprint Name: {blueprint_name}, Blueprint Object: {blueprint}")


        # Create static asset bundles from assets.py
        compile_static_assets(app)
        # Create Database Models
        db.create_all()

        return app
