from typing import TYPE_CHECKING

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from flaskrc.services.produto.EditarProdutoService import EditarProdutoService
from flaskrc.commons.mappers.ProdutoDTOMapper import ProdutoDTOMapper
from flaskrc.commons.mappers.ProdutoMapper import ProdutoMapper
from flaskrc.controllers.ControllerBase import trata_excecao_api, trata_excecao_form
from flaskrc.repositories.ProdutoRepository import ProdutoRepository
from flaskrc.services.produto.ConsultarProdutoService import ConsultarProdutoService
from flaskrc.services.produto.RegistrarProdutoService import RegistrarProdutoService

if TYPE_CHECKING:
    from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO
    from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO

bp = Blueprint("produto", __name__, url_prefix="/produto")
bp_api = Blueprint("api-produto", __name__, url_prefix="/api/produto")

registrar_produto_service = RegistrarProdutoService(ProdutoRepository(), ProdutoMapper())
consultar_produto_service = ConsultarProdutoService(ProdutoRepository(), ProdutoMapper())
atualizar_produto_service = EditarProdutoService(ProdutoRepository(), ProdutoMapper())

@bp.route("/cadastrar", methods=["GET", "POST"])
@login_required
@trata_excecao_form("produto.cadastrar_produto")
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
        flash(
            f"Produto n°'{novo_produto.id_produto}' cadastrado com sucesso.",
            category="success"
        )
    return render_template("cadastrar-produto.html")

@bp.route("/consultar", methods=["GET","POST"])
@login_required
@trata_excecao_form("produto.consultar_produto")
def consultar_produto() -> str | None:
    if (request.method == "POST"):
        produto_mapper: ProdutoDTOMapper = ProdutoDTOMapper(
            only=["id_produto",
                    "quantia_estoque_minimo",
                    "indicador_ativo_enum",
                    "id_usuario",
                    "data_cadastro"]
        )
        print(request.form)
        produto_dto : ProdutoDTO = produto_mapper.load(request.form)
        produtos: list[ProdutoDTO] = consultar_produto_service.consultar_produtos(produto_dto)  # noqa: E501
        print(produto_dto)
        print("----------")
        print(produtos)
        return render_template(
            "consultar-produto.html", 
            produtos=ProdutoDTOMapper(many=True).dump(produtos)
        )
    return render_template("consultar-produto.html", produtos=None)

@bp_api.route("/consultar-abaixo-estoque-minimo", methods=["GET"])
@login_required
@trata_excecao_api
def consultar_produtos_abaixo_estoque_minimo() -> dict:
    produtos: list[ProdutoDTO] = consultar_produto_service\
        .consultar_produtos_abaixo_estoque_minimo()
    return ProdutoDTOMapper(many=True).dump(produtos), 200

@bp_api.route("/consultar-id-por-nome", methods=["GET"])
@login_required
@trata_excecao_api
def consultar_id_produto_por_nome() -> dict:
    nome_produto: str = request.args.get("nomeProduto", "")
    print(nome_produto)
    produtos: list[ProdutoDTO] = consultar_produto_service\
        .consultar_id_produto_por_nome(nome_produto)
    return ProdutoDTOMapper(many=True, only=["id_produto", "nome_produto"]).dump(produtos)


@bp.route("atualizar", methods=["POST"])
@login_required
@trata_excecao_form("produto.consultar_produto")
def atualizar_produto():
    produto_mapper: ProdutoDTOMapper = ProdutoDTOMapper(
        campos_obrigatorios=[
            "id_produto",
            "nome_produto",
            "descricao_produto",
            "indicador_ativo_enum",
            "quantia_estoque_ninimo"
        ]
    )
    produto_dto : ProdutoDTO = produto_mapper.load(request.form)
    produto_atualizado: ProdutoDTO = atualizar_produto_service.editar_produto(produto_dto)
    flash(f"Produto n°{produto_atualizado.id_produto} atualizado com sucesso.", "success")
    return redirect(url_for("produto.consultar_produto"))
