from typing import TYPE_CHECKING

from flask import Blueprint, request
from flask_login import login_required

from flaskrc.commons.mappers.TipoMovimentacaoMapper import TipoMovimentacaoMapper
from flaskrc.commons.mappers.TipoMovimentoDTOMapper import TipoMovimentoDTOMapper
from flaskrc.controllers.ControllerBase import trata_excecao_api
from flaskrc.repositories.TipoMovimentacaoRepository import TipoMovimentacaoRepository
from flaskrc.services.tipomovimentacao.ConsultarTipoMovimentacaoService import (
    ConsultarTipoMovimentacaoService,
)

if TYPE_CHECKING:
    from flaskrc.commons.dtos.TipoMovimentacaoDTO import TipoMovimentacaoDTO

bp_api = Blueprint("api-tipo-movimentacao", __name__, url_prefix="/api/tipo-movimentacao")
consultar_tp_mov_service = ConsultarTipoMovimentacaoService(
    TipoMovimentacaoRepository(),
    TipoMovimentacaoMapper()
)


@bp_api.route("/consultar-id-por-nome", methods=["GET"])
@login_required
@trata_excecao_api
def consultar_id_por_nome() -> str:
    nome_tipo_movimentacao: str = request.args.get("nomeTipoMov", "")
    tipos_movimentacao: list[TipoMovimentacaoDTO] = consultar_tp_mov_service\
        .consultar_id_tipo_movimentacao_por_nome(nome_tipo_movimentacao)
    return TipoMovimentoDTOMapper(
            many=True,
            only=["id_tipo_mov", "nome_tipo_mov"]
        ).dump(tipos_movimentacao)
