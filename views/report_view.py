# Helpers;
from helpers.index import Validator
from tabulate import tabulate
from datetime import datetime, date
from collections import defaultdict
# Exception;
from exceptions.index import MenuOptionError

from dearpygui import dearpygui as dpg

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


    def general_report_gui(self, public_agency, retentions, companies):
        retention_totals = defaultdict(float)
        total_all_retencoes = 0.0

        dpg.create_context()

        with dpg.window(label="Relatório Geral", width=900, height=600):
            dpg.add_text("Companhias Cadastradas")
            if companies:
                companies_data = [
                    [idx + 1, c.social_reason, c.cnpj]
                    for idx, c in enumerate(companies)
                ]
                with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp, row_background=True):
                    dpg.add_table_column(label="#")
                    dpg.add_table_column(label="Razão Social")
                    dpg.add_table_column(label="CNPJ")

                    for row in companies_data:
                        with dpg.table_row():
                            for cell in row:
                                dpg.add_text(cell)
            else:
                dpg.add_text("Nenhuma companhia cadastrada.")

            dpg.add_spacing(count=2)
            dpg.add_text("Notas Fiscais Cadastradas")

            if public_agency.invoices:
                invoices_data = []
                for invoice in public_agency.invoices:
                    codigo = invoice.code
                    tipo = invoice.type
                    desc = invoice.commitment.description[:50]
                    company = invoice.company.social_reason
                    valor = f"R$ {invoice.total_price:,.2f}"
                    aprovada = "Sim" if invoice.approved else "Não"

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
                    total_all_retencoes += total_impostos_nota

                    invoices_data.append([
                        codigo, tipo, desc, company, valor, aprovada
                    ] + ret_values)

                headers = ["Código", "Tipo", "Descrição", "Empresa", "Valor", "Aprovada"] + [r.name for r in retentions] + ["Total de Impostos"]

                with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp, row_background=True):
                    for header in headers:
                        dpg.add_table_column(label=header)

                    for row in invoices_data:
                        with dpg.table_row():
                            for cell in row:
                                dpg.add_text(cell)
            else:
                dpg.add_text("Nenhuma nota fiscal cadastrada.")

        dpg.create_viewport(title='Relatorio', width=900, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()


    def per_commitment_report_gui(self, commitment, invoices, retentions):
        retention_totals = defaultdict(float)
        total_all_retencoes = 0.0

        # Filtrar notas relacionadas ao compromisso
        related_invoices = [inv for inv in invoices if inv.commitment.code == commitment.code]

        # Montar dados da tabela
        table_data = []

        if related_invoices:
            for invoice in related_invoices:
                # Reusar seu método format_retentions para calcular os valores
                ret_values, total_impostos_nota = self.format_retentions(invoice, retentions, retention_totals)
                total_all_retencoes += total_impostos_nota
                row = [
                    commitment.code,
                    commitment.description,
                    invoice.type,
                    f"R$ {invoice.total_price:,.2f}",
                    "Sim" if invoice.approved else "Não"
                ] + ret_values
                table_data.append(row)

            # Linha de total
            total_line = ["", "", "TOTAL", "", ""] + [f"R$ {retention_totals[r.name]:,.2f}" for r in retentions] + [f"R$ {total_all_retencoes:,.2f}"]
            table_data.append(total_line)

        headers = ["Código Compromisso", "Descrição", "Tipo", "Valor da Nota Fiscal", "Aprovada"] + [r.name for r in retentions] + ["Total de Impostos"]

        dpg.create_context()

        with dpg.window(label=f"Relatório por Compromisso - {commitment.code}", width=900, height=400):
            if table_data:
                with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp, row_background=True):
                    for header in headers:
                        dpg.add_table_column(label=header)

                    for row in table_data:
                        with dpg.table_row():
                            for cell in row:
                                dpg.add_text(cell)
            else:
                dpg.add_text("Nenhuma nota fiscal relacionada a este compromisso.")

        dpg.create_viewport(title="Relatorio por Compromisso", width=900, height=400)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()





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


    #############################################################################
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


    #############################################################################
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