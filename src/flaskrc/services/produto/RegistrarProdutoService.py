from datetime import date

from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.enums.IndicadorAtivoEnum import IndicadorAtivoEnum
from flaskrc.commons.mappers.ProdutoMapper import ProdutoMapper
from flaskrc.models.Produto import Produto
from flaskrc.repositories.ProdutoRepository import ProdutoRepository


class RegistrarProdutoService:

    def __init__(
            self,
            produto_repository: ProdutoRepository,
            produto_mapper: ProdutoMapper
        ) -> None:
        self.produto_repository: ProdutoRepository = produto_repository
        self.produto_mapper: ProdutoMapper = produto_mapper
        self.produto: Produto = None

    def registrar_produto(self, produto_dto: ProdutoDTO, id_usuario: int) -> ProdutoDTO:
        """
            Registra um novo produto no sistema.
        """
        produto_dto.indicador_ativo_enum = IndicadorAtivoEnum.ATIVO
        produto_dto.id_usuario = id_usuario
        produto_dto.data_cadastro = date.today()
        self.produto: Produto = Produto(**produto_dto.__dict__)
        self.produto = self.produto_repository.registrar_produto(self.produto)

        return self.produto_mapper.converter_para_produto_dto(self.produto)
