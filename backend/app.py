import os
from flask import Flask, jsonify
from flask_cors import CORS
from routes.projects import projects
from routes.auth import auth

from models import User

from flask_login import LoginManager
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from specklepy.api.client import SpeckleClient

from config import db, jwt
# -------------
# Configuration
# -------------


# ----------------------------
# Application Factory Function
# ----------------------------
def create_app():
    # Create Flask application
    app = Flask(__name__)

    # configure the Flask app
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    # Initialize the extensions with the app
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)  # Allow cross-origin requests for React frontend

    # Create the database tables
    with app.app_context():
        db.create_all()

    register_blueprints(app)


    # -----------------------------------------
    # Test index route to see if app is running
    # -----------------------------------------
    @app.route("/")
    @jwt_required()
    def protected():
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        return jsonify(logged_in_as=user.username), 200
    

    return app

# ----------------
# Helper functions
# ----------------
def register_blueprints(app):
    app.register_blueprint(projects)
    app.register_blueprint(auth)

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5005)