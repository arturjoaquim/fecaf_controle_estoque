from sqlalchemy import select

from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm
from flaskrc.models.TipoMovimentacao import TipoMovimentacao


class TipoMovimentacaoRepository:

    def consultar_tipo_movimentacao_por_id(
            self, id_tipo_movimentacao: int
        ) -> TipoMovimentacao | None:
        consulta = select(TipoMovimentacao).where(
            TipoMovimentacao.id_tipo_mov == id_tipo_movimentacao
        )
        return orm.session.execute(consulta).scalar_one_or_none()
