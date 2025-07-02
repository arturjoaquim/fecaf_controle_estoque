from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint("home", __name__, url_prefix="/")

@bp.route("/", methods=["GET"])
#@login_required
def home() -> str:
    """
        Rota para página inicial.
    """
    return render_template("index.html")
