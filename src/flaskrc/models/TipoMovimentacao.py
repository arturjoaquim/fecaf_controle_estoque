from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import CHAR, Date, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm

if TYPE_CHECKING:

    from flaskrc.models.Movimentacao import Movimentacao


class TipoMovimentacao(orm.Model):
    __tablename__ = "TipoMovimentacao"

    nome_tipo_mov: Mapped[str] = mapped_column("nm_tp_mov", Text)
    descricao_tipo_mov: Mapped[str] = mapped_column("ds_tp_mov", Text)
    indicador_movimento: Mapped[str] = mapped_column("ic_mov", CHAR(1))
    data_cadastro: Mapped[date] = mapped_column("dt_cad", Date)
    id_tipo_mov: Mapped[int] = mapped_column("id_tp_mov", Integer, primary_key=True)

    Movimentacao: Mapped[list["Movimentacao"]] = relationship("Movimentacao", back_populates="TipoMovimentacao_")
