from dataclasses import dataclass
from datetime import date


@dataclass
class ProdutoDTO:
    id_produto: int = None
    nome_produto: str = None
    descricao_produto: str = None
    indicador_ativo: str = None
    quantia_estoque_minimo: int = None
    id_usuario: int = None
    data_cadastro: date = None
    estoque: int = None
