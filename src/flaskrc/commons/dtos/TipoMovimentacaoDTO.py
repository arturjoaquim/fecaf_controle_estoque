from dataclasses import dataclass
from datetime import date

from flaskrc.commons.enums.IndicadorMovimentoEnum import IndicadorMovimentoEnum


@dataclass
class TipoMovimentacaoDTO:
    id_tipo_mov: int = None
    nome_tipo_mov: str = None
    descricao_tipo_mov: str = None
    indicador_movimento_enum: IndicadorMovimentoEnum = None
    data_cadastro: date = None
