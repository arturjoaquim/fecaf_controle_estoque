from datetime import date

from sqlalchemy import Select, func, select

from flaskrc.commons.dtos.MovimentoDTO import MovimentoDTO
from flaskrc.commons.sqlbuilders.QueryBuilder import QueryBuilder
from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm
from flaskrc.models.Movimentacao import Movimentacao


class MovimentacaoRepository:

    def registrar_movimento(self, movimento: Movimentacao) -> Movimentacao:
        orm.session.add(movimento)
        orm.session.flush()
        return movimento

    def consultar_movimentacoes(self, filtro: MovimentoDTO) -> list[Movimentacao]:
        consulta = QueryBuilder(filtro_obrigatorio=False).selecionar(Movimentacao)\
            .filtro_igual(Movimentacao.id_movimentacao, filtro.id_movimentacao)\
            .filtro_igual(Movimentacao.data_cadastro, filtro.data_cadastro)\
            .filtro_igual(Movimentacao.id_produto, filtro.id_produto)\
            .filtro_igual(Movimentacao.id_usuario, filtro.id_usuario)\
            .filtro_igual(Movimentacao.id_tipo_movimento, filtro.id_tipo_movimento)\
            .filtro_igual(Movimentacao.quantia_movimentada, filtro.quantia_movimentada)\
            .filtro_igual(Movimentacao.data_movimentacao, filtro.data_movimentacao)\
            .construir()
        return orm.session.execute(consulta).scalars().all()
