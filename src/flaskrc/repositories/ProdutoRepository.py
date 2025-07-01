from typing import TYPE_CHECKING

from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.querybuilders.ProdutoQueryBuilder import ProdutoQueryBuilder
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
        query_builder = ProdutoQueryBuilder(filtro_obrigatorio=False).selecionar_tudo()\
            .filtro_nome(filtro.nome_produto)\
            .filtro_data_cadastro(filtro.data_cadastro)\
            .filtro_indicador_ativo(filtro.indicador_ativo)\
            .filtro_estoque_minimo(filtro.quantia_estoque_minimo)\
            .filtro_id_usuario(filtro.id_usuario)
        comando_sql: Select = query_builder.construir_consulta()

        return orm.session.execute(comando_sql).scalars().all()

    def consultar_produto_por_id(self, id_produto: int) -> Produto | None:
        consulta = ProdutoQueryBuilder().selecionar_tudo()\
            .filtro_id(id_produto).construir_consulta()
        return orm.session.execute(consulta).scalar_one_or_none()

