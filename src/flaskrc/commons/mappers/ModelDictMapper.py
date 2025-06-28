from flask_sqlalchemy.model import Model


class ModelDictMapper:
    """
    Mapper para converter objetos de modelo em dicionários.
    """

    @staticmethod
    def converter_para_dicionario(model: Model) -> dict:
        """
        Converte um objeto de modelo em um dicionário genérico.
        """
        if model is None:
            return {}
        return {coluna.name: getattr(model, coluna.name) for coluna in model.__table__.columns}
