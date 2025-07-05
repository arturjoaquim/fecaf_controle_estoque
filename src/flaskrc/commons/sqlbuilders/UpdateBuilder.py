from sqlalchemy import Update, update

from flaskrc.commons.sqlbuilders.SqlBuilderAbstract import SqlBuilderAbstract
from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm

Model = orm.Model

class UpdateBuilder(SqlBuilderAbstract):

    def __init__(self, model: Model, *, filtro_obrigatorio:bool=True) -> None:
        super().__init__(filtro_obrigatorio)
        self._model = model
        self._alteracoes = {}

    def alterar(self, **atualizacoes:dict) -> "UpdateBuilder":
        self._alteracoes.update(atualizacoes)
        return self

    def construir(self) -> Update[Model]:
        return update(self._model).where(*self._filtros).values(**self._alteracoes)
