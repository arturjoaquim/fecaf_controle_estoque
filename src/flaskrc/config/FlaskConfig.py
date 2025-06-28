import os  # noqa: N999

from flask import Flask

from flaskrc.config import DatabaseConfig
from flaskrc.config.SQLAlchemyConfig import sql_alchemy
from flaskrc.controllers.AutenticacaoController import bp as bp_autenticacao
from flaskrc.controllers.AutenticacaoController import bp_api as bp_autenticacao_api
from flaskrc.controllers.ProdutoController import bp as bp_produto
from flaskrc.controllers.ProdutoController import bp_api as bp_produto_api
from flaskrc.models import *  # noqa: F403


def adicionar_cli_iniciar_banco(app: Flask) -> None:
    app.teardown_appcontext(DatabaseConfig.fechar_conexao)
    app.cli.add_command(DatabaseConfig.iniciar_db_cli)

def configurar_app(app) -> None:
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE= os.path.join(app.root_path, "stock_control.sqlite"),
        SESSION_COOKIE_SAMESITE= "Strict", # Para evitar CRFS, pois não estou usando Flask WTF
        SESSION_COOKIE_SECURE = True,
        SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(app.root_path, "stock_control.sqlite")  # noqa: E501
    )
    adicionar_cli_iniciar_banco(app)
    app.register_blueprint(bp_produto)
    app.register_blueprint(bp_produto_api)
    app.register_blueprint(bp_autenticacao)
    app.register_blueprint(bp_autenticacao_api)
    sql_alchemy.init_app(app)
