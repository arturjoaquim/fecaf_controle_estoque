from typing import TYPE_CHECKING

from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.sqlbuilders.QueryBuilder import QueryBuilder
from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm
from flaskrc.models.Produto import Produto

if TYPE_CHECKING:
    from sqlalchemy import Select


class ProdutoRepository:

    def registrar_produto(self, produto: Produto) -> Produto:
        orm.session.add(produto)
        orm.session.flush()
        return produto

    def consultar_produtos(self, filtro: ProdutoDTO) -> set[Produto]:
        consulta = QueryBuilder(filtro_obrigatorio=False).selecionar(Produto)\
            .filtro_igual(Produto.id_produto, filtro.id_produto)\
            .filtro_igual(Produto.data_cadastro, filtro.data_cadastro)\
            .filtro_igual(Produto.quantia_estoque_minimo, filtro.quantia_estoque_minimo)\
            .filtro_ilike(Produto.nome_produto, filtro.nome_produto)\
            .construir()

        return orm.session.execute(consulta).scalars().all()

    def consultar_produto_por_id(self, id_produto: int) -> Produto | None:
        consulta = QueryBuilder().selecionar(Produto)\
            .filtro_igual(Produto.id_produto, id_produto)\
            .construir()
        return orm.session.execute(consulta).scalar_one_or_none()

    def consultar_produtos_abaixo_estoque_minimo(self) -> list[Produto]:
        consulta = (
            QueryBuilder().selecionar(Produto)
            .filtro_menor_que(Produto.quantia_estoque, Produto.quantia_estoque_minimo)
            .construir()
        )

        return orm.session.execute(consulta).scalars().all()
