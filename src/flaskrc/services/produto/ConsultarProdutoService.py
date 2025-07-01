from typing import TYPE_CHECKING

from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.mappers.ModelMapperGenerico import (
    converter_para_dicionario,
)
from flaskrc.repositories.ProdutoRepository import ProdutoRepository

if TYPE_CHECKING:
    from flaskrc.models.Produto import Produto


class ConsultarProdutoService:

    def __init__(self, produto_repository: ProdutoRepository) -> None:
        self.produto_repository: ProdutoRepository = produto_repository

    def consultar_produtos(self, filtro: ProdutoDTO) -> list[ProdutoDTO] | None:
        produtos: list[Produto] = self.produto_repository.consultar_produtos(filtro)

        return [ProdutoDTO(**converter_para_dicionario(produto)) for produto in produtos]

    def consultar_produtos_abaixo_estoque_minimo(self) -> list[ProdutoDTO]:
        produtos: list[Produto] = self.produto_repository\
            .consultar_produtos_abaixo_estoque_minimo()
        return [ProdutoDTO(**converter_para_dicionario(produto)) for produto in produtos]
