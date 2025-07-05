from sqlalchemy import Update, update

from flaskrc.commons.sqlbuilders.SqlBuilderAbstract import SqlBuilderAbstract
from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm

Model = orm.Model

class UpdateBuilder(SqlBuilderAbstract):

    def __init__(
            self,
            model: Model,
            *, filtro_obrigatorio:bool=True,
            alts_obrigatorias: bool=True
        ) -> None:
        super().__init__(filtros_obrigatorios=filtro_obrigatorio)
        self._model: Model = model
        self._alteracoes: dict = {}
        self._alteracoes_obrigatorias: bool = alts_obrigatorias

    def alterar(self, *, alt_obrigatoria:bool=True, **atualizacoes:dict) -> "UpdateBuilder":
        for coluna, novo_valor in atualizacoes.items():
            self._validar_alteracao_obrigatoria(coluna, novo_valor, alt_obrigatoria)
            if novo_valor is not None:
                self._alteracoes.update({coluna: novo_valor})
        return self

    def construir(self) -> Update[Model]:
        return update(self._model).where(*self._filtros).values(**self._alteracoes)

    def _validar_alteracao_obrigatoria(
            self,
            coluna: object,
            novo_valor: object,
            alt_obrigatoria_individual: bool  # noqa: FBT001
        ) -> None:
        if (
            self._alteracoes_obrigatorias
            and novo_valor is None
            and alt_obrigatoria_individual
        ):
            msg = f"Alteração para {coluna} deve ser preenchida."
            raise ValueError(msg)
