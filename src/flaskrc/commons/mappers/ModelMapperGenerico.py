from flask_sqlalchemy.model import Model
from sqlalchemy.orm.properties import ColumnProperty


def converter_para_dicionario(model: Model, *, campos_excluidos: set|None=None) -> dict:  # noqa: E501
    """
    Converte um objeto de modelo em um dicionário.
    """
    if model is None:
        return {}

    if campos_excluidos is None:
        campos_excluidos = {}

    return {
            atributo.key: getattr(model, atributo.key)
            for atributo in model.__mapper__.attrs
            if atributo.key not in campos_excluidos
                and isinstance(atributo, ColumnProperty)
        }

def converter_dto_para_model(dto: object, classe_modelo: type[Model]) -> Model:
    """
    Converte um dto em um modelo através dos nomes dos campos,
    funciona inclusive quando dtos tem mais campos que model.
    """
    campos_modelo: set = {atributo.key for atributo in classe_modelo.__mapper__.attrs if isinstance(atributo, ColumnProperty)}  # noqa: E501
    campos_dto: dict = dto.__dict__

    dados_validos: dict = {
        chave: valor for chave, valor in campos_dto.items()
            if chave in campos_modelo
    }

    return classe_modelo(**dados_validos)