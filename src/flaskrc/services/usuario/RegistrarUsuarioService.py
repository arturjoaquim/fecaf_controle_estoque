from datetime import date

from argon2 import PasswordHasher

from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.commons.enums.IndicadorAtivoEnum import IndicadorAtivoEnum
from flaskrc.commons.mappers.ModelMapperGenerico import (
    converter_dto_para_model,
)
from flaskrc.commons.mappers.UsuarioMapper import UsuarioMapper
from flaskrc.models.Usuario import Usuario
from flaskrc.repositories.UsuarioRepository import UsuarioRepository


class RegistrarUsuarioService:

    def __init__(
            self,
            usuario_repository: UsuarioRepository,
            usuario_mapper: UsuarioMapper
        ) -> None:
        self.usuario_repository: UsuarioRepository = usuario_repository
        self.usuario_mapper: UsuarioMapper = usuario_mapper
        self.usuario: Usuario = None

    def registrar_usuario(self, usr_dto: UsuarioDTO) -> Usuario:
        usr_dto.indicador_ativo_enum = IndicadorAtivoEnum.ATIVO
        usr_dto.data_cadastro = date.today

        self.usuario: Usuario = converter_dto_para_model(usr_dto, Usuario)
        self._criptografar_senha()
        self.usuario = self.usuario_repository.registrar_usuario(self.usuario)

        return self.usuario_mapper.converter_para_usuario_dto(self.usuario)

    def _criptografar_senha(self) -> None:
        ph = PasswordHasher()
        self.usuario.senha_usr = ph.hash(self.usuario.senha_usr)

