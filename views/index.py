class IndexView:
    def main_menu(self):
        print("\n===== MENU =====")
        print("1. Empresas")
        print("2. Notas fiscais")
        print("3. Ver empenhos")
        print("4. Simular pagamentos")
        print("5. Ver pagamentos")
        print("6. Aprovar todos os pagamentos")
        print("7. Homologar todos os pagamentos")
        print("0. Sair")
        opcao = int(input("Escolha a opcao:"))
        return opcao
