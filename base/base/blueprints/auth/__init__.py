from flask import Blueprint
from blueprints.auth import routes
auth_bp = Blueprint("auth",__name__, template_folder="templates")
