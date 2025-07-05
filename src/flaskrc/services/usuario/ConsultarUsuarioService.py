from typing import TYPE_CHECKING

from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.commons.mappers.UsuarioMapper import UsuarioMapper
from flaskrc.repositories.UsuarioRepository import UsuarioRepository

if TYPE_CHECKING:
    from flaskrc.models.Usuario import Usuario


class ConsultarUsuarioService:

    def __init__(
            self,
            usuario_repository: UsuarioRepository,
            usuario_mapper: UsuarioMapper
        ) -> None:
        self.usuario_repository: UsuarioRepository = usuario_repository
        self.usuario_mapper: UsuarioMapper = usuario_mapper
        self.usuario: Usuario = None

    def consultar_usuario_por_id(self, id_usr: str) -> UsuarioDTO | None:
        self.usuario: Usuario = self.usuario_repository\
            .consultar_usuario_por_id(int(id_usr))

        if self.usuario is None:
            return None

        return self.usuario_mapper.converter_para_usuario_dto(self.usuario)
