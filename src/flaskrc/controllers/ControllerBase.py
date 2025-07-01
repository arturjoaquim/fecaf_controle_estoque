import functools
import traceback
from collections.abc import Callable

from flask import flash

from flaskrc.config.SQLAlchemyConfig import sql_alchemy as orm


def trata_excecao_form(pagina: str) -> Callable:
    """
    Decorador para tratar exceções em rotas que recebem dados de formulário.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> object:
            try:
                return func(*args, **kwargs)
            except Exception as error:  # noqa: BLE001
                flash(error.__str__(), "error")
                print(traceback.print_exc())
                orm.session.rollback() # Reverte a transação no contexto de uma requisição HTTP  # noqa: E501
                return pagina
        return wrapper
    return decorator

def trata_excecao_api(func: Callable) -> Callable:
    """
    Decorador para tratar exceções em rotas de API.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> object:
        try:
            return func(*args, **kwargs)
        except Exception as error: # noqa: BLE001
            print(traceback.print_exc())
            orm.session.rollback()
            return {"error": error.__str__()}, 500
    return wrapper
