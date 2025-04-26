class Invoice:
    def __init__(self, codigo: str, tipo: str, data: str, valor_total: float, empresa):
        self.codigo = codigo
        self.tipo = tipo  # "NF" ou "Fatura"
        self.data = data
        self.valor_total = valor_total
        self.empresa = empresa  # agregação reversa

    def __str__(self):
        return (
            f"Nota Fiscal\n"
            f"╔══════════════════════════════════════════╗\n"
            f"║ Código:         {self.codigo}\n"
            f"║ Tipo:           {self.tipo}\n"
            f"║ Data:           {self.data}\n"
            f"║ Valor Total:    R$ {self.valor_total:.2f}\n"
            f"║ Empresa:        {self.empresa}\n"
            f"╚══════════════════════════════════════════╝"
        )