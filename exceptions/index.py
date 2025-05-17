
class MenuOptionError(Exception):
    def __init__(self, message="Opção de menu inválida."):
        self.message = message
        super().__init__(self.message)

        
class InvalidInputError(Exception):
    def __init__(self, message="Entrada inválida. Esperado um número."):
        self.message = message
        super().__init__(self.message)