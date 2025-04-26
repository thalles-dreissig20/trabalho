from models.company import Company

class Invoice:
    def __init__(self, codigo: str, tipo: str, data: str, valor_total: float, empresa: Company):
        self.codigo = codigo
        self.tipo = tipo  # "NF" ou "Fatura"
        self.data = data
        self.valor_total = valor_total
        self.empresa = empresa  # agregação reversa
        self.aprovada = False
        self.homologada = False

    def aprovar(self):
        self.aprovada = True

    def homologar(self):
        self.homologada = True

    def __str__(self):
        return (
            f"╔══════════════════════════════════════════╗\n"
            f"║ Código:         {self.codigo}\n"
            f"║ Tipo:           {self.tipo}\n"
            f"║ Data:           {self.data}\n"
            f"║ Valor Total:    R$ {self.valor_total:.2f}\n"
            f"║ Aprovada:       {self.aprovada}\n"
            f"║ Homologada:     {self.homologada}\n"
            f"╚══════════════════════════════════════════╝ \n" 
            f"{self.empresa}\n"
        )