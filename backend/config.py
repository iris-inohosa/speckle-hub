import os
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Path of top-level dir for this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# read .env as dict
path_to_env = os.path.abspath(os.path.join(BASEDIR, '.', '.env'))
config = dotenv_values(path_to_env)


db = SQLAlchemy()
jwt = JWTManager()

class Config(object):
    """
    Base configuration.
    **Flask Documentation: "https://flask.palletsprojects.com/en/2.3.x/config/"
    """
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", default="12435")
    JWT_SECRET_KEY = os.getenv("SECRET_KEY", default="your_jwt_secret_key")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    FLASK_ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
