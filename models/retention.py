class Retention:
    def __init__(self, tipo: str, valor: float, nota_fiscal: 'Invoice'):
        self.tipo = tipo
        self.valor = valor
        self.nota_fiscal = nota_fiscal

    def __str__(self):
        return f"Retenção: {self.tipo} - Valor: R$ {self.valor:.2f} - Nota Fiscal: {self.nota_fiscal.codigo}"
