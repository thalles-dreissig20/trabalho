
class CompanyView:
    def main_menu(self):
        print("\n===== MENU =====")
        print("1. Cadastrar empresa")
        print("2. Listar empresas")
        print("3. Alterar empresa")
        print("4. Excluir empresa")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao:"))
        return opcao
    
    def get_company_data(self):
        cnpj = input("Digite o CNPJ: ")
        nome = input("Digite a razão social: ")
        return cnpj, nome

    def select_company_index(self, empresas):
        if not empresas:
            print("Nenhuma empresa cadastrada.")
            return None
        self.show_companies(empresas)
        index = int(input("Escolha o número da empresa: "))
        if 0 <= index < len(empresas):
            return index
        else:
            print("Índice inválido.")
            return None

    def show_companies(self, empresas):
        print("\n--- EMPRESAS ---")
        for i, empresa in enumerate(empresas):
            print(f"[{i}]")
            print(empresa)
            print()

    def show_message(self, msg):
        print(f"\n{msg}")