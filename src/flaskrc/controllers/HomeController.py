from typing import TYPE_CHECKING

from flask import Blueprint, render_template
from flask_login import login_required

from flaskrc.commons.mappers.ProdutoDTOMapper import ProdutoDTOMapper
from flaskrc.commons.mappers.ProdutoMapper import ProdutoMapper
from flaskrc.controllers.ControllerBase import trata_excecao_form
from flaskrc.repositories.ProdutoRepository import ProdutoRepository
from flaskrc.services.produto.ConsultarProdutoService import ConsultarProdutoService

if TYPE_CHECKING:
    from flaskrc.commons.dtos.ProdutoDTO import ProdutoDTO

bp = Blueprint("home", __name__, url_prefix="/")
consultar_produto_service = ConsultarProdutoService(ProdutoRepository(), ProdutoMapper())


@bp.route("/", methods=["GET"])
@login_required
@trata_excecao_form("home.home")
def home() -> str:
    """
        Rota para página inicial.
    """
    produto_dto_mapper:ProdutoDTOMapper = ProdutoDTOMapper(many=True)
    produtos: list[ProdutoDTO] = consultar_produto_service\
        .consultar_produtos_abaixo_estoque_minimo()
    return render_template("index.html", produtos=produto_dto_mapper.dump(produtos))
