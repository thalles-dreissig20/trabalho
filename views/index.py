# Exceptions;
from exceptions.index import MenuOptionError

class IndexView:
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU =====")
                print("1. Agencia")
                print("2. Companias")
                print("3. Notas fiscais")
                print("4. Empenhos")
                print("5. Retenções")
                print("0. Sair")
                opcao = int(input("Escolha a opcao: "))
                
                if opcao not in [0, 1, 2, 3, 4, 5]:
                    raise MenuOptionError()
                return opcao

            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)
                
    def show_message(self, msg):
        print(f"\n{msg}")