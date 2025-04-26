class Commitment:
    def __init__(self, numero: str, valor: float, descricao: str, nota_fiscal: 'Invoice'):
        self.numero = numero
        self.valor = valor
        self.descricao = descricao
        self.nota_fiscal = nota_fiscal

    def __str__(self):
        return (
            f"Empenho Nº: {self.numero}\n"
            f"Valor: R$ {self.valor:.2f}\n"
            f"Descrição: {self.descricao}\n"
            f"Nota Fiscal: {self.nota_fiscal.codigo}"
        )