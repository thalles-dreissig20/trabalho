from models.retention import Retention
from models.invoice import Invoice

class RetentionController:
    def __init__(self):
        self.retentions = []
    
    def cadastrar_retencao(self, tipo: str, valor: float, nota_fiscal: Invoice):
        retencao = Retention(tipo, valor, nota_fiscal)
        self.retentions.append(retencao)
        return retencao
    
    def listar_retentions(self):
        return self.retentions
