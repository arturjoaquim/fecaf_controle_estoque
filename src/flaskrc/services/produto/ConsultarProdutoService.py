from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.mappers.ModelMapperGenerico import (
    converter_dto_para_model,
    converter_para_dicionario,
)
from flaskrc.models.Produto import Produto
from flaskrc.repositories.ProdutoRepository import ProdutoRepository


class ConsultarProdutoService:

    def consultar_produtos(self, filtro: ProdutoDTO) -> list[ProdutoDTO] | None:
        produto_repository = ProdutoRepository()

        produtos: list[Produto] = produto_repository.consultar_produtos(filtro)

        return [ProdutoDTO(**converter_para_dicionario(produto)) for produto in produtos]
