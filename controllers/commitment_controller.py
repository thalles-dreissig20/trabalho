from models.commitment import Commitment
from models.invoice import Invoice

class CommitmentController:
    def __init__(self):
        self.empenhos = []
    
    def cadastrar_empenho(self, numero: str, valor: float, descricao: str, nota_fiscal: Invoice):
        empenho = Commitment(numero, valor, descricao, nota_fiscal)
        self.empenhos.append(empenho)
        return empenho
    
    def listar_empenhos(self):
        return self.empenhos
