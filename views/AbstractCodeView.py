from abc import ABC

class AbstractCodeView(ABC):
    def get_code(self, message):
        try:
            return int(input(message))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            return None