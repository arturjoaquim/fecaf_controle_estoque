from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import CHAR, Date, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm

if TYPE_CHECKING:

    from flaskrc.models.Movimentacao import Movimentacao
    from flaskrc.models.UsuarioAcessoDetalhe import UsuarioAcessoDetalhe


class Usuario(orm.Model):
    __tablename__ = "Usuario"

    id_usr: Mapped[int] = mapped_column(Integer, primary_key=True)
    nm_usr: Mapped[str] = mapped_column(Text)
    dt_cad: Mapped[date] = mapped_column(Date)
    ic_atv: Mapped[str] = mapped_column(CHAR(1))

    Produto: Mapped[list["Produto"]] = relationship("Produto", back_populates="Usuario_")
    UsuarioAcessoDetalhe: Mapped[list["UsuarioAcessoDetalhe"]] = relationship("UsuarioAcessoDetalhe", back_populates="Usuario_")
    Movimentacao: Mapped[list["Movimentacao"]] = relationship("Movimentacao", back_populates="Usuario_")
