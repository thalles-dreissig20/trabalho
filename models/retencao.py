class Retencao:
    def __init__(self, codigo: str, porcentagem: float):
        self.codigo = codigo
        self.porcentagem = porcentagem
        self.valor = 0.0

    def calcular(self, base: float):
        self.valor = round(base * (self.porcentagem / 100), 2)

    def __str__(self):
        return f"Retenção {self.codigo}: {self.porcentagem}% - R$ {self.valor:.2f}"
