
from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
from flaskrc.commons.sqlbuilders.QueryBuilder import QueryBuilder
from flaskrc.commons.sqlbuilders.UpdateBuilder import UpdateBuilder
from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm
from flaskrc.models.Produto import Produto


class ProdutoRepository:

    def registrar_produto(self, produto: Produto) -> Produto:
        orm.session.add(produto)
        orm.session.flush()
        return produto

    def consultar_produtos(self, filtro: ProdutoDTO) -> set[Produto]:
        consulta = QueryBuilder(filtro_obrigatorio=False).selecionar(Produto)\
            .filtro_igual(Produto.id_produto, filtro.id_produto)\
            .filtro_igual(Produto.data_cadastro, filtro.data_cadastro)\
            .filtro_igual_enum(Produto.indicador_ativo, filtro.indicador_ativo_enum)\
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

    def atualizar_produto_por_id(self, produto_atualizado: Produto) -> Produto:
        alteracao = UpdateBuilder(Produto, alts_obrigatorias=False)\
            .filtro_igual(Produto.id_produto, produto_atualizado.id_produto)\
            .alterar(
                nome_produto=produto_atualizado.nome_produto,
                descricao_produto=produto_atualizado.descricao_produto,
                indicador_ativo=produto_atualizado.indicador_ativo_enum.value,
                quantia_estoque_minimo=produto_atualizado.quantia_estoque_minimo
            ).construir()

        orm.session.execute(alteracao)
        orm.session.flush()

        return produto_atualizado
