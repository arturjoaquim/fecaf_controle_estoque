from datetime import date

from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.mappers.ModelDictMapper import ModelDictMapper
from flaskrc.models.Produto import Produto
from flaskrc.repositories.ProdutoRepository import ProdutoRepository


class RegistrarProdutoService:

    def registrar_produto(self, produto_dto: ProdutoDTO, id_usuario: int) -> ProdutoDTO:
        """
            Registra um novo produto no sistema.
        """
        produto_repository: ProdutoRepository = ProdutoRepository()
        model_dict_mapper: ModelDictMapper = ModelDictMapper()
        produto: Produto = Produto(**produto_dto.__dict__)

        produto.indicador_ativo = "A"
        produto.id_usuario = id_usuario
        produto.data_cadastro = date.today()
        produto_repository.registrar_produto(produto)

        return ProdutoDTO(**model_dict_mapper.converter_para_dicionario(produto))
