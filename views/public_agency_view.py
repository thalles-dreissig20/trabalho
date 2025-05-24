# Exception;
from exceptions.index import MenuOptionError

class PublicAgencyView:
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU DA AGENCIA =====")
                print("1. Sobre a agencia")
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



    def show_public_agency(self, agency_data: dict):
        print('\n\n')
        print(
            f"╔════════════════════════════════════════════════════╗\n"
            f"║ Nome:          {agency_data['Nome']}\n"
            f"║ CNPJ:          {agency_data['CNPJ']}\n"
            f"║ Email:         {agency_data['Email']}\n"
            f"║ Telefone:      {agency_data['Telefone']}\n"
            f"╚════════════════════════════════════════════════════╝\n"
        )