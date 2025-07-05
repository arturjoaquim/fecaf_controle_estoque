from __future__ import annotations

from datetime import date  # noqa: TC003
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer, Text, func, select
from sqlalchemy.orm import Mapped, column_property, mapped_column, relationship

from flaskrc.commons.enums.IndicadorAtivoEnum import IndicadorAtivoEnum
from flaskrc.commons.enums.IndicadorMovimentoEnum import IndicadorMovimentoEnum
from flaskrc.commons.exceptions.NegocioError import NegocioError
from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm
from flaskrc.models.Movimentacao import Movimentacao
from flaskrc.models.TipoMovimentacao import TipoMovimentacao

if TYPE_CHECKING:

    from flaskrc.models.Usuario import Usuario


class Produto(orm.Model):
    __tablename__ = "Produto"

    nome_produto: Mapped[str] = mapped_column("nm_prd", Text)
    descricao_produto: Mapped[str] = mapped_column("ds_prd", Text)
    indicador_ativo: Mapped[str] = mapped_column("ic_atv", Text)
    quantia_estoque_minimo: Mapped[int] = mapped_column("qtd_est_min", Integer)
    id_usuario: Mapped[int] = mapped_column("id_usr", ForeignKey("Usuario.id_usr"))
    data_cadastro: Mapped[date] = mapped_column("dt_cad", Date)
    id_produto: Mapped[int] = mapped_column("id_prd", Integer, primary_key=True)

    @property
    def indicador_ativo_enum(self) -> IndicadorAtivoEnum:
        return IndicadorAtivoEnum(self.indicador_ativo)

    @indicador_ativo_enum.setter
    def indicador_ativo_enum(self, value: IndicadorAtivoEnum) -> None:
        print(value)
        self.indicador_ativo = value.value

    Usuario_: Mapped[Usuario] = relationship("Usuario", back_populates="Produto_")
    Movimentacao_: Mapped[list[Movimentacao]] = relationship("Movimentacao", back_populates="Produto_")  # noqa: E501

    quantia_estoque = column_property(
        select(
            func.coalesce(func.sum(Movimentacao.quantia_movimentada), 0)
        )
        .join(TipoMovimentacao, Movimentacao.id_tipo_movimento == TipoMovimentacao.id_tipo_mov)  # noqa: E501
        .where(
            TipoMovimentacao.indicador_movimento == IndicadorMovimentoEnum.ENTRADA.value,
            Movimentacao.id_produto == id_produto
        ).correlate_except(Movimentacao).scalar_subquery()
        -
        select(
            func.coalesce(func.sum(Movimentacao.quantia_movimentada), 0)
        )
        .join(TipoMovimentacao, Movimentacao.id_tipo_movimento == TipoMovimentacao.id_tipo_mov)  # noqa: E501
        .where(
            TipoMovimentacao.indicador_movimento == IndicadorMovimentoEnum.SAIDA.value,
            Movimentacao.id_produto == id_produto
        ).correlate_except(Movimentacao).scalar_subquery()
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._validar_quantia_estoque_minimo()

    def _validar_quantia_estoque_minimo(self) -> None:
        def _estoque_minimo_negativo(self: "Produto") -> None:
            if (self.quantia_estoque_minimo < 0):
                msg = "Quantia estoque mínimo não pode ser negativo."
                raise NegocioError(msg)
        _estoque_minimo_negativo(self)
