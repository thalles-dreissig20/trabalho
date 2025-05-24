# Helpers;
from helpers.index import Validator
from tabulate import tabulate
from datetime import datetime, date
from collections import defaultdict
# Exception;
from exceptions.index import MenuOptionError

class ReportView:
    #############################################################################
    # Menu;
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU DE RELATÓRIOS =====")
                print("1. Relatório Geral")
                print("2. Relatório por Compromisso")
                print("3. Relatório por Data")
                print("0. Retornar")
                opcao = int(input("Escolha a opção: "))
                
                if opcao not in [0, 1, 2, 3, 4, 5]:
                    raise MenuOptionError()
                return opcao
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)

    #############################################################################
    # Methods;

    def format_retentions(self, invoice, retentions, retention_totals):
        ret_map = {r.name: r for r in invoice.retentions}
        ret_values = []
        total_impostos_nota = 0.0

        for r in retentions:
            if r.name in ret_map:
                reten = ret_map[r.name]
                reten_valor = invoice.total_price * (reten.rate / 100)
                retention_totals[r.name] += reten_valor
                total_impostos_nota += reten_valor
                ret_values.append(f"{reten.rate}%")
            else:
                ret_values.append("-")

        ret_values.append(f"R$ {total_impostos_nota:,.2f}")
        return ret_values, total_impostos_nota

    def general_report(self, public_agency, retentions): 
        total_companies = len(public_agency.companies)
        total_invoices = len(public_agency.invoices)
        total_faturamento = sum(invoice.total_price for invoice in public_agency.invoices)

        retention_totals = defaultdict(float)
        total_all_retencoes = 0.0

        print('\n\n')
        print("           COMPANHIAS CADASTRADAS      ")
        if total_companies:
            companies_table = []
            for idx, company in enumerate(public_agency.companies, start=1):
                companies_table.append([idx, company.social_reason, company.cnpj])
            headers = ["#", "Razão Social", "CNPJ"]
            print(tabulate(companies_table, headers=headers, tablefmt="fancy_grid", stralign="left"))
        else:
            print("Nenhuma companhia cadastrada.\n")

        print('\n\n')
        print("           NOTAS FISCAIS CADASTRADAS      ")
        if total_invoices:
            invoice_table = []
            for invoice in public_agency.invoices:
                codigo = invoice.code
                tipo = invoice.type
                desc = invoice.commitment.description[:50]
                company = invoice.company.social_reason
                valor = f"R$ {invoice.total_price:,.2f}"
                aprovada = "Sim" if invoice.approved else "Não"

                ret_values, total_impostos_nota = self.format_retentions(invoice, retentions, retention_totals)
                total_all_retencoes += total_impostos_nota

                invoice_table.append([codigo, tipo, desc, company, valor, aprovada] + ret_values)

            retention_total_cells = [f"R$ {retention_totals[r.name]:,.2f}" for r in retentions]
            retention_total_cells.append(f"R$ {total_all_retencoes:,.2f}")

            invoice_table.append([f"{total_invoices} Notas", "", "TOTAL", "", f"R$ {total_faturamento:,.2f}", ""] + retention_total_cells)

            headers = ["Código", "Tipo", "Descrição de Compromisso", "Empresa", "Valor", "Aprovada"] + [r.name for r in retentions] + ["Total de Impostos"]
            print(tabulate(invoice_table, headers=headers, tablefmt="fancy_grid", stralign="center", numalign="right"))
        else:
            print("Nenhuma nota fiscal cadastrada.\n")

    def per_commitment_report(self, commitment, invoices, retentions):
        print('\n\n')
        print("           RELATÓRIO DE NOTAS POR COMPROMISSO       ")

        table_data = []
        related_invoices = [inv for inv in invoices if inv.commitment.code == commitment.code]
        retention_totals = defaultdict(float)
        total_all_retencoes = 0.0

        if related_invoices:
            for invoice in related_invoices:
                ret_values, total_impostos_nota = self.format_retentions(invoice, retentions, retention_totals)
                total_all_retencoes += total_impostos_nota
                table_data.append([
                    commitment.code,
                    commitment.description,
                    invoice.type,
                    f"R$ {invoice.total_price:,.2f}",
                    "Sim" if invoice.approved else "Não"
                ] + ret_values)

            total_line = ["", "", "TOTAL", "", ""] + [f"R$ {retention_totals[r.name]:,.2f}" for r in retentions] + [f"R$ {total_all_retencoes:,.2f}"]
            table_data.append(total_line)

        headers = ["Código Compromisso", "Descrição", "Tipo", "Valor da Nota Fiscal", "Aprovada"] + [r.name for r in retentions] + ["Total de Impostos"]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", stralign="left"))

    def per_date_report(self, invoices, retentions):
        while True:
            data_str_from = input("Data inicial (DD-MM-YYYY): ")
            data_str_to = input("Data final (DD-MM-YYYY): ")

            date_from = Validator.validate_data(data_str_from)
            date_to = Validator.validate_data(data_str_to)

            if date_from and date_to:
                break
            else:
                print("Uma ou ambas as datas são inválidas. Tente novamente.")

        print('\n\n')
        print("           RELATÓRIO POR DATA")
        print('\n')
        print(f"Período: {date_from} a {date_to}")

        filtered_invoices = [
            inv for inv in invoices
            if date_from <= (
                inv.date if isinstance(inv.date, date)
                else datetime.strptime(inv.date, '%d-%m-%Y').date()
            ) <= date_to
        ]

        retention_totals = defaultdict(float)
        total_all_retencoes = 0.0

        if filtered_invoices:
            total_faturamento = sum(inv.total_price for inv in filtered_invoices)

            table_data = []
            for inv in filtered_invoices:
                codigo = inv.code
                tipo = inv.type
                desc = inv.commitment.description[:50]
                inv_date = inv.date
                valor = f"R$ {inv.total_price:,.2f}"
                aprovada = "Sim" if inv.approved else "Não"

                ret_values, total_impostos_nota = self.format_retentions(inv, retentions, retention_totals)
                total_all_retencoes += total_impostos_nota

                table_data.append([codigo, tipo, desc, inv_date, valor, aprovada] + ret_values)

            total_line = ["", "", "TOTAL", "", f"R$ {total_faturamento:,.2f}", ""] + [f"R$ {retention_totals[r.name]:,.2f}" for r in retentions] + [f"R$ {total_all_retencoes:,.2f}"]
            table_data.append(total_line)

            headers = ["Código", "Tipo", "Descrição de Compromisso", "Data", "Valor", "Aprovada"] + [r.name for r in retentions] + ["Total de Impostos"]
            print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", stralign="center", numalign="right"))
        else:
            print("Nenhuma nota fiscal encontrada no período informado.\n")