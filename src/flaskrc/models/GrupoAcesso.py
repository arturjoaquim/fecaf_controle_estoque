from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import CHAR, Date, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm

if TYPE_CHECKING:
    from flaskrc.models.UsuarioAcessoDetalhe import UsuarioAcessoDetalhe

class GrupoAcesso(orm.Model):
    __tablename__ = "GrupoAcesso"

    nm_grp_acs: Mapped[str] = mapped_column(Text)
    ds_grp_acs: Mapped[str] = mapped_column(Text)
    ic_atv: Mapped[str] = mapped_column(CHAR(1))
    dt_cad: Mapped[date] = mapped_column(Date)
    id_grp_acs: Mapped[int] = mapped_column(Integer, primary_key=True)

    UsuarioAcessoDetalhe: Mapped[list["UsuarioAcessoDetalhe"]] = relationship("UsuarioAcessoDetalhe", back_populates="GrupoAcesso_")
