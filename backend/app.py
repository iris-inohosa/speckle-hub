import os
from flask import Flask
from flask_cors import CORS
from routes.projects import projects

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

    register_blueprints(app)


    # -----------------------------------------
    # Test index route to see if app is running
    # -----------------------------------------
    @app.route("/")
    def index():
        return "App is running!"
    return app

# ----------------
# Helper functions
# ----------------
def register_blueprints(app):

    app.register_blueprint(projects)
    # TODO:
    #   - add user blueprint

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5005)