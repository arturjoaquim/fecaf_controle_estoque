from datetime import date

from argon2 import PasswordHasher

from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.commons.mappers.ModelMapperGenerico import (
    converter_dto_para_model,
    converter_para_dicionario,
)
from flaskrc.models.Usuario import Usuario
from flaskrc.repositories.UsuarioRepository import UsuarioRepository


class RegistrarUsuarioService:

    usuario: Usuario

    def registrar_usuario(self, usr_dto: UsuarioDTO) -> Usuario:
        usuario_repository: UsuarioRepository = UsuarioRepository()
        self.usuario: Usuario = converter_dto_para_model(usr_dto, Usuario)
        self.criptografar_senha()
        self.ativar_usuario()
        usuario_repository.registrar_usuario(self.usuario)

        return UsuarioDTO(**converter_para_dicionario(self.usuario, campos_excluidos=["senha_usr"]))

    def criptografar_senha(self) -> None:
        ph = PasswordHasher()
        self.usuario.senha_usr = ph.hash(self.usuario.senha_usr)

    def ativar_usuario(self) -> None:
        self.usuario.indicador_ativo = "A"
        self.usuario.data_cadastro = date.today()
