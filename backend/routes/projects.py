from flask import request, jsonify, Blueprint
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Create blueprint
#-----------------------------------------------------
projects = Blueprint('projects', __name__,
                      url_prefix='/projects',
                      template_folder='templates',
                      static_folder='static')

@projects.route("/", methods=["GET"])
def get_all_projects():
    result = "list of projects"
    return jsonify(result)


@projects.route("/<path:project_id>", methods=["GET"])
def get_project_by_id(project_id):
    try:
        "temp"

        return jsonify({"msg": f"Selected Project-{project_id}"}), 201
    except Exception as e:
        "temp"
        return jsonify({"error": str(e)}), 500