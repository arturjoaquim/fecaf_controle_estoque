from flaskrc.models.GrupoAcesso import GrupoAcesso
from flaskrc.models.Movimentacao import Movimentacao
from flaskrc.models.Produto import Produto
from flaskrc.models.TipoMovimentacao import TipoMovimentacao
from flaskrc.models.Usuario import Usuario
from flaskrc.models.UsuarioAcessoDetalhe import UsuarioAcessoDetalhe

# Para permitir importação de todos os modelos de uma vez e evitar falta de importações para o SQLAlchemy  # noqa: E501
__all__ = [
    "GrupoAcesso",
    "Movimentacao",
    "Produto",
    "TipoMovimentacao",
    "Usuario",
    "UsuarioAcessoDetalhe",
]
