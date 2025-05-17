

class CommitmentView:
    def main_menu(self):
        print("\n===== MENU =====")
        print("1. Cadastrar compromisso")
        print("2. Listar compromissos")
        print("3. Alterar compromisso")
        print("4. Excluir compromisso")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao:"))
        return opcao
    

    def form(self):
        description = input("Descrição do compromisso: ")
        date = input("Data do compromisso (DD/MM/AAAA): ")
        amount = float(input("Valor do compromisso: "))
        return description, date, amount

    
    def get_commitment(self, commitments):
        if not commitments:
            print("Nenhum compromisso cadastrado.")
            return None
        self.show_commitments(commitments)
        index = int(input("Escolha o número do compromisso: "))
        if 0 <= index < len(commitments):
            return index
        else:
            print("Índice inválido.")
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
                f"║ ----\n"
                f"║ Agencia pública Associada:   {commitment.public_agency.social_reason}\n"
                f"╚══════════════════════════════════════════════════════════╝\n"
            )