import os  # noqa: N999

from flask import Flask

from flaskrc.config import DatabaseConfig
from flaskrc.config.FlaskLoginConfig import login_manager
from flaskrc.config.SQLAlchemyConfig import finalizar_transacao, sql_alchemy
from flaskrc.controllers.HomeController import bp as bp_home
from flaskrc.controllers.MovimentacaoController import bp as bp_movimentacao
from flaskrc.controllers.MovimentacaoController import bp_api as bp_movimentacao_api
from flaskrc.controllers.ProdutoController import bp as bp_produto
from flaskrc.controllers.ProdutoController import bp_api as bp_produto_api
from flaskrc.controllers.UsuarioController import bp as bp_usuario
from flaskrc.controllers.UsuarioController import bp_api as bp_usuario_api
from flaskrc.models import *  # noqa: F403


def adicionar_cli_iniciar_banco(app: Flask) -> None:
    # app.teardown_appcontext(DatabaseConfig.fechar_conexao)
    app.cli.add_command(DatabaseConfig.iniciar_db_cli)

def adicionar_controle_transacional_por_sessao(app: Flask) -> None:
    app.teardown_appcontext(finalizar_transacao)

def configurar_app(app: Flask) -> None:
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
    app.register_blueprint(bp_usuario)
    app.register_blueprint(bp_usuario_api)
    app.register_blueprint(bp_movimentacao)
    app.register_blueprint(bp_movimentacao_api)
    app.register_blueprint(bp_home)
    sql_alchemy.init_app(app)
    login_manager.init_app(app)
    adicionar_controle_transacional_por_sessao(app)
