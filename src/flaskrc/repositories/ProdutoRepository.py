from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm
from flaskrc.models.Produto import Produto


class ProdutoRepository:

    def registrar_produto(self, produto: Produto) -> Produto:
        orm.session.add(produto)
        return produto
