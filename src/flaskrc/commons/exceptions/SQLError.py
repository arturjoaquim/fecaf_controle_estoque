class SQLError(Exception):
    """
    Exceção personalizada para indicar que falha na execução de um comando sql.
    """

    def __init__(self, message: str = "Operação falhou por comando sql inválido.") -> None:
        super().__init__(message)
        self.message = message