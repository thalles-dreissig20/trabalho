
class CompanyView:
    def __str__(self):
        return (
            f"╔══════════════════════════════════════════╗\n"
            f"║ Empresa: {self.__social_reason}\n"
            f"║ CNPJ:    {self.__cnpj}\n"
            f"╚══════════════════════════════════════════╝"
        )
    
    def main_menu(self):
        print("\n===== MENU =====")
        print("1. Cadastrar empresa")
        print("2. Listar empresas")
        print("3. Alterar empresa")
        print("4. Excluir empresa")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao:"))
        return opcao
    
    def form(self):
        cnpj = input("Digite o CNPJ: ")
        nome = input("Digite a razão social: ")
        return cnpj, nome

    def get_company(self, companies):
        if not companies:
            print("Nenhuma empresa cadastrada.")
            return None
        self.show_companies(companies)
        index = int(input("Escolha o número da empresa: "))
        if 0 <= index < len(companies):
            return index
        else:
            print("Índice inválido.")
            return None

    def show_companies(self, companies):
        print("\n--- EMPRESAS ---")
        for i, company in enumerate(companies):
            print(f"[{i}]")
            print(f"Razão Social: {company.social_reason}")
            print(f"CNPJ: {company.cnpj}")
            print(f"Entidade Associada: {company.entity.social_reason}")
            print()

    def show_message(self, msg):
        print(f"\n{msg}")