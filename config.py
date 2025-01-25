"""App configuration."""
from os import environ, path, system

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

# pylint: disable=R0903
class Config:
    """Set Flask configuration variables from .env file."""

    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")

    # Flask Config
    FLASK_APP = "main.py"
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SECRET_KEY = environ.get("SECRET_KEY")

    # Flask-Session
    # Cookies, user data
    SESSION_TYPE = "filesystem"


    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # Flask-Assets (Optional)
    LESS_BIN = system("which lessc")
    ASSETS_DEBUG = True
    LESS_RUN_IN_DEBUG = False
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG")
