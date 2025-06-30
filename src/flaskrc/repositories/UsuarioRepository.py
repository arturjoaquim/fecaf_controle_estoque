from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm
from flaskrc.models.Usuario import Usuario


class UsuarioRepository:

    def consultar_usuario_por_id(self, id_usuario: int) -> Usuario | None:
        return orm.session.query(Usuario).filter(Usuario.id == id_usuario).first()

    def consultar_usuario_por_nome(self, nome_usuario: str) -> Usuario | None:
        return orm.session.query(Usuario).filter(Usuario.nome_usr == nome_usuario).first()

    def registrar_usuario(self, usuario: Usuario) -> Usuario:
        orm.session.add(usuario)
        orm.session.flush()
        return usuario
