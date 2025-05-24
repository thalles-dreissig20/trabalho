# Exceptions;
from exceptions.index import MenuOptionError
from tabulate import tabulate

from views.AbstractCodeView import AbstractCodeView

class CompanyView(AbstractCodeView): 
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU EMPRESAS =====")
                print("1. Cadastrar empresa")
                print("2. Listar empresas")
                print("3. Alterar empresa")
                print("4. Excluir empresa")
                print("0 - Retornar")
                opcao = int(input("Escolha a opção: "))
                
                if opcao not in [0, 1, 2, 3, 4]:
                    raise MenuOptionError()
                return opcao

            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)

    
    def form(self):
        cnpj = input("Digite o CNPJ: ")
        nome = input("Digite a razão social: ")
        return cnpj, nome


    def show_companies(self, companies):
        if not companies:
            print("Nenhuma empresa cadastrada.")
            return
        print('\n\n')
        headers = ["Código", "Razão Social", "CNPJ", "Agência Pública Associada"]
        table_data = [
            [company.code, company.social_reason, company.cnpj, company.public_agency.social_reason]
            for company in companies
        ]

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", stralign="left"))