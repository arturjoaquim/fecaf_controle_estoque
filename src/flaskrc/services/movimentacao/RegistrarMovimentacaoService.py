

from datetime import date
from typing import TYPE_CHECKING

from flaskrc.commons.dtos.MovimentoDTO import MovimentoDTO
from flaskrc.commons.enums.IndicadorMovimentoEnum import IndicadorMovimentoEnum
from flaskrc.commons.exceptions.NegocioError import NegocioError
from flaskrc.commons.mappers.ModelMapperGenerico import (
    converter_dto_para_model,
    converter_para_dicionario,
)
from flaskrc.models.Movimentacao import Movimentacao
from flaskrc.repositories.MovimentacaoRepository import MovimentacaoRepository
from flaskrc.repositories.ProdutoRepository import ProdutoRepository
from flaskrc.repositories.TipoMovimentacaoRepository import TipoMovimentacaoRepository

if TYPE_CHECKING:
    from flaskrc.models.TipoMovimentacao import TipoMovimentacao


class RegistrarMovimentacaoService:

    def __init__(
            self,
            movimento_repository: MovimentacaoRepository,
            tipo_movimentacao_repository: TipoMovimentacaoRepository,
            produto_repository: ProdutoRepository
        ) -> None:
        self.movimento_repository = movimento_repository
        self.tipo_movimentacao_repository = tipo_movimentacao_repository
        self.produto_repository = produto_repository
        self.movimento: Movimentacao = None

    def registrar_movimento(
        self,
        movimento_dto: MovimentoDTO,
        id_usr: int
    ) -> MovimentoDTO:
        self.movimento: Movimentacao = converter_dto_para_model(
            movimento_dto, Movimentacao
        )
        self.movimento.id_usuario = id_usr
        self.movimento.data_cadastro = date.today()

        self._validar_estoque_disponivel()
        self.movimento = self.movimento_repository.registrar_movimento(self.movimento)
        return MovimentoDTO(**converter_para_dicionario(self.movimento))

    def _validar_estoque_disponivel(self) -> None:
        tipo_movimentacao: TipoMovimentacao = self.tipo_movimentacao_repository\
            .consultar_tipo_movimentacao_por_id(self.movimento.id_tipo_movimento)
        if tipo_movimentacao.indicador_movimento == IndicadorMovimentoEnum.SAIDA.value:
            quantia_disponivel = self.produto_repository.consultar_produto_por_id(
                self.movimento.id_produto
            ).estoque
            if quantia_disponivel < self.movimento.quantia_movimentada:
                msg = "Estoque insuficiente para realizar a movimentação."
                raise NegocioError(msg)
