from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.mappers.ModelMapperGenerico import converter_para_dicionario
from flaskrc.models.Produto import Produto


class ProdutoMapper:

    def converter_para_produto_dto(
            self,
            produto: Produto,
            campos_ignorados: list=[]
        ) -> ProdutoDTO:
        campos_ignorados_padrao = ["indicador_ativo", "Usuario_", "Movimentacao_"]
        campos_ignorados.extend(campos_ignorados_padrao)
        return ProdutoDTO(**converter_para_dicionario(
                    produto,
                    campos_ignorados=campos_ignorados
                )
            )
