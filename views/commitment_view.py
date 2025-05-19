# Helpers;
from helpers.index import validate_data

class CommitmentView:
    def main_menu(self):
        print("\n===== MENU COMPROMISSO =====")
        print("1. Cadastrar compromisso")
        print("2. Listar compromissos")
        print("3. Alterar compromisso")
        print("4. Excluir compromisso")
        print("0. Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao
    

    def form(self):
        description = input("Descrição do compromisso: ")
        while True:
            data_str = input("Data do compromisso (DD/MM/AAAA): ")
            date = validate_data(data_str)
            if date:
                break
        amount = float(input("Valor do compromisso: "))
        return description, date, amount

    
    def get_commitment(self):
        try:
            return int(input("Código do compromisso: "))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            return None


    def show_commitments(self, commitments):
        print("\n--- COMPROMISSOS ---")
        for i, commitment in enumerate(commitments):
            print(
                f"╔══════════════════════════════════════════════════════════╗\n"
                f"║ Código:       {commitment.code}\n"
                f"║ Descrição:    {commitment.description}\n"
                f"║ Data:         {commitment.date}\n"
                f"║ Valor:        R$ {commitment.amount}\n"
                f"║ ----------------------------------------------------------\n"
                f"║ Agencia pública Associada:   {commitment.public_agency.social_reason}\n"
                f"╚══════════════════════════════════════════════════════════╝\n"
            )