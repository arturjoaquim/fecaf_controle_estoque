from http import HTTPStatus

from flask import abort, flash, redirect, request
from flask_login import LoginManager

from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.repositories.UsuarioRepository import UsuarioRepository
from flaskrc.services.usuario.ConsultarUsuarioService import (
    ConsultarUsuarioService,
)

login_manager = LoginManager()

@login_manager.user_loader
def carregar_usuario(id_usr: str) -> UsuarioDTO | None:
    consulta_usuario_service = ConsultarUsuarioService(UsuarioRepository())
    return consulta_usuario_service.consultar_usuario_por_id(id_usr)

@login_manager.unauthorized_handler
def unauthorized() -> str:
    if request.blueprint.__contains__("api"):
        abort(HTTPStatus.UNAUTHORIZED)
    flash("Por favor, se autentique para acessar essa página.", "info")
    return redirect("/usuario/autenticar", code=302)
