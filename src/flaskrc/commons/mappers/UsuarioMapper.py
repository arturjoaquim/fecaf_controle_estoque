from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.commons.mappers.ModelMapperGenerico import converter_para_dicionario
from flaskrc.models.Usuario import Usuario


class UsuarioMapper:

    def converter_para_usuario_dto(
            self,
            produto: Usuario,
            campos_ignorados: list=[]
        ) -> UsuarioDTO:
        campos_ignorados_padrao = [
            "indicador_ativo",
            "Produto_",
            "UsuarioAcessoDetalhe",
            "Movimentacao_"
        ]
        campos_ignorados.extend(campos_ignorados_padrao)
        return UsuarioDTO(**converter_para_dicionario(
                    produto,
                    campos_ignorados=campos_ignorados
                )
            )
