class NegocioError(Exception):
    """
    Exceção personalizada para indicar que houve recusa de uma operação de negócio.
    Essa exceção é lançada quando uma regra de negócio não é satisfeita.
    """

    def __init__(self, message: str = "Operação falhou por recusa de regra de negócio.") -> None:
        super().__init__(message)
        self.message = message
