class InvoiceView:
    def main_menu(self):
        print("\n===== MENU =====")
        print("1. Cadastrar nota")
        print("2. Listar notas")
        print("3. Alterar nota")
        print("4. Excluir nota")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao:"))
        return opcao
    

    def get_invoice_data(self):
        codigo = input("Código da nota: ")
        tipo = input("Tipo (NF/Fatura): ")
        data = input("Data (YYYY-MM-DD): ")
        valor_total = float(input("Valor total: "))
        return codigo, tipo, data, valor_total

    def show_invoices(self, invoices):
        print("\n--- NOTAS FISCAIS ---")
        for i, inv in enumerate(invoices):
            print(f"[{i}]")
            print(inv)
            print()

    def select_invoice_index(self, invoices):
        self.show_invoices(invoices)
        try:
            index = int(input("Escolha o número da nota: "))
            if 0 <= index < len(invoices):
                return index
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida.")
        return None

    def update_invoice_fields(self, invoice):
        while True:
            print(f"\n--- Editar Nota: {invoice} ---")
            print("1. Código")
            print("2. Tipo")
            print("3. Data")
            print("4. Valor total")
            print("5. Empresa")
            print("0. Voltar")
            op = input("Escolha o campo a editar: ")

            match op:
                case "1":
                    invoice.codigo = input("Novo código: ")
                case "2":
                    invoice.tipo = input("Novo tipo (NF/Fatura): ")
                case "3":
                    invoice.data = input("Nova data (YYYY-MM-DD): ")
                case "4":
                    try:
                        invoice.valor_total = float(input("Novo valor total: "))
                    except ValueError:
                        print("Valor inválido.")
                case "5":
                    invoice.empresa = input("Nova empresa: ")
                case "0":
                    break
                case _:
                    print("Opção inválida.")
                    
    def show_message(self, msg):
        print(f"\n{msg}")