from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm

if TYPE_CHECKING:

    from flaskrc.models.Produto import Produto
    from flaskrc.models.TipoMovimentacao import TipoMovimentacao
    from flaskrc.models.Usuario import Usuario


class Movimentacao(orm.Model):
    __tablename__ = "Movimentacao"

    id_prd: Mapped[int] = mapped_column(ForeignKey("Produto.id_prd"))
    id_tp_mov: Mapped[int] = mapped_column(ForeignKey("TipoMovimentacao.id_tp_mov"))
    qtd_mov: Mapped[int] = mapped_column(Integer)
    dt_mov: Mapped[date] = mapped_column(Date)
    dt_cad: Mapped[date] = mapped_column(Date)
    id_usr: Mapped[int] = mapped_column(ForeignKey("Usuario.id_usr"))
    id_mov: Mapped[int] = mapped_column(Integer, primary_key=True)

    Produto_: Mapped["Produto"] = relationship("Produto", back_populates="Movimentacao")
    TipoMovimentacao_: Mapped["TipoMovimentacao"] = relationship("TipoMovimentacao", back_populates="Movimentacao")
    Usuario_: Mapped["Usuario"] = relationship("Usuario", back_populates="Movimentacao")
