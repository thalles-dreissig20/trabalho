# Helpers;
from helpers.index import Validator
from tabulate import tabulate
# Exceptions;
from exceptions.index import MenuOptionError

class InvoiceView:    
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU DE NOTAS =====")
                print("1. Cadastrar nota")
                print("2. Listar notas")
                print("3. Alterar nota")
                print("4. Aprovar nota")
                print("5. Excluir nota")
                print("0. Retornar")
                opcao = int(input("Escolha a opção: "))
                
                if opcao not in [0, 1, 2, 3, 4, 5]:
                    raise MenuOptionError()
                return opcao
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)
    

    def form(self, total_price):
        tipo = input("Tipo (NF/Fatura): ")
        
        while True:
            data_str = input("Data (DD-MM-YYYY): ")
            data = Validator.validate_data(data_str)
            if data:
                break

        while True:
            try:
                valor_total = float(input("Valor total: "))
                if valor_total > total_price:
                    print("Valor total não pode ser maior que o valor do compromisso.")
                    continue
                break
            except ValueError:
                print("Digite um valor numérico válido.")

        tax = input("Aplicar imposto? (S/N): ").strip().upper()
        return tipo, data, valor_total, tax



    def update_invoice_fields(self, invoice):
        while True:
            print(f"\n--- Editar Nota: {invoice.code} ---")
            print("1. Tipo")
            print("2. Data")
            print("3. Valor total")
            print("0. Voltar")
            op = input("Escolha o campo a editar: ")

            match op:
                case "1":
                    invoice.type = input("Novo tipo (NF/Fatura): ")
                case "2":
                    while True:
                        nova_data = input("Data (DD-MM-YYYY): ")
                        data_validada = Validator.validate_data(nova_data)
                        if data_validada:
                            invoice.date = data_validada
                            break
                case "3":
                    try:
                        invoice.total_price = float(input("Novo valor total: "))
                    except ValueError:
                        print("Valor inválido.")
                case "0":
                    break
                case _:
                    print("Opção inválida.")


    def get_invoice(self):
        try:
            return int(input("Código da nota: "))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            return None


    def show_invoices(self, invoices):
        if not invoices:
            print("Nenhuma nota fiscal cadastrada.")
            return

        print('\n\n')
        headers = [
            "Código", "Tipo", "Data", "Valor Total",
            "Aprovada", "Descrição",
            "Empresa Prestadora", "Agência Pública"
        ]

        table_data = []
        for inv in invoices:
            table_data.append([
                inv.code,
                inv.type,
                inv.date,
                f"R$ {inv.total_price:,.2f}",
                "Sim" if inv.approved else "Não",
                inv.commitment.description,
                inv.company.social_reason,
                inv.public_agency.social_reason,
            ])

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", stralign="left"))