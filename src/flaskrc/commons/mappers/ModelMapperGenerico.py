from flask_sqlalchemy.model import Model
from sqlalchemy.orm.properties import ColumnProperty


def converter_para_dicionario(model: Model, *, campos_excluidos: list|None=None) -> dict:  # noqa: E501
    """
    Converte um objeto de modelo em um dicionário.
    """
    if model is None:
        return {}

    if campos_excluidos is None:
        campos_excluidos = []

    return {
            atributo.key: getattr(model, atributo.key)
            for atributo in model.__mapper__.attrs
            if atributo.key not in campos_excluidos
                and isinstance(atributo, ColumnProperty)
        }
