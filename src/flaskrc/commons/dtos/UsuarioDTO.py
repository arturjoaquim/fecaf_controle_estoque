from dataclasses import dataclass
from datetime import date

from flaskrc.commons.enums.IndicadorAtivoEnum import IndicadorAtivoEnum


@dataclass
class UsuarioDTO:

    id_usr: int = None
    nome_usr: str = None
    data_cadastro: date = None
    indicador_ativo_enum: IndicadorAtivoEnum = None
    senha_usr: str = None
    is_authenticated: bool = None
    is_anonymous: bool = False
    is_active: bool = None

    def __init__(self,
                id_usr: int|None=None,
                nome_usr:str|None=None,
                data_cadastro:date|None=None,
                indicador_ativo_enum:IndicadorAtivoEnum|None=None,
                senha_usr: str|None=None, *,
                is_authenticated:bool=True,
                is_anonymous:bool=False) -> None:
        self.id_usr = id_usr
        self.nome_usr = nome_usr
        self.data_cadastro = data_cadastro
        self.indicador_ativo_enum = indicador_ativo_enum
        self.senha_usr = senha_usr
        self.is_authenticated = is_authenticated
        self.is_anonymous = is_anonymous
        self.is_active = (indicador_ativo_enum is not None and indicador_ativo_enum.value == IndicadorAtivoEnum.ATIVO.value)  # noqa: E501

    def get_id(self) -> str:
        return str(self.id_usr)
