from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm

if TYPE_CHECKING:
    from flaskrc.models.GrupoAcesso import GrupoAcesso
    from flaskrc.models.Usuario import Usuario

class UsuarioAcessoDetalhe(orm.Model):
    __tablename__ = "UsuarioAcessoDetalhe"

    id_usr: Mapped[int] = mapped_column(ForeignKey("Usuario.id_usr"))
    id_grp_acs: Mapped[int] = mapped_column(ForeignKey("GrupoAcesso.id_grp_acs"))
    id_usr_dtl: Mapped[int] = mapped_column(Integer, primary_key=True)

    GrupoAcesso_: Mapped['GrupoAcesso'] = relationship('GrupoAcesso', back_populates='UsuarioAcessoDetalhe')
    Usuario_: Mapped['Usuario'] = relationship('Usuario', back_populates='UsuarioAcessoDetalhe')

