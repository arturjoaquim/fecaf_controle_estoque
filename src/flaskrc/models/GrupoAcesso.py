from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskrc.commons.enums.IndicadorAtivoEnum import IndicadorAtivoEnum
from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm

if TYPE_CHECKING:
    from flaskrc.models.UsuarioAcessoDetalhe import UsuarioAcessoDetalhe

class GrupoAcesso(orm.Model):
    __tablename__ = "GrupoAcesso"

    nome_grupo_acesso: Mapped[str] = mapped_column("nm_grp_acs", Text)
    descricao_grupo_acesso: Mapped[str] = mapped_column("ds_grp_acs", Text)
    indicador_ativo: Mapped[str] = mapped_column("ic_atv", Text)
    data_cadastro: Mapped[date] = mapped_column("dt_cad", Date)
    id_grupo_acesso: Mapped[int] = mapped_column("id_grp_acs", Integer, primary_key=True)

    @property
    def indicador_ativo_enum(self) -> IndicadorAtivoEnum:
        return IndicadorAtivoEnum(self.indicador_ativo)

    @indicador_ativo_enum.setter
    def indicador_ativo_enum(self, value: IndicadorAtivoEnum) -> None:
        self.indicador_ativo = value.value

    UsuarioAcessoDetalhe: Mapped[list["UsuarioAcessoDetalhe"]] = relationship("UsuarioAcessoDetalhe", back_populates="GrupoAcesso_")
