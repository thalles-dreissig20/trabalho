# Exceptions;
from exceptions.index import MenuOptionError

class InvoiceView:
    def __str__(self):
        return (
            f"╔══════════════════════════════════════════╗\n"
            f"║ Código:         {self.__code}\n"
            f"║ Tipo:           {self.__type}\n"
            f"║ Data:           {self.__date}\n"
            f"║ Valor Total:    R$ {self.__total_price:.2f}\n"
            f"║ Aprovada:       {self.__approved}\n"
            f"╚══════════════════════════════════════════╝ \n" 
            f"{self.__company}\n"
        )
    
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU DE NOTAS =====")
                print("1. Cadastrar nota")
                print("2. Listar notas")
                print("3. Alterar nota")
                print("4. Aprovar nota")
                print("5. Excluir nota")
                print("0 - Retornar")
                opcao = int(input("Escolha a opcao:"))
                
                if opcao not in [0, 1, 2, 3, 4, 5]:
                    raise MenuOptionError()
                return opcao
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)
    

    def form(self):
        tipo = input("Tipo (NF/Fatura): ")
        data = input("Data (YYYY-MM-DD): ")
        valor_total = float(input("Valor total: "))
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
                    invoice.date = input("Nova data (YYYY-MM-DD): ")
                case "3":
                    try:
                        invoice.total_price = float(input("Novo valor total: "))
                    except ValueError:
                        print("Valor inválido.")
                case "0":
                    break
                case _:
                    print("Opção inválida.")


    def get_invoice(self, invoices):
        if not invoices:
            print("Nenhuma nota cadastrada.")
            return None
        
        self.show_invoices(invoices)
        
        try:
            codigo = int(input("Digite o código da nota: "))
            for invoice in invoices:
                if invoice.code == codigo:
                    return invoice
            print("Código inválido. Nenhuma nota encontrada com esse código.")
            return None
        
        except ValueError:
            print("Entrada inválida.")
        return None


    def show_invoices(self, invoices):
        print("\n--- NOTAS FISCAIS ---")
        for i, inv in enumerate(invoices):
            print(
                f"╔══════════════════════════════════════════════════════════════════════╗\n"
                f"║ Código:       {inv.code}\n"
                f"║ Tipo:         {inv.type}\n"
                f"║ Data:         {inv.date}\n"
                f"║ Valor Total:  R$ {inv.total_price:,.2f}\n"
                f"║ Aprovada:     {inv.approved}\n"
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