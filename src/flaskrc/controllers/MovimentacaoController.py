from typing import TYPE_CHECKING

from flask import Blueprint, request
from flask_login import current_user, login_required

from flaskrc.commons.mappers.MovimentoDTOMapper import MovimentoDTOMapper
from flaskrc.controllers.ControllerBase import trata_excecao_form
from flaskrc.repositories.MovimentacaoRepository import MovimentacaoRepository
from flaskrc.repositories.ProdutoRepository import ProdutoRepository
from flaskrc.repositories.TipoMovimentacaoRepository import TipoMovimentacaoRepository
from flaskrc.services.movimentacao.ConsultarMovimentacaoService import (
    ConsultarMovimentacaoService,
)
from flaskrc.services.movimentacao.RegistrarMovimentacaoService import (
    RegistrarMovimentacaoService,
)

if TYPE_CHECKING:
    from flaskrc.commons.dtos.MovimentoDTO import MovimentoDTO
    from flaskrc.commons.dtos.UsuarioDTO import UsuarioDTO

bp = Blueprint("movimentacao", __name__, url_prefix="/movimentacao")
bp_api = Blueprint("api-movimentacao", __name__, url_prefix="/api/movimentacao")

@bp.route("/registrar", methods=["GET","POST"])
@login_required
@trata_excecao_form("cadastro movimento")
def registrar_movimento() -> str|None:
    if request.method == "POST":
        dados_necessarios = [
            "id_produto",
            "quantia_movimentada",
            "data_movimentacao",
            "id_tipo_movimento"
        ]

        movimento_mapper = MovimentoDTOMapper(
            campos_obrigatorios=dados_necessarios,
            only=dados_necessarios
        )

        registrar_movimento_service = RegistrarMovimentacaoService(
            MovimentacaoRepository(),
            TipoMovimentacaoRepository(),
            ProdutoRepository()
        )
        usuario_logado: UsuarioDTO = current_user

        movimento_dto: MovimentoDTO = movimento_mapper.load(request.form)
        novo_movimento = registrar_movimento_service.registrar_movimento(
            movimento_dto, usuario_logado.id_usr
        )
        print(novo_movimento)
    return "cadastro movimento"

@bp.route("/consultar", methods=["GET","POST"])
@login_required
@trata_excecao_form("consulta movimento")
def consultar_movimento() -> str|None:
    if request.method == "POST":
        movimento_mapper = MovimentoDTOMapper(
            only=[
                "id_produto",
                "quantia_movimentada",
                "data_movimentacao",
                "id_tipo_movimento",
                "id_usuario",
                "data_cadastro"
            ]
        )
        consultar_movimento_service = ConsultarMovimentacaoService()

        filtro: MovimentoDTO = movimento_mapper.load(request.form)
        lista_movimentos: list[MovimentoDTO] = consultar_movimento_service\
            .consultar_movimentacoes(filtro)
        print(lista_movimentos)
    return "consulta movimento"
