# Exceptions;
from exceptions.index import MenuOptionError

class CompanyView:
    def __str__(self):
        return (
            f"╔══════════════════════════════════════════╗\n"
            f"║ Empresa: {self.__social_reason}\n"
            f"║ CNPJ:    {self.__cnpj}\n"
            f"╚══════════════════════════════════════════╝"
        )
    
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU EMPRESAS =====")
                print("1. Cadastrar empresa")
                print("2. Listar empresas")
                print("3. Alterar empresa")
                print("4. Excluir empresa")
                print("0 - Retornar")
                opcao = int(input("Escolha a opcao:"))
                
                if opcao not in [0, 1, 2, 3, 4]:
                    raise MenuOptionError()
                return opcao

            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)

    
    def form(self):
        cnpj = input("Digite o CNPJ: ")
        nome = input("Digite a razão social: ")
        return cnpj, nome

    def get_company(self, companies):
        if not companies:
            print("Nenhuma empresa cadastrada.")
            return None

        self.show_companies(companies)

        try:
            codigo = int(input("Digite o código da empresa: "))
            for company in companies:
                if company.code == codigo:
                    return company
            print("Código inválido. Nenhuma empresa encontrada com esse código.")
            return None
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            return None

    def show_companies(self, companies):
        print("\n--- EMPRESAS ---")
        for i, company in enumerate(companies):
            print(
                f"╔══════════════════════════════════════════════════════════╗\n"
                f"║ Código:       {company.code}\n"
                f"║ Razão Social: {company.social_reason}\n"
                f"║ CNPJ:         {company.cnpj}\n"
                f"║ ----------------------------------------------------------\n"
                f"║ Agencia pública Associada:   {company.public_agency.social_reason}\n"
                f"╚══════════════════════════════════════════════════════════╝\n"
            )