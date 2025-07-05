from sqlalchemy import Select, select

from flaskrc.commons.sqlbuilders.SqlBuilderAbstract import SqlBuilderAbstract


class QueryBuilder(SqlBuilderAbstract):

    def __init__(self, *, filtro_obrigatorio:bool=True) -> None:
        super().__init__(filtros_obrigatorios=filtro_obrigatorio)
        self._selecao = []
        self._relacionamentos = []

    def selecionar(self, *selecoes: tuple) -> "QueryBuilder":
        self._selecao.extend(selecoes)
        return self

    def relacionar(self, *relacionamentos: tuple) -> "QueryBuilder":
        self._relacionamentos.extend(relacionamentos)
        return self

    def construir(self) -> Select:
        consulta = select(*self._selecao)

        if self._relacionamentos:
            consulta = consulta.join(*self._relacionamentos)

        return consulta.where(*self._filtros)
