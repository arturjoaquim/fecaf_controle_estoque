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

    nm_tp_mov: Mapped[str] = mapped_column(Text)
    ds_tp_mov: Mapped[str] = mapped_column(Text)
    ic_mov: Mapped[str] = mapped_column(CHAR(1))
    dt_cad: Mapped[date] = mapped_column(Date)
    id_tp_mov: Mapped[int] = mapped_column(Integer, primary_key=True)

    Movimentacao: Mapped[list["Movimentacao"]] = relationship("Movimentacao", back_populates="TipoMovimentacao_")
