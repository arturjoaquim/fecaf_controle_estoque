class RollbackError(Exception):
    """
    Exceção personalizada para indicar que uma transação deve ser revertida.
    Esta exceção é usada para sinalizar que uma operação falhou e a transação
    no contexto de uma requisição HTTP deve ser revertida."""

    def __init__(self, message: str = "Operação falhou e a transação foi revertida.") -> None:
        super().__init__(message)
        self.message = message
