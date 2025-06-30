from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import CHAR, Date, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm

if TYPE_CHECKING:
    from flaskrc.models.UsuarioAcessoDetalhe import UsuarioAcessoDetalhe

class GrupoAcesso(orm.Model):
    __tablename__ = "GrupoAcesso"

    nome_grupo_acesso: Mapped[str] = mapped_column("nm_grp_acs", Text)
    descricao_grupo_acesso: Mapped[str] = mapped_column("ds_grp_acs", Text)
    indicador_ativo: Mapped[str] = mapped_column("ic_atv", CHAR(1))
    data_cadastro: Mapped[date] = mapped_column("dt_cad", Date)
    id_grupo_acesso: Mapped[int] = mapped_column("id_grp_acs", Integer, primary_key=True)

    UsuarioAcessoDetalhe: Mapped[list["UsuarioAcessoDetalhe"]] = relationship("UsuarioAcessoDetalhe", back_populates="GrupoAcesso_")
