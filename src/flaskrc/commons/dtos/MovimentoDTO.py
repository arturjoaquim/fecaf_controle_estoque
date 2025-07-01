from dataclasses import dataclass, field
from datetime import date


@dataclass
class MovimentoDTO:
    id_produto: int = None
    id_tipo_movimento: int = None
    quantia_movimentada: int = None
    data_movimentacao: date = None
    data_cadastro: date = field(default_factory=date.today)
    id_usuario: int = None
    id_movimentacao: int = None
