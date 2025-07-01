from enum import Enum


class IndicadorMovimentoEnum(Enum):
    ENTRADA = "E"
    SAIDA = "S"

    @classmethod
    def receber_valor(cls, nome: str) -> str | None:
        return cls[nome].value if nome in cls.__members__ else None

    @classmethod
    def receber_nome(cls, valor: str) -> str | None:
        for tag in cls:
            if tag.value == valor:
                return tag.name
        return None

