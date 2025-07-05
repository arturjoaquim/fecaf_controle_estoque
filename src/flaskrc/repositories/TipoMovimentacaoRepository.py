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

    def consultar_id_tipo_movimentacao_por_nome(
            self,
            nome_tipo_movimentacao: str
        ) -> list[TipoMovimentacao]:
        consulta = select(TipoMovimentacao)\
            .where(TipoMovimentacao.nome_tipo_mov.like(f"%{nome_tipo_movimentacao}%"))
        return orm.session.execute(consulta).scalars().all()
