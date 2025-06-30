from flask import Blueprint, request

bp = Blueprint("autenticacao", __name__, url_prefix="/autenticacao")
bp_api = Blueprint("api-autenticacao", __name__, url_prefix="/api/autenticacao")

@bp.route("/registro", methods=["GET", "POST"])
def registrar_usuario() -> None | str:
    if (request.method == "POST"):
        return None # TODO @<ARTUR>: implementar registro de usuario

    return "registro" # TODO @<ARTUR>: implementar pagina de registro
