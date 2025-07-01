from flaskrc.commons.dtos.MovimentoDTO import MovimentoDTO
from flaskrc.commons.mappers.ModelMapperGenerico import (
    converter_para_dicionario,
)
from flaskrc.models.Movimentacao import Movimentacao
from flaskrc.repositories.MovimentacaoRepository import MovimentacaoRepository


class ConsultarMovimentacaoService:
    def __init__(self, movimentacao_repository: MovimentacaoRepository) -> None:
        self.movimentacao_repository: MovimentacaoRepository = movimentacao_repository

    def consultar_movimentacoes(self, filtro: MovimentoDTO) -> list[Movimentacao]:
        movimentacoes: list[Movimentacao] = self.movimentacao_repository\
            .consultar_movimentacoes(filtro)
        return [MovimentoDTO(**converter_para_dicionario(mov)) for mov in movimentacoes]
