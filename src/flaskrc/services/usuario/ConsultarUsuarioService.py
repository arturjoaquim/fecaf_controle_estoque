from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.commons.mappers.ModelMapperGenerico import converter_para_dicionario
from flaskrc.models.Usuario import Usuario
from flaskrc.repositories.UsuarioRepository import UsuarioRepository


class ConsultarUsuarioService:

    def __init__(self, usuario_repository: UsuarioRepository) -> None:
        self.usuario_repository: UsuarioRepository = usuario_repository
        self.usuario: Usuario = None

    def consultar_usuario_por_id(self, id_usr: str) -> Usuario | None:
        self.usuario: Usuario = self.usuario_repository\
            .consultar_usuario_por_id(int(id_usr))

        if self.usuario is None:
            return None

        dict_usr: dict = converter_para_dicionario(self.usuario, campos_excluidos=["senha_usr"])  # noqa: E501
        return UsuarioDTO(**dict_usr)
