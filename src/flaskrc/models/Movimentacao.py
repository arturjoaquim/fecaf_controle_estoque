from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskrc.commons.exceptions.NegocioError import NegocioError
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

    Produto_: Mapped["Produto"] = relationship("Produto", back_populates="Movimentacao_")
    TipoMovimentacao_: Mapped["TipoMovimentacao"] = relationship("TipoMovimentacao", back_populates="Movimentacao_")
    Usuario_: Mapped["Usuario"] = relationship("Usuario", back_populates="Movimentacao_")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._validar_data_movimentacao()
        self._validar_quantia_movimentada()

    def _validar_data_movimentacao(self) -> None:
        def _data_movimentacao_futura(self: "Movimentacao") -> None:
            if self.data_movimentacao > date.today():
                msg = "Data de movimentação não pode ser futura."
                raise NegocioError(msg)

        _data_movimentacao_futura(self)

    def _validar_quantia_movimentada(self) -> None:
        def _quantia_menor_igual_zero(self: "Movimentacao") -> None:
            if self.quantia_movimentada <= 0:
                msg = "Quantia movimentada deve ser maior que zero."
                raise NegocioError(msg)

        _quantia_menor_igual_zero(self)
