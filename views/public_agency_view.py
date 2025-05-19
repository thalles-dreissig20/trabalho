# Exception;
from exceptions.index import MenuOptionError

class PublicAgencyView:
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU DA AGENCIA =====")
                print("1. Sobre")
                print("2. Listar companias")
                print("3. Listar notas fiscais")
                print("4. Relatorio")
                print("0. Retornar")
                opcao = int(input("Escolha a opção: "))
                
                if opcao not in [0, 1, 2, 3, 4]:
                    raise MenuOptionError()
                return opcao
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)



    def show_public_agency(self, public_agency):
        print(
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Nome:          {public_agency.social_reason}\n"
            f"║ CNPJ:          {public_agency.cnpj}\n"
            f"║ Capital:       R$ {public_agency.amount:,.2f}\n"
            f"║ Email:         {public_agency.email or 'N/A'}\n"
            f"║ Telefone:      {public_agency.phone or 'N/A'}\n"
            f"╚════════════════════════════════════════════════════╝\n"
        )