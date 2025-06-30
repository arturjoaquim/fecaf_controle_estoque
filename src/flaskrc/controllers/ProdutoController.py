from typing import TYPE_CHECKING

from flask import Blueprint, flash, request
from flask_login import current_user, login_required

from flaskrc.commons.mappers.ProdutoDTOMapper import ProdutoDTOMapper
from flaskrc.controllers.ControllerBase import trata_excecao_form
from flaskrc.services.Produto.ConsultarProdutoService import ConsultarProdutoService
from flaskrc.services.Produto.RegistrarProdutoService import RegistrarProdutoService

if TYPE_CHECKING:
    from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
    from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO

bp = Blueprint("produto", __name__, url_prefix="/produto")
bp_api = Blueprint("api-produto", __name__, url_prefix="/api/produto")

@bp.route("/cadastro", methods=["GET", "POST"])
@login_required
@trata_excecao_form("hello")
def cadastrar_produto() -> str | None:
    if (request.method == "POST"):
        usuario_logado: UsuarioDTO = current_user
        registrar_service = RegistrarProdutoService()
        produto_mapper: ProdutoDTOMapper = ProdutoDTOMapper(
            only=["nome_produto",
                    "descricao_produto",
                    "quantia_estoque_minimo"],
            campos_obrigatorios=["nome_produto",
                                    "descricao_produto",
                                    "quantia_estoque_minimo"]
        )
        produto_dto : ProdutoDTO = produto_mapper.load(request.form)
        novo_produto: ProdutoDTO = registrar_service.registrar_produto(produto_dto, usuario_logado.id_usr)  # noqa: E501
        print(produto_dto)
        print(novo_produto)
        flash("Sucesso", "error")
    return "hello"

@bp.route("/consulta", methods=["GET","POST"])
@login_required
@trata_excecao_form("Consulta produto")
def consultar_produto() -> str | None:
    if (request.method == "POST"):
        consultar_produto_service = ConsultarProdutoService()
        produto_mapper: ProdutoDTOMapper = ProdutoDTOMapper(
            only=["nome_produto",
                    "quantia_estoque_minimo",
                    "indicador_ativo",
                    "id_usuario",
                    "data_cadastro"]
        )
        produto_dto : ProdutoDTO = produto_mapper.load(request.form)
        produtos: list[ProdutoDTO] = consultar_produto_service.consultar_produtos(produto_dto)  # noqa: E501
        print(produto_dto)
        print("----------")
        print(produtos)
    return "Consulta produto"
