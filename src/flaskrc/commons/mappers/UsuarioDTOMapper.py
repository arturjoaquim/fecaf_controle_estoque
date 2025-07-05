from marshmallow import Schema, fields, post_load

from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO
from flaskrc.commons.enums.IndicadorAtivoEnum import IndicadorAtivoEnum


class UsuarioDTOMapper(Schema):
    id_usr = fields.Int(data_key="idUsuario")
    nome_usr = fields.Str(data_key="nomeUsuario")
    data_cadastro = fields.Date(data_key="dataCadastro")
    indicador_ativo_enum = fields.Enum(IndicadorAtivoEnum, by_value=False, data_key="indicadorAtivo")  # noqa: E501
    senha_usr = fields.Str(data_key="senhaUsuario")

    def __init__(self, *, campos_obrigatorios: list | None=None, **keyargs: any) -> None:  # noqa: E501
        super().__init__(**keyargs)
        if campos_obrigatorios is not None:
            for campo_obrigatorio in campos_obrigatorios:
                if campo_obrigatorio in self.fields:
                    self.fields[campo_obrigatorio].required = True

    @post_load
    def converter_para_usuariodto(self, dados: dict, **kwargs: any) -> UsuarioDTO:
        return UsuarioDTO(**dados)
