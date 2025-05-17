class PublicAgencyView:
    def main_menu(self):
        print("\n===== MENU =====")
        print("1. Sobre")
        print("2. Listar companias")
        print("3. Listar notas fiscais")
        print("4. Relatorio")
        print("0. Retornar")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def show_public_agency(self, public_agency):
        """Exibe os dados principais da entidade (social reason, CNPJ, etc.)."""
        print(
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Nome:          {public_agency.social_reason}\n"
            f"║ CNPJ:          {public_agency.cnpj}\n"
            f"║ Capital:       R$ {public_agency.amount:,.2f}\n"
            f"║ Email:         {public_agency.email or 'N/A'}\n"
            f"║ Telefone:      {public_agency.phone or 'N/A'}\n"
            f"╚════════════════════════════════════════════════════╝\n"
        )

    def show_companies(self, public_agency):
        """Exibe as companhias cadastradas na entidade."""
        companies_str = "\n".join([
            f"║ {idx}. {company.social_reason} CNPJ: {company.cnpj}"
            for idx, company in enumerate(public_agency.companies, start=1)
        ])
        print(
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Companias cadastradas:\n"
            f"{companies_str if companies_str else '║ Nenhuma empresa cadastrada.'}\n"
            f"╚════════════════════════════════════════════════════╝\n"
        )

    def show_invoices(self, public_agency):
        invoices_str = "\n".join([
            f"║ {idx}. Código: {invoice.code} | Tipo: {invoice.type} | "
            f"Total: R$ {invoice.total_price:,.2f} | Empresa: {invoice.company.social_reason}"
            for idx, invoice in enumerate(public_agency.invoices, start=1)
        ])
        print(
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Notas fiscais cadastradas:\n"
            f"{invoices_str if invoices_str else '║ Nenhuma nota fiscal cadastrada.'}\n"
            f"╚════════════════════════════════════════════════════╝\n"
        )

    def report(self, public_agency):
        total_companies = len(public_agency.companies)
        total_invoices = len(public_agency.invoices)
        total_faturamento = sum(invoice.total_price for invoice in public_agency.invoices)

        print("╔════════════════════════════════════════════════════╗")
        print("║            RELATÓRIO GERAL DA ENTIDADE")
        print("╠════════════════════════════════════════════════════╣")
        print(f"║ Nome:          {public_agency.social_reason}")
        print(f"║ CNPJ:          {public_agency.cnpj}")
        print(f"║ Capital:       R$ {public_agency.amount:,.2f}")
        print(f"║ Email:         {public_agency.email or 'N/A'}")
        print(f"║ Telefone:      {public_agency.phone or 'N/A'}")
        print("╚════════════════════════════════════════════════════╝\n")

        print("╔════════════════════════════════════════════════════╗")
        print("║            COMPANHIAS CADASTRADAS")
        print("╠════════════════════════════════════════════════════╣")
        if total_companies:
            for idx, company in enumerate(public_agency.companies, start=1):
                print(f"║ {idx}. {company.social_reason} - CNPJ: {company.cnpj}")
        else:
            print("║ Nenhuma companhia cadastrada.")
        print("╚════════════════════════════════════════════════════╝\n")

        print("╔════════════════════════════════════════════════════╗")
        print("║            NOTAS FISCAIS CADASTRADAS")
        print("╠════════════════════════════════════════════════════╣")
        if total_invoices:
            for idx, invoice in enumerate(public_agency.invoices, start=1):
                print(
                    f"║ {idx}. Código: {invoice.code} | Tipo: {invoice.type} | "
                    f"Total: R$ {invoice.total_price:,.2f}\n"
                    f"║    Empresa: {invoice.company.social_reason} - CNPJ: {invoice.company.cnpj}"
                )
        else:
            print("║ Nenhuma nota fiscal cadastrada.")
        print("╚════════════════════════════════════════════════════╝\n")

        print("╔════════════════════════════════════════════════════╗")
        print("║                 RESUMO FINAL")
        print("╠════════════════════════════════════════════════════╣")
        print(f"║ Total de notas fiscais: {total_invoices}")
        print(f"║ Despesas total:         R$ {total_faturamento:,.2f}")
        print("╚════════════════════════════════════════════════════╝\n")
