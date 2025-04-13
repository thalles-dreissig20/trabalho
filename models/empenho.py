class Empenho:
    def __init__(self, codigo: str, saldo: float):
        self.codigo = codigo
        self.saldo = saldo

    def abater_valor(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            raise ValueError("Valor a abater maior que o saldo disponível.")

    def __str__(self):
        return f"Empenho {self.codigo} - Saldo: R$ {self.saldo:.2f}"