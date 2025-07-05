from typing import TYPE_CHECKING

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user

from flaskrc.commons.mappers.UsuarioDTOMapper import UsuarioDTOMapper
from flaskrc.commons.mappers.UsuarioMapper import UsuarioMapper
from flaskrc.controllers.ControllerBase import trata_excecao_form
from flaskrc.repositories.UsuarioRepository import UsuarioRepository
from flaskrc.services.usuario.AutenticarUsuarioService import AutenticarUsuarioService
from flaskrc.services.usuario.RegistrarUsuarioService import RegistrarUsuarioService

if TYPE_CHECKING:
    from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO

bp = Blueprint("usuario", __name__, url_prefix="/usuario")
bp_api = Blueprint("api-usuario", __name__, url_prefix="/api/usuario")

registrar_usuario_service = RegistrarUsuarioService(UsuarioRepository(), UsuarioMapper())
autenticar_usuario_service = AutenticarUsuarioService(UsuarioRepository(), UsuarioMapper())

@bp.route("/registrar", methods=["GET", "POST"])
@trata_excecao_form("registro")
def registrar_usuario() -> None | str:
    if (request.method == "POST"):
        usuario_dto_mapper = UsuarioDTOMapper(campos_obrigatorios=["nome_usuario", "senha_usr"])  # noqa: E501
        usuario_dto: UsuarioDTO = usuario_dto_mapper.load(request.form)
        novo_usuario: UsuarioDTO = registrar_usuario_service.registrar_usuario(usuario_dto)  # noqa: E501
        print(usuario_dto)
        print(novo_usuario)
        flash("Usuario registrado com sucesso")

    return "registro" # TODO @<ARTUR>: implementar pagina de registro

@bp.route("/autenticar", methods=["GET", "POST"])
@trata_excecao_form("usuario.autenticar_usuario")
def autenticar_usuario()-> None | str:
    if (request.method == "POST"):
        usuario_dto_mapper = UsuarioDTOMapper(campos_obrigatorios=["nome_usuario", "senha_usr"])  # noqa: E501
        usuario_dto: UsuarioDTO = usuario_dto_mapper.load(request.form)
        usuario_autenticado = autenticar_usuario_service.autenticar_usuario(usuario_dto.nome_usr, usuario_dto.senha_usr)  # noqa: E501
        login_user(usuario_autenticado)
        flash("Autenticação realizada com sucesso.", category="success")
        print("Sucesso")
        return redirect(url_for("home.home"), code=302)
    return render_template("autenticar-usuario.html")
