from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.commons.mappers.ModelMapperGenerico import converter_para_dicionario
from flaskrc.models.Usuario import Usuario
from flaskrc.repositories.UsuarioRepository import UsuarioRepository


class ConsultarUsuarioService:

    def consultar_usuario_por_id(self, id_usr: str) -> Usuario | None:
        """
        Consulta um usuário pelo ID.
        :param id_usr: ID do usuário a ser consultado.
        :return: Usuário consultado ou None se não encontrado.
        """
        usuario_repository = UsuarioRepository()
        usuario: Usuario = usuario_repository.consultar_usuario_por_id(int(id_usr))

        if usuario is None:
            return None

        dict_usr: dict = converter_para_dicionario(usuario, campos_excluidos=["senha_usr"])  # noqa: E501
        return UsuarioDTO(**dict_usr)
