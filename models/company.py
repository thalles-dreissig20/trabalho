class Company:
    def __init__(self, cnpj: str, social_reason: str):
        self.cnpj = cnpj
        self.social_reason = social_reason

    def __str__(self):
        return (
            f"╔══════════════════════════════════════════╗\n"
            f"║ Empresa: {self.social_reason}\n"
            f"║ CNPJ:    {self.cnpj}\n"
            f"╚══════════════════════════════════════════╝"
        )