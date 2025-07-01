from typing import TYPE_CHECKING

from flask import Blueprint, flash, request
from flask_login import login_user

from flaskrc.commons.mappers.UsuarioDTOMapper import UsuarioDTOMapper
from flaskrc.controllers.ControllerBase import trata_excecao_form
from flaskrc.services.usuario.AutenticarUsuarioService import AutenticarUsuarioService
from flaskrc.services.usuario.RegistrarUsuarioService import RegistrarUsuarioService

if TYPE_CHECKING:
    from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO

bp = Blueprint("usuario", __name__, url_prefix="/usuario")
bp_api = Blueprint("api-usuario", __name__, url_prefix="/api/usuario")

@bp.route("/registrar", methods=["GET", "POST"])
@trata_excecao_form("registro")
def registrar_usuario() -> None | str:
    if (request.method == "POST"):
        registrar_usuario_service = RegistrarUsuarioService()
        usuario_dto_mapper = UsuarioDTOMapper(campos_obrigatorios=["nome_usuario", "senha_usr"])  # noqa: E501
        usuario_dto: UsuarioDTO = usuario_dto_mapper.load(request.form)
        novo_usuario: UsuarioDTO = registrar_usuario_service.registrar_usuario(usuario_dto)  # noqa: E501
        print(usuario_dto)
        print(novo_usuario)
        flash("Usuario registrado com sucesso")

    return "registro" # TODO @<ARTUR>: implementar pagina de registro

@bp.route("/autenticar", methods=["GET", "POST"])
@trata_excecao_form("autenticar")
def autenticar_usuario()-> None | str:
    if (request.method == "POST"):
        autenticar_usuario_service = AutenticarUsuarioService()
        usuario_dto_mapper = UsuarioDTOMapper(campos_obrigatorios=["nome_usuario", "senha_usr"])  # noqa: E501
        usuario_dto: UsuarioDTO = usuario_dto_mapper.load(request.form)
        usuario_autenticado = autenticar_usuario_service.autenticar_usuario(usuario_dto.nome_usr, usuario_dto.senha_usr)  # noqa: E501
        login_user(usuario_autenticado)
        # TODO @<ARTUR>: implementar redirect para pagina inicial
    return "autenticar" # TODO @<ARTUR>: implementar pagina de login
