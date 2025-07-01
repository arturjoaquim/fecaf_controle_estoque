from flask_login import LoginManager

from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.services.usuario.ConsultarUsuarioService import (
    ConsultarUsuarioService,
)

login_manager = LoginManager()

@login_manager.user_loader
def carregar_usuario(id_usr: str) -> UsuarioDTO | None:
    consulta_usuario_service = ConsultarUsuarioService()
    return consulta_usuario_service.consultar_usuario_por_id(id_usr)
