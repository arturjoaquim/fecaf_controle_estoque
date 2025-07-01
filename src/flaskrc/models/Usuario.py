from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import CHAR, Date, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm
from flaskrc.models.Produto import Produto

if TYPE_CHECKING:

    from flaskrc.models.Movimentacao import Movimentacao
    from flaskrc.models.UsuarioAcessoDetalhe import UsuarioAcessoDetalhe


class Usuario(orm.Model):
    __tablename__ = "Usuario"

    id_usr: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome_usr: Mapped[str] = mapped_column("nm_usr", Text)
    data_cadastro: Mapped[date] = mapped_column("dt_cad", Date)
    indicador_ativo: Mapped[str] = mapped_column("ic_atv", CHAR(1))
    senha_usr: Mapped[str] = mapped_column("psw_usr", Text)

    Produto_: Mapped[list[Produto]] = relationship("Produto", back_populates="Usuario_")
    UsuarioAcessoDetalhe: Mapped[list["UsuarioAcessoDetalhe"]] = relationship("UsuarioAcessoDetalhe", back_populates="Usuario_")
    Movimentacao_: Mapped[list["Movimentacao"]] = relationship("Movimentacao", back_populates="Usuario_")
