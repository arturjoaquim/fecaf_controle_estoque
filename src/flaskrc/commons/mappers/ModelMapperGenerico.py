from flask_sqlalchemy.model import Model
from sqlalchemy.orm.properties import ColumnProperty


def converter_para_dicionario(model: Model, *, campos_ignorados: list|None=None) -> dict:  # noqa: E501
    """
    Converte um objeto de modelo em um dicionário.
    Utiliza set para obter tempos O(1) em verificações.
    """
    if model is None:
        return {}

    campos_ignorados_padrao = {"metadata", "query", "registry", "denominator", "imag", "numerator", "real"}

    if campos_ignorados is None:
        campos_ignorados = campos_ignorados_padrao
    else:
        campos_ignorados = set(campos_ignorados)
        campos_ignorados.update(campos_ignorados_padrao)

    return {
        attr: getattr(model, attr)
        for attr in dir(model)
        if not attr.startswith("_")
            and not callable(getattr(model, attr))
            and attr not in campos_ignorados
    }

def converter_dto_para_model(dto: object, classe_modelo: type[Model]) -> Model:
    """
    Converte um dto em um modelo através dos nomes dos campos,
    funciona inclusive quando dtos tem mais campos que model.
    """
    campos_ignorados = {"metadata", "query", "registry", "denominator", "imag", "numerator", "real"}

    campos_modelo: set = {
        attr: getattr(classe_modelo, attr)
        for attr in dir(classe_modelo)
        if not attr.startswith("_")
            and not callable(getattr(classe_modelo, attr))
            and attr not in campos_ignorados
        }  # noqa: E501
    campos_dto: dict = dto.__dict__

    dados_validos: dict = {
        chave: valor for chave, valor in campos_dto.items()
            if chave in campos_modelo
    }

    return classe_modelo(**dados_validos)