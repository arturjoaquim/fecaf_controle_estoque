from flaskrc.commons.dtos.MovimentoDTO import MovimentoDTO
from flaskrc.commons.mappers.ModelMapperGenerico import (
    converter_dto_para_model,
    converter_para_dicionario,
)
from flaskrc.models.Movimentacao import Movimentacao
from flaskrc.repositories.MovimentacaoRepository import MovimentacaoRepository


class ConsultarMovimentacaoService:

    def consultar_movimentacoes(self, filtro: MovimentoDTO) -> list[Movimentacao]:
        movimentacao_repository: MovimentacaoRepository = MovimentacaoRepository()
        filtro_model: Movimentacao = converter_dto_para_model(filtro, Movimentacao)
        movimentacoes: list[Movimentacao] = movimentacao_repository\
            .consultar_movimentacoes(filtro_model)
        return [MovimentoDTO(**converter_para_dicionario(mov)) for mov in movimentacoes]
