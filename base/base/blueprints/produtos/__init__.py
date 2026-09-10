from flask import Blueprint
from blueprints.produtos import routes
produtos_bp = Blueprint("produtos",__name__,template_folder="templates")