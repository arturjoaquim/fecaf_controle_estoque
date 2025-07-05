from typing import TYPE_CHECKING

from flaskrc.commons.dtos.TipoMovimentacaoDTO import TipoMovimentacaoDTO
from flaskrc.commons.mappers.TipoMovimentacaoMapper import (
    TipoMovimentacaoMapper,
)
from flaskrc.repositories.TipoMovimentacaoRepository import TipoMovimentacaoRepository

if TYPE_CHECKING:
    from flaskrc.models.TipoMovimentacao import TipoMovimentacao


class ConsultarTipoMovimentacaoService:

    def __init__(
            self,
            tipo_movimentacao_repository:TipoMovimentacaoRepository,
            tipo_mov_mapper: TipoMovimentacaoMapper
        ) ->None:
        self.tipo_movimentacao_repository = tipo_movimentacao_repository
        self.tipo_mov_mapper: TipoMovimentacaoMapper = tipo_mov_mapper

    def consultar_id_tipo_movimentacao_por_nome(
            self,
            nome_tipo_movimentacao: str
        ) -> list[TipoMovimentacaoDTO]:

        tipos_mov: list[TipoMovimentacao] = self.tipo_movimentacao_repository\
            .consultar_id_tipo_movimentacao_por_nome(nome_tipo_movimentacao)
        return [self.tipo_mov_mapper.converter_para_tipo_mov_dto(tipo_mov) for tipo_mov in tipos_mov]  # noqa: E501
