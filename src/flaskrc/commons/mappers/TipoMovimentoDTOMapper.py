from datetime import date

from marshmallow import Schema, fields, post_load

from flaskrc.commons.dtos.TipoMovimentacaoDTO import TipoMovimentacaoDTO
from flaskrc.commons.enums.IndicadorMovimentoEnum import IndicadorMovimentoEnum


class TipoMovimentoDTOMapper(Schema):
    id_tipo_mov = fields.Int(data_key="idTipoMov")
    nome_tipo_mov = fields.Str(data_key="nomeTipoMov")
    descricao_tipo_mov = fields.Str(data_key="descricaoTipMov")
    indicador_movimento_enum = fields.Enum(IndicadorMovimentoEnum, by_value=False)
    data_cadastro: date

    def __init__(self, *, campos_obrigatorios: list | None=None, **keyargs: any) -> None:  # noqa: E501
        super().__init__(**keyargs)
        if campos_obrigatorios is not None:
            for campo_obrigatorio in campos_obrigatorios:
                if campo_obrigatorio in self.fields:
                    self.fields[campo_obrigatorio].required = True

    @post_load
    def converter_para_produtodto(self, dados: dict, **kwargs: any) -> TipoMovimentacaoDTO:
        return TipoMovimentacaoDTO(**dados)