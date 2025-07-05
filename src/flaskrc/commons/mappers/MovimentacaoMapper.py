from flaskrc.commons.dtos.MovimentoDTO import MovimentoDTO
from flaskrc.commons.mappers.ModelMapperGenerico import converter_para_dicionario
from flaskrc.models.Movimentacao import Movimentacao


class MovimentacaoMapper:

    def converter_para_mov_dto(
            self,
            movimentacao: Movimentacao,
            campos_ignorados: list | None=None
        ) -> MovimentoDTO:
        if campos_ignorados is None:
            campos_ignorados = []
        campos_ignorados_padrao = ["Produto_", "Usuario_", "TipoMovimentacao_"]
        campos_ignorados = campos_ignorados + campos_ignorados_padrao
        return MovimentoDTO(**converter_para_dicionario(
                    movimentacao,
                    campos_ignorados=campos_ignorados
                )
            )
