from datetime import date

from sqlalchemy import Select, func, select

from flaskrc.commons.dtos.MovimentoDTO import MovimentoDTO
from flaskrc.commons.querybuilders.MovimentacaoQueryBuilder import (
    MovimentacaoQueryBuilder,
)
from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm
from flaskrc.models.Movimentacao import Movimentacao


class MovimentacaoRepository:

    def registrar_movimento(self, movimento: Movimentacao) -> Movimentacao:
        orm.session.add(movimento)
        orm.session.flush()
        return movimento

    def consultar_movimentacoes(self, filtro: MovimentoDTO) -> list[Movimentacao]:
        query_builder: MovimentacaoQueryBuilder
        query_builder = MovimentacaoQueryBuilder(filtro_obrigatorio=False)\
            .selecionar_tudo()\
            .filtro_data_mov(filtro.data_movimentacao)\
            .filtro_id_produto(filtro.id_produto)\
            .filtro_id_usuario(filtro.id_usuario)\
            .filtro_id_tipo_mov(filtro.id_tipo_movimento)\
            .filtro_quantia_movimentada(filtro.quantia_movimentada)\
            .filtro_data_cadastro(filtro.data_cadastro)
        comando_sql: Select = query_builder.construir_consulta()
        return orm.session.execute(comando_sql).scalars().all()
