from dataclasses import dataclass, field
from datetime import date


@dataclass
class ProdutoDTO:
    id_produto: int = 0
    nome_produto: str = ""
    descricao_produto: str = ""
    indicador_ativo: str = ""
    quantia_estoque_minimo: int = 0
    id_usuario: int = 0
    data_cadastro: date = field(default_factory=date.today)
