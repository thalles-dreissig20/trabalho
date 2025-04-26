from models.company import Company

class Invoice:
    def __init__(self, code: str, type: str, date: str, total_price: float, company: Company):
        self.code = code
        self.type = type
        self.date = date
        self.total_price = total_price
        self.company = company
        self.approved = False

    def approved_invoice(self):
        self.approved = True

    def __str__(self):
        return (
            f"╔══════════════════════════════════════════╗\n"
            f"║ Código:         {self.code}\n"
            f"║ Tipo:           {self.type}\n"
            f"║ Data:           {self.date}\n"
            f"║ Valor Total:    R$ {self.total_price:.2f}\n"
            f"║ Aprovada:       {self.approved}\n"
            f"╚══════════════════════════════════════════╝ \n" 
            f"{self.company}\n"
        )