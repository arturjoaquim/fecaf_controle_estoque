from dataclasses import dataclass
from datetime import date

from flaskrc.commons.enums.IndicadorAtivoEnum import IndicadorAtivoEnum


@dataclass
class ProdutoDTO:
    id_produto: int = None
    nome_produto: str = None
    descricao_produto: str = None
    indicador_ativo_enum: IndicadorAtivoEnum = None
    quantia_estoque_minimo: int = None
    id_usuario: int = None
    data_cadastro: date = None
    quantia_estoque: int = None
