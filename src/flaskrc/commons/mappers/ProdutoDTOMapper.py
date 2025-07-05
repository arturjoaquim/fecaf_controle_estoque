from marshmallow import Schema, fields, post_load

from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.enums.IndicadorAtivoEnum import IndicadorAtivoEnum


class ProdutoDTOMapper(Schema):
    id_produto = fields.Int(data_key="idProduto")
    nome_produto = fields.Str(data_key="nomeProduto")
    descricao_produto = fields.Str(data_key="descricaoProduto")
    indicador_ativo_enum = fields.Enum(IndicadorAtivoEnum, by_value=False, data_key="indicadorAtivo")  # noqa: E501
    quantia_estoque_minimo = fields.Int(data_key="quantiaEstoqueMinimo")
    id_usuario = fields.Int(data_key="idUsuarioCriador")
    data_cadastro = fields.Date(data_key="dataCadastro")
    quantia_estoque = fields.Int(data_key="quantiaEstoque")

    def __init__(self, *, campos_obrigatorios: list | None=None, **keyargs: any) -> None:  # noqa: E501
        super().__init__(**keyargs)
        if campos_obrigatorios is not None:
            for campo_obrigatorio in campos_obrigatorios:
                if campo_obrigatorio in self.fields:
                    self.fields[campo_obrigatorio].required = True

    @post_load
    def converter_para_produtodto(self, dados: dict, **kwargs: any) -> ProdutoDTO:
        return ProdutoDTO(**dados)
