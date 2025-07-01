from datetime import date

from sqlalchemy import Select, select

from flaskrc.models.Movimentacao import Movimentacao


class MovimentacaoQueryBuilder:
    def __init__(self) -> None:
        self._consulta: Select[Movimentacao] = select(Movimentacao)

    def filtro_id_mov(self, id_movimentacao: int) -> "MovimentacaoQueryBuilder":
        if id_movimentacao is not None:
            self._consulta = self._consulta.where(
                Movimentacao.id_movimentacao == id_movimentacao
            )
        return self

    def filtro_data_mov(self, data_movimentacao: date) -> "MovimentacaoQueryBuilder":
        if data_movimentacao is not None:
            self._consulta = self._consulta.where(
                Movimentacao.data_movimentacao == data_movimentacao
            )
        return self

    def filtro_id_produto(self, id_produto: int) -> "MovimentacaoQueryBuilder":
        if id_produto is not None:
            self._consulta = self._consulta.where(Movimentacao.id_produto == id_produto)
        return self

    def filtro_id_usuario(self, id_usuario: int) -> "MovimentacaoQueryBuilder":
        if id_usuario is not None:
            self._consulta = self._consulta.where(Movimentacao.id_usuario == id_usuario)
        return self

    def filtro_id_tipo_mov(
            self,
            id_tipo_movimentacao: int
        ) -> "MovimentacaoQueryBuilder":
        if id_tipo_movimentacao is not None:
            self._consulta = self._consulta.where(
                Movimentacao.id_tipo_movimento == id_tipo_movimentacao
            )
        return self

    def filtro_quantia_movimentada(
            self,
            quantia_movimentada: int
        ) -> "MovimentacaoQueryBuilder":
        if quantia_movimentada is not None:
            self._consulta = self._consulta.where(
                Movimentacao.quantia_movimentada == quantia_movimentada
            )
        return self

    def filtro_data_cadastro(self, data_cadastro: date) -> "MovimentacaoQueryBuilder":
        if data_cadastro is not None:
            self._consulta = self._consulta.where(
                Movimentacao.data_cadastro == data_cadastro
            )
        return self

    def reiniciar_builder(self) -> "MovimentacaoQueryBuilder":
        self._consulta = select(Movimentacao)
        return self

    def construir_consulta(self) -> Select[Movimentacao]:
        return self._consulta