from typing import TYPE_CHECKING

from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.mappers.ProdutoMapper import ProdutoMapper
from flaskrc.repositories.ProdutoRepository import ProdutoRepository

if TYPE_CHECKING:
    from flaskrc.models.Produto import Produto


class ConsultarProdutoService:

    def __init__(
            self,
            produto_repository: ProdutoRepository,
            produto_mapper: ProdutoMapper
        ) -> None:
        self.produto_repository: ProdutoRepository = produto_repository
        self.produto_mapper: ProdutoMapper = produto_mapper

    def consultar_produtos(self, filtro: ProdutoDTO) -> list[ProdutoDTO] | None:
        produtos: list[Produto] = self.produto_repository.consultar_produtos(filtro)

        return [self.produto_mapper.converter_para_produto_dto(produto) for produto in produtos]  # noqa: E501

    def consultar_produtos_abaixo_estoque_minimo(self) -> list[ProdutoDTO]:
        produtos: list[Produto] = self.produto_repository\
            .consultar_produtos_abaixo_estoque_minimo()
        return [self.produto_mapper.converter_para_produto_dto(produto) for produto in produtos]  # noqa: E501

    def consultar_id_produto_por_nome(self, nome_produto: str) -> list[ProdutoDTO]:
        if (not nome_produto):
            msg = "Nome produto não pode ser vazio."
            raise ValueError(msg)

        filtro = ProdutoDTO(nome_produto=nome_produto)
        produtos: list[Produto] = self.produto_repository.consultar_produtos(filtro)
        return [ProdutoDTO(produto.id_produto, produto.nome_produto) for produto in produtos]  # noqa: E501

