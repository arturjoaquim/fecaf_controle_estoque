from datetime import date

from sqlalchemy import Select, select

from flaskrc.models.Produto import Produto


class ProdutoQueryBuilder:

    consulta_sql: Select

    def __init__(self) -> None:
        self.consulta_sql = select(Produto)

    def com_nome(self, nome: str) -> None:
        if nome is not None:
            self.consulta_sql = self.consulta_sql.where(Produto.nome_produto.like(f"%{nome}%"))  # noqa: E501

    def com_data_cadastro(self, data: date) -> None:
        if data is not None:
            self.consulta_sql = self.consulta_sql.where(Produto.data_cadastro == data)

    def com_indicador_ativo(self, indicador: str) -> None:
        if indicador is not None:
            self.consulta_sql = self.consulta_sql.where(Produto.indicador_ativo == indicador)  # noqa: E501

    def com_descricao(self, descricao:str) -> None:
        if descricao is not None:
            self.consulta_sql = self.consulta_sql.where(Produto.descricao_produto.like(f"%{descricao}%"))  # noqa: E501

    def com_estoque_minimo(self, estoque_minimo: int) -> None:
        if estoque_minimo is not None:
            self.consulta_sql = self.consulta_sql.where(Produto.quantia_estoque_minimo == estoque_minimo)  # noqa: E501

    def com_id_usuario(self, id_usr: int) -> None:
        if id_usr is not None:
            self.consulta_sql = self.consulta_sql.where(Produto.id_usuario == id_usr)

    def com_id_produto(self, id_produto: int) -> None:
        if id_produto is not None:
            self.consulta_sql = self.consulta_sql.where(Produto.id_produto == id_produto)  # noqa: E501

    def construir_consulta(self) -> Select:
        return self.consulta_sql

    def reiniciar_builder(self) -> None:
        self.consulta_sql = select(Produto)
