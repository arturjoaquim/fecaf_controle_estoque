from datetime import date

from sqlalchemy import Select, select

from flaskrc.models.Movimentacao import Movimentacao


class MovimentacaoQueryBuilder:
    _consulta: Select[Movimentacao]
    filtro_obrigatorio: bool

    def __init__(
            self,
            consulta:Select[Movimentacao]=None,
            *, filtro_obrigatorio: bool = True
        ) -> None:
        self._consulta = consulta
        self.filtro_obrigatorio = filtro_obrigatorio

    def selecionar_tudo(self) -> "MovimentacaoQueryBuilder":
        self._consulta = select(Movimentacao)
        return self

    def filtro_id_mov(self, id_movimentacao: int) -> "MovimentacaoQueryBuilder":
        self._validar_filtro_obrigatorio(id_movimentacao)

        if id_movimentacao is not None:
            self._consulta = self._consulta.where(
                Movimentacao.id_movimentacao == id_movimentacao
            )
        return self

    def filtro_data_mov(self, data_movimentacao: date) -> "MovimentacaoQueryBuilder":
        self._validar_filtro_obrigatorio(data_movimentacao)

        if data_movimentacao is not None:
            self._consulta = self._consulta.where(
                Movimentacao.data_movimentacao == data_movimentacao
            )
        return self

    def filtro_id_produto(self, id_produto: int) -> "MovimentacaoQueryBuilder":
        self._validar_filtro_obrigatorio(id_produto)

        if id_produto is not None:
            self._consulta = self._consulta.where(Movimentacao.id_produto == id_produto)
        return self

    def filtro_id_usuario(self, id_usuario: int) -> "MovimentacaoQueryBuilder":
        self._validar_filtro_obrigatorio(id_usuario)

        if id_usuario is not None:
            self._consulta = self._consulta.where(Movimentacao.id_usuario == id_usuario)
        return self

    def filtro_id_tipo_mov(
            self,
            id_tipo_movimentacao: int
        ) -> "MovimentacaoQueryBuilder":
        self._validar_filtro_obrigatorio(id_tipo_movimentacao)

        if id_tipo_movimentacao is not None:
            self._consulta = self._consulta.where(
                Movimentacao.id_tipo_movimento == id_tipo_movimentacao
            )
        return self

    def filtro_quantia_movimentada(
            self,
            quantia_movimentada: int
        ) -> "MovimentacaoQueryBuilder":
        self._validar_filtro_obrigatorio(quantia_movimentada)

        if quantia_movimentada is not None:
            self._consulta = self._consulta.where(
                Movimentacao.quantia_movimentada == quantia_movimentada
            )
        return self

    def filtro_data_cadastro(self, data_cadastro: date) -> "MovimentacaoQueryBuilder":
        self._validar_filtro_obrigatorio(data_cadastro)

        if data_cadastro is not None:
            self._consulta = self._consulta.where(
                Movimentacao.data_cadastro == data_cadastro
            )
        return self

    def reiniciar_builder(self) -> "MovimentacaoQueryBuilder":
        self._consulta = None
        return self

    def construir_consulta(self) -> Select[Movimentacao]:
        consulta_final: Select[Movimentacao] = self._consulta
        self.reiniciar_builder()
        return consulta_final

    def _validar_filtro_obrigatorio(self, filtro: object) -> None:
        if self.filtro_obrigatorio and filtro is None:
            msg = "Filtro obrigatório não fornecido."
            raise ValueError(msg)
