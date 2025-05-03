class EntityView:
    def main_menu(self):
        print("\n===== MENU =====")
        print("1. Sobre")
        print("2. Listar companias")
        print("3. Listar notas")
        print("0 - Retornar")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def show_entity(self, entity):
        """Exibe os dados principais da entidade (social reason, CNPJ, etc.)."""
        print(
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Nome:          {entity.social_reason}\n"
            f"║ CNPJ:          {entity.cnpj}\n"
            f"║ Capital:       R$ {entity.amount:,.2f}\n"
            f"║ Email:         {entity.email or 'N/A'}\n"
            f"║ Telefone:      {entity.phone or 'N/A'}\n"
            f"╚════════════════════════════════════════════════════╝\n"
        )

    def show_companies(self, entity):
        """Exibe as companhias cadastradas na entidade."""
        companies_str = "\n".join([
            f"║ {idx}. {company.social_reason} CNPJ: {company.cnpj}"
            for idx, company in enumerate(entity.companies, start=1)
        ])
        print(
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Companias cadastradas:\n"
            f"{companies_str if companies_str else '║ Nenhuma empresa cadastrada.'}\n"
            f"╚════════════════════════════════════════════════════╝\n"
        )

    def show_invoices(self, entity):
        invoices_str = "\n".join([
            f"║ {idx}. Código: {invoice.code} | Tipo: {invoice.type} | "
            f"Total: R$ {invoice.total_price:,.2f} | Empresa: {invoice.company.social_reason}"
            for idx, invoice in enumerate(entity.invoices, start=1)
        ])
        print(
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Notas fiscais cadastradas:\n"
            f"{invoices_str if invoices_str else '║ Nenhuma nota fiscal cadastrada.'}\n"
            f"╚════════════════════════════════════════════════════╝\n"
        )
