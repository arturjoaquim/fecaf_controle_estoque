from typing import TYPE_CHECKING

from flask import Blueprint, flash, request
from flask_login import current_user, login_required

from flaskrc.commons.mappers.ProdutoDTOMapper import ProdutoDTOMapper
from flaskrc.controllers.ControllerBase import trata_excecao_api, trata_excecao_form
from flaskrc.repositories.ProdutoRepository import ProdutoRepository
from flaskrc.services.produto.ConsultarProdutoService import ConsultarProdutoService
from flaskrc.services.produto.RegistrarProdutoService import RegistrarProdutoService

if TYPE_CHECKING:
    from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
    from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO

bp = Blueprint("produto", __name__, url_prefix="/produto")
bp_api = Blueprint("api-produto", __name__, url_prefix="/api/produto")

registrar_produto_service = RegistrarProdutoService(ProdutoRepository())
consultar_produto_service = ConsultarProdutoService(ProdutoRepository())

@bp.route("/cadastrar", methods=["GET", "POST"])
@login_required
@trata_excecao_form("hello")
def cadastrar_produto() -> str | None:
    if (request.method == "POST"):
        usuario_logado: UsuarioDTO = current_user
        produto_mapper: ProdutoDTOMapper = ProdutoDTOMapper(
            only=["nome_produto",
                    "descricao_produto",
                    "quantia_estoque_minimo"],
            campos_obrigatorios=["nome_produto",
                                    "descricao_produto",
                                    "quantia_estoque_minimo"]
        )
        produto_dto : ProdutoDTO = produto_mapper.load(request.form)
        novo_produto: ProdutoDTO = registrar_produto_service\
            .registrar_produto(produto_dto, usuario_logado.id_usr)
        print(produto_dto)
        print(novo_produto)
        flash("Sucesso", "error")
    return "hello"

@bp.route("/consultar", methods=["GET","POST"])
@login_required
@trata_excecao_form("Consulta produto")
def consultar_produto() -> str | None:
    if (request.method == "POST"):
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

@bp_api.route("/consultar-abaixo-estoque-minimo", methods=["GET"])
@login_required
@trata_excecao_api
def consultar_produtos_abaixo_estoque_minimo() -> str:
    produtos: list[ProdutoDTO] = consultar_produto_service\
        .consultar_produtos_abaixo_estoque_minimo()
    return ProdutoDTOMapper().dump(produtos, many=True), 200
