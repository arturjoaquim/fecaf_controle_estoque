from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.mappers.ModelMapperGenerico import converter_dto_para_model
from flaskrc.commons.mappers.ProdutoMapper import ProdutoMapper
from flaskrc.models.Produto import Produto
from flaskrc.repositories.ProdutoRepository import ProdutoRepository


class EditarProdutoService:

    def __init__(self, produto_repository: ProdutoRepository, produto_mapper: ProdutoMapper) -> None:
        self.produto_repository = produto_repository
        self.produto_mapper: ProdutoMapper = produto_mapper

    def editar_produto(self, produto_alterado: ProdutoDTO) -> ProdutoDTO:
        produto: Produto = converter_dto_para_model(produto_alterado, Produto)
        produto_atualizado = self.produto_repository.atualizar_produto_por_id(produto)
        return self.produto_mapper.converter_para_produto_dto(produto_atualizado)
