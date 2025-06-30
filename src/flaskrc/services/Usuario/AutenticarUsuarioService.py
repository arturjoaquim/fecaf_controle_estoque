from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.commons.exceptions.NegocioError import NegocioError
from flaskrc.commons.mappers.ModelMapperGenerico import converter_para_dicionario
from flaskrc.models.Usuario import Usuario
from flaskrc.repositories.UsuarioRepository import UsuarioRepository


class AutenticarUsuarioService:

    usuario: Usuario

    def autenticar_usuario(self, nome_usr: str, senha_usr:str) -> UsuarioDTO:
        usuario_repository: UsuarioRepository = UsuarioRepository()
        self.usuario: Usuario = usuario_repository.consultar_usuario_por_nome(nome_usr)
        self.validar_usuario_existe()
        self.validar_senha(senha_usr)
        return UsuarioDTO(**converter_para_dicionario(self.usuario, campos_excluidos=["psw_usr"]))  # noqa: E501

    def validar_usuario_existe(self) -> None:
        if self.usuario is None:
            msg = "Usuario não existe"
            raise NegocioError(msg)

    def validar_senha(self, senha_usr:str) -> None:
        ph = PasswordHasher()

        try:
            ph.verify(self.usuario.senha_usr, senha_usr)
        except VerifyMismatchError as error:
            msg = "Usuario ou senha inválidos"
            raise NegocioError(msg) from error

