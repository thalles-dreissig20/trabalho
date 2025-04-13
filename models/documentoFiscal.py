class DocumentoFiscal:
    def __init__(self, codigo: str, tipo: str, data: str, valor_total: float, empresa):
        self.codigo = codigo
        self.tipo = tipo  # "NF" ou "Fatura"
        self.data = data
        self.valor_total = valor_total
        self.empresa = empresa  # agregação reversa

    def __str__(self):
        return f"{self.tipo} {self.codigo} - R$ {self.valor_total}"