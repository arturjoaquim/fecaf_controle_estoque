from enum import Enum
import functools
from collections.abc import Callable
from typing import TypeVar

# Define um tipo genérico que representa a subclasse concreta
T = TypeVar("T", bound="SqlBuilderAbstract")


def filtro(filtro_func: Callable) -> Callable:
    @functools.wraps(filtro_func)
    def wrapper_filtro(
        self: T,
        coluna: object,
        valor: object,
        *, filtro_obrigatorio: bool=True
    ) -> T:
        self._validar_filtro_obrigatorio(coluna, valor, filtro_obrigatorio)
        if valor is not None:
            return filtro_func(self, coluna, valor)
        return self
    return wrapper_filtro

class SqlBuilderAbstract:

    def __init__(self, *, filtros_obrigatorios:bool=True) -> None:
        self._filtros = []
        self._filtros_obrigatorios = filtros_obrigatorios

    @filtro
    def filtro_igual(self: T, coluna: object, valor: object) -> T:
        self._filtros.append(coluna == valor)
        return self

    @filtro
    def filtro_ilike(self: T, coluna: object, valor: object) -> T:
        self._filtros.append(coluna.ilike(f"%{valor}%"))
        return self

    @filtro
    def filtro_maior_que(self: T, coluna: object, valor: object) -> T:
        self._filtros.append(coluna > valor)
        return self

    @filtro
    def filtro_menor_que(self: T, coluna: object, valor: object) -> T:
        self._filtros.append(coluna < valor)
        return self

    @filtro
    def filtro_igual_enum(self: T, coluna:object, valor: Enum) -> T:
        self._filtros.append(coluna == valor.value)
        return self

    def _validar_filtro_obrigatorio(
            self,
            coluna: object,
            filtro: object,
            fil_obrigatorio_individual: bool  # noqa: FBT001
        ) -> None:
        if (
            self._filtros_obrigatorios
            and filtro is None
            and fil_obrigatorio_individual
        ):
            msg = f"Filtro para {coluna} deve ser preenchido."
            raise ValueError(msg)
