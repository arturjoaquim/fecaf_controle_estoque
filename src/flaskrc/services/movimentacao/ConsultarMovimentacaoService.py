from flaskrc.commons.dtos.MovimentoDTO import MovimentoDTO
from flaskrc.commons.mappers.MovimentacaoMapper import MovimentacaoMapper
from flaskrc.models.Movimentacao import Movimentacao
from flaskrc.repositories.MovimentacaoRepository import MovimentacaoRepository


class ConsultarMovimentacaoService:
    def __init__(
            self,
            movimentacao_repository: MovimentacaoRepository,
            movimentacao_mapper: MovimentacaoMapper
        ) -> None:
        self.movimentacao_repository: MovimentacaoRepository = movimentacao_repository
        self.mov_mapper = movimentacao_mapper

    def consultar_movimentacoes(self, filtro: MovimentoDTO) -> list[Movimentacao]:
        movimentacoes: list[Movimentacao] = self.movimentacao_repository\
            .consultar_movimentacoes(filtro)
        return [self.mov_mapper.converter_para_mov_dto(mov) for mov in movimentacoes]
