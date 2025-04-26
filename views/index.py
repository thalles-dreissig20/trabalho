class IndexView:
    def main_menu(self):
        print("\n===== MENU =====")
        print("1. Empresas")
        print("2. Notas fiscais")
        print("3. Aprovar todos os pagamentos")
        print("4. Homologar todos os pagamentos")
        print("0. Sair")
        opcao = int(input("Escolha a opcao:"))
        return opcao
