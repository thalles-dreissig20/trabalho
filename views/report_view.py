# Helpers;
from helpers.index import validate_data

# Exception;
from exceptions.index import MenuOptionError

class ReportView:
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU DE RELATÓRIOS =====")
                print("1. Relatório Geral")
                print("2. Relatório por Companhia")
                print("3. Relatório por Nota Fiscal")
                print("4. Relatório por Compromisso")
                print("5. Relatório por Data")
                print("0. Retornar")
                opcao = int(input("Escolha a opção: "))
                
                if opcao not in [0, 1, 2, 3, 4, 5]:
                    raise MenuOptionError()
                return opcao
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)



    def general_report(self, public_agency):
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



    def per_company_report(self, company, invoices):
        total_invoices = len(invoices)
        total_faturamento = sum(invoice.total_price for invoice in invoices)
        print("╔════════════════════════════════════════════════════╗")
        print("║            RELATÓRIO POR COMPANHIA")
        print("╠════════════════════════════════════════════════════╣")
        print(f"║ Nome:          {company.social_reason}")
        print(f"║ CNPJ:          {company.cnpj}")
        print("╚════════════════════════════════════════════════════╝\n")
        print("╔════════════════════════════════════════════════════╗")
        print("║            NOTAS FISCAIS CADASTRADAS")
        print("╠════════════════════════════════════════════════════╣")
        if total_invoices:
            for idx, invoice in enumerate(invoices, start=1):
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




    def per_invoice_report(self):
        print("╔════════════════════════════════════════════════════╗")
        print("║            RELATÓRIO POR NOTA FISCAL")
        print("╠════════════════════════════════════════════════════╣")
        print("║ Escolha uma nota fiscal:")
        # Aqui você pode adicionar a lógica para listar as notas fiscais e permitir que o usuário escolha uma
        print("╚════════════════════════════════════════════════════╝\n")



    def per_commitment_report(self):
        print("╔════════════════════════════════════════════════════╗")
        print("║            RELATÓRIO POR COMPROMISSO")
        print("╠════════════════════════════════════════════════════╣")
        print("║ Escolha um compromisso:")
        # Aqui você pode adicionar a lógica para listar os compromissos e permitir que o usuário escolha um
        print("╚════════════════════════════════════════════════════╝\n")


    def per_date_report(self, invoices):
        while True:
            data_str_from = input("Data inicial (DD-MM-YYYY): ")
            data_str_to = input("Data final (DD-MM-YYYY): ")

            date_from = validate_data(data_str_from)
            date_to = validate_data(data_str_to)

            if date_from and date_to:
                break
            else:
                print("Uma ou ambas as datas são inválidas. Tente novamente.")

        print("╔════════════════════════════════════════════════════╗")
        print("║            RELATÓRIO POR DATA")
        print("╠════════════════════════════════════════════════════╣")
        print(f"║ Período: {date_from.strftime('%d-%m-%Y')} a {date_to.strftime('%d-%m-%Y')}")
        print("╚════════════════════════════════════════════════════╝\n")

        filtered_invoices = [inv for inv in invoices if date_from <= inv.date <= date_to]

        if filtered_invoices:
            print("╔════════════════════════════════════════════════════╗")
            print("║            NOTAS FISCAIS CADASTRADAS")
            print("╚════════════════════════════════════════════════════╝\n")
            for idx, inv in enumerate(filtered_invoices, start=1):
                print(
                    f"╔══════════════════════════════════════════════════════════════════════╗\n"
                    f"║ {idx}. Código:       {inv.code}\n"
                    f"║    Tipo:         {inv.type}\n"
                    f"║    Data:         {inv.date.strftime('%d-%m-%Y')}\n"
                    f"║    Valor Total:  R$ {inv.total_price:,.2f}\n"
                    f"║    Aprovada:     {'Sim' if inv.approved else 'Não'}\n"
                    f"║ ----------------------------------------------------------------------\n"
                    f"║ Retenções:\n" +
                    ("".join(f"║   • {ret.name} ({ret.rate}%)\n" for ret in inv.retentions) if inv.retentions else "║   Nenhuma taxa associada\n") +
                    f"║ ----------------------------------------------------------------------\n"
                    f"║ Empresa prestadora: {inv.company.social_reason}\n"
                    f"║ CNPJ:               {inv.company.cnpj}\n"
                    f"║ ----------------------------------------------------------------------\n"
                    f"║ Agencia pública Associada:   {inv.public_agency.social_reason}\n"
                    f"╚══════════════════════════════════════════════════════════════════════╝\n"
                )
        else:
            print("║ Nenhuma nota fiscal cadastrada nesse período.")
            print("╚════════════════════════════════════════════════════╝\n")

        print("╔════════════════════════════════════════════════════╗")
        print("║                 RESUMO FINAL")
        print("╠════════════════════════════════════════════════════╣")
        print(f"║ Total de notas fiscais: {len(filtered_invoices)}")
        print(f"║ Despesas total:         R$ {sum(inv.total_price for inv in filtered_invoices):,.2f}")
        print("╚════════════════════════════════════════════════════╝\n")