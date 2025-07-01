from datetime import date

from sqlalchemy import Select, select

from flaskrc.models.Produto import Produto


class ProdutoQueryBuilder:

    _consulta: Select[Produto]
    filtro_obrigatorio: bool

    def __init__(
            self,
            consulta: Select[Produto] = None,
            *, filtro_obrigatorio: bool = True
        ) -> None:
        self._consulta = consulta
        self.filtro_obrigatorio = filtro_obrigatorio

    def selecionar_tudo(self) -> "ProdutoQueryBuilder":
        self._consulta = select(Produto)
        return self

    def filtro_id(self, id_produto: int) -> "ProdutoQueryBuilder":
        self._validar_filtro_obrigatorio(id_produto)
        if id_produto is not None:
            self._consulta = self._consulta.where(Produto.id_produto == id_produto)
        return self

    def filtro_nome(self, nome_produto: str) -> "ProdutoQueryBuilder":
        self._validar_filtro_obrigatorio(nome_produto)
        if nome_produto is not None:
            self._consulta = self._consulta.where(
                Produto.nome_produto.like(f"%{nome_produto}%")
            )
        return self

    def filtro_data_cadastro(self, data_cadastro: date) -> "ProdutoQueryBuilder":
        self._validar_filtro_obrigatorio(data_cadastro)
        if data_cadastro is not None:
            self._consulta = self._consulta.where(
                Produto.data_cadastro == data_cadastro
            )
        return self

    def filtro_indicador_ativo(self, indicador_ativo: str) -> "ProdutoQueryBuilder":
        self._validar_filtro_obrigatorio(indicador_ativo)
        if indicador_ativo is not None:
            self._consulta = self._consulta.where(
                Produto.indicador_ativo == indicador_ativo
            )
        return self

    def filtro_descricao(self, descricao_produto: str) -> "ProdutoQueryBuilder":
        self._validar_filtro_obrigatorio(descricao_produto)
        if descricao_produto is not None:
            self._consulta = self._consulta.where(
                Produto.descricao_produto.like(f"%{descricao_produto}%")
            )
        return self

    def filtro_estoque_minimo(self, estoque_minimo: int) -> "ProdutoQueryBuilder":
        self._validar_filtro_obrigatorio(estoque_minimo)
        if estoque_minimo is not None:
            self._consulta = self._consulta.where(
                Produto.quantia_estoque_minimo == estoque_minimo
            )
        return self

    def filtro_id_usuario(self, id_usuario: int) -> "ProdutoQueryBuilder":
        self._validar_filtro_obrigatorio(id_usuario)
        if id_usuario is not None:
            self._consulta = self._consulta.where(Produto.id_usuario == id_usuario)
        return self

    def construir_consulta(self) -> Select:
        consulta_final: Select = self._consulta
        self.reiniciar_builder()
        return consulta_final

    def reiniciar_builder(self) -> "ProdutoQueryBuilder":
        self._consulta = None
        return self

    def _validar_filtro_obrigatorio(self, filtro: object) -> None:
        if self.filtro_obrigatorio and filtro is None:
            msg = "Filtro obrigatório não fornecido."
            raise ValueError(msg)
