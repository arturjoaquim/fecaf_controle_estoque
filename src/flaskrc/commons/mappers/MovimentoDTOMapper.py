from datetime import date

from marshmallow import Schema, fields, post_load

from flaskrc.commons.dtos.MovimentoDTO import MovimentoDTO


class MovimentoDTOMapper(Schema):
    id_movimentacao: int = fields.Int(data_key="idMovimentacao")
    id_produto: int = fields.Int(data_key="idProduto")
    id_tipo_movimento: int = fields.Int(data_key="idTipoMovimento")
    quantia_movimentada: int = fields.Int(data_key="quantiaMovimentada")
    data_movimentacao: date = fields.Date(data_key="dataMovimentacao")
    data_cadastro: date = fields.Date(data_key="dataCadastro")
    id_usuario: int = fields.Int(data_key="idUsuario")

    def __init__(self, *, campos_obrigatorios: list | None=None, **keyargs: any) -> None:  # noqa: E501
        super().__init__(**keyargs)
        if campos_obrigatorios is not None:
            for campo_obrigatorio in campos_obrigatorios:
                if campo_obrigatorio in self.fields:
                    self.fields[campo_obrigatorio].required = True

    @post_load
    def converter_para_movimentodto(self, dados: dict, **kwargs: any) -> MovimentoDTO:
        return MovimentoDTO(**dados)
