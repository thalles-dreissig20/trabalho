class IndexView:
    def main_menu(self):
        print("\n===== MENU =====")
        print("1. Agencia")
        print("2. Companias")
        print("3. Notas fiscais")
        print("4. Empenhos")
        print("5. Retenções")
        print("0. Sair")
        opcao = int(input("Escolha a opcao:"))
        return opcao
