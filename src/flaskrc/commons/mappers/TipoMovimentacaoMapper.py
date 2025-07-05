from flaskrc.commons.dtos.TipoMovimentacaoDTO import TipoMovimentacaoDTO
from flaskrc.commons.mappers.ModelMapperGenerico import converter_para_dicionario
from flaskrc.models.TipoMovimentacao import TipoMovimentacao


class TipoMovimentacaoMapper:

    def converter_para_tipo_mov_dto(
            self,
            produto: TipoMovimentacao,
            campos_ignorados: list=[]
        ) -> TipoMovimentacaoDTO:
        campos_ignorados_padrao = ["indicador_movimento", "Movimentacao_"]
        campos_ignorados.extend(campos_ignorados_padrao)
        return TipoMovimentacaoDTO(**converter_para_dicionario(
                    produto,
                    campos_ignorados=campos_ignorados
                )
            )
