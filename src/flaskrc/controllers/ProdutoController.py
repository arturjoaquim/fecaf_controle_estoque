import traceback
from typing import TYPE_CHECKING

from flask import Blueprint, flash, request

from flaskrc.commons.mappers.ProdutoDTOMapper import ProdutoDTOMapper
from flaskrc.models.Produto import Produto
from flaskrc.repositories.ProdutoRepository import ProdutoRepository

if TYPE_CHECKING:
    from flaskrc.commons.dtos import ProdutoDTO

bp = Blueprint("produto", __name__, url_prefix="/produto")
bp_api = Blueprint("api-produto", __name__, url_prefix="/api/produto")

@bp.route("/cadastro", methods=["GET", "POST"])
def cadastrar_produto() -> str | None:
    if (request.method == "POST"):
        try:
            produto_repository = ProdutoRepository() 
            produto_mapper: ProdutoDTOMapper = ProdutoDTOMapper(
                campos_obrigatorios=["nome_produto",
                                     "descricao_produto",
                                     "quantia_estoque_minimo"]
            )
            produto : ProdutoDTO = produto_mapper.load(request.form)
            produto_repository.registrar_produto(Produto(**produto.__dict__))
            print(produto)
        except Exception as error:
            print(traceback.print_exc())
            flash(error.__str__(), "error")
    return "hello"

@bp.route("/consulta", methods=["GET","POST"])
def consultar_produto() -> str | None:
    if (request.method == "POST"):
        pass
    return "Consulta produto"
