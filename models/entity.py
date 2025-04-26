from models.tax import Tax

class Entity:
    def __init__(
        self,
        cnpj: str,
        social_reason: str,
        amount: float,
        email: str = "",
        phone: str = ""
    ):
        self.cnpj = cnpj
        self.social_reason = social_reason
        self.amount = amount 
        self.email = email
        self.phone = phone
        self.companies = []
        self.__taxes = [
            Tax("ISS", 5.0, "Serviço"),
            Tax("ICMS", 18.0, "Produto"),
            Tax("INSS", 11.0, "Folha"),
        ]
        

    def __str__(self):
        companies_str = "\n".join([
            f"║ {idx}. {company.social_reason} CNPJ: {company.cnpj}"
            for idx, company in enumerate(self.companies, start=1)
        ])
        return (
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Nome:          {self.social_reason}\n"
            f"║ CNPJ:          {self.cnpj}\n"
            f"║ Capital:       R$ {self.amount:,.2f}\n"
            f"║ Email:         {self.email or 'N/A'}\n"
            f"║ Telefone:      {self.phone or 'N/A'}\n"
            f"╚════════════════════════════════════════════════════╝\n"
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Companias cadastradas:\n"
            f"{companies_str if companies_str else '║ Nenhuma empresa cadastrada.'}\n"
            f"╚════════════════════════════════════════════════════╝\n"
        )

    ################################################################################
    # METHODS;

    def add_company(self, company):
        self.companies.append(company)

    def get_companies(self):
        return self.companies

    def list_companies(self):
        for idx, company in enumerate(self.companies, start=1):
            print(f"{idx}. {company.social_reason} - CNPJ: {company.cnpj}")