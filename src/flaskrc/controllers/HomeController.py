from flask import Blueprint
from flask_login import login_required

bp = Blueprint("home", __name__, url_prefix="/")

@bp.route("/", methods=["GET"])
@login_required
def home() -> str:
    """
        Rota para página inicial.
    """
    return "Bem-vindo à página inicial do sistema de controle de estoque!"
