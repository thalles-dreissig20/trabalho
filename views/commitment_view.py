# Helpers;
from helpers.index import Validator
from tabulate import tabulate
from datetime import datetime

class CommitmentView:
    def main_menu(self):
        print("\n===== MENU COMPROMISSO =====")
        print("1. Cadastrar compromisso")
        print("2. Listar compromissos")
        print("3. Alterar compromisso")
        print("4. Excluir compromisso")
        print("0. Retornar")
        opcao = int(input("Escolha a opção: "))
        return opcao
    

    def form(self):
        description = input("Descrição do compromisso: ")
        
        while True:
            data_str = input("Data do compromisso (DD-MM-AAAA): ")
            date = Validator.validate_data(data_str)
            if date:
                break

        while True:
            try:
                amount = float(input("Valor do compromisso: "))
                break
            except ValueError:
                print("Digite um valor numérico válido.")

        return description, date, amount

    
    def get_commitment(self):
        try:
            return int(input("Código do compromisso: "))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            return None

    def show_commitments(self, commitments):
        if not commitments:
            print("Nenhum compromisso cadastrado.")
            return
        print('\n\n')
        headers = [
            "Código", "Descrição", "Data", "Valor",
            "Empresa", "CNPJ", "Agência Pública"
        ]

        table_data = []
        for commitment in commitments:
            if isinstance(commitment.date, str):
                try:
                    date_obj = datetime.strptime(commitment.date, "%Y-%m-%d")
                except ValueError:
                    date_obj = commitment.date
            else:
                date_obj = commitment.date

            table_data.append([
                commitment.code,
                commitment.description,
                date_obj.strftime('%d/%m/%Y') if hasattr(date_obj, "strftime") else str(date_obj),
                f"R$ {commitment.amount:,.2f}",
                commitment.company.social_reason,
                commitment.company.cnpj,
                commitment.public_agency.social_reason,
            ])

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", stralign="left"))