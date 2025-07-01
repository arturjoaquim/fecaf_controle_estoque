from datetime import date

from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.mappers.ModelMapperGenerico import converter_para_dicionario
from flaskrc.models.Produto import Produto
from flaskrc.repositories.ProdutoRepository import ProdutoRepository


class RegistrarProdutoService:

    def __init__(self, produto_repository: ProdutoRepository) -> None:
        self.produto_repository: ProdutoRepository = produto_repository
        self.produto: Produto = None

    def registrar_produto(self, produto_dto: ProdutoDTO, id_usuario: int) -> ProdutoDTO:
        """
            Registra um novo produto no sistema.
        """
        self.produto: Produto = Produto(**produto_dto.__dict__)

        self.produto.indicador_ativo = "A"
        self.produto.id_usuario = id_usuario
        self.produto.data_cadastro = date.today()
        self.produto = self.produto_repository.registrar_produto(self.produto)

        return ProdutoDTO(**converter_para_dicionario(self.produto))
