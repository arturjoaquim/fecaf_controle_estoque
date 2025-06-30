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

    id_produto: Mapped[int] = mapped_column("id_prd", ForeignKey("Produto.id_prd"))
    id_tipo_movimento: Mapped[int] = mapped_column("id_tp_mov", ForeignKey("TipoMovimentacao.id_tp_mov"))
    quantia_movimentada: Mapped[int] = mapped_column("qtd_mov", Integer)
    data_movimentacao: Mapped[date] = mapped_column("dt_mov", Date)
    data_cadastro: Mapped[date] = mapped_column("dt_cad", Date)
    id_usuario: Mapped[int] = mapped_column("id_usr", ForeignKey("Usuario.id_usr"))
    id_movimentacao: Mapped[int] = mapped_column("id_mov", Integer, primary_key=True)

    Produto_: Mapped["Produto"] = relationship("Produto", back_populates="Movimentacao")
    TipoMovimentacao_: Mapped["TipoMovimentacao"] = relationship("TipoMovimentacao", back_populates="Movimentacao")
    Usuario_: Mapped["Usuario"] = relationship("Usuario", back_populates="Movimentacao")
