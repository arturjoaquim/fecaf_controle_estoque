import os
import sqlite3
from datetime import datetime

import click
from flask import current_app, g


def receber_conexao() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], # type: ignore
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def fechar_conexao(e=None) -> None:
    conexao = None

    if "db" in g:
        conexao: sqlite3.Connection | None = g.pop("db")

    if conexao is not None:
        conexao.close()

def iniciar_db() -> None:
    conexao = receber_conexao()

    with open(os.path.join(current_app.root_path, "config", "schema.sql")) as script_iniciar_banco:  # noqa: E501
        statement = script_iniciar_banco.read()
        conexao.executescript(statement)


@click.command("init-db")
def iniciar_db_cli() -> None:
    iniciar_db()
    click.echo("Banco de dados e tabelas inciais criadas.")

sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)
