# Exceptions;
from exceptions.index import MenuOptionError

class RetentionView:
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU RETENÇAO =====")
                print("1. Listar retenções")
                print("2. Atualizar retenções")
                print("0 - Retornar")
                opcao = int(input("Escolha a opcao: "))
                
                if opcao not in [0, 1, 2]:
                    raise MenuOptionError()
                return opcao
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)
    

    def get_retention(self): 
        try:
            return int(input("Digite o código da retenção: "))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            return None
    
    
    def form(self):
        active = int(input("A retenção está ativa? (1 - Sim, 0 - Não): "))
        return active
    

    def show_retentions(self, retentions):
        print("\n--- RETENÇÕES ---\n")
        for retention in retentions:
            print(
                f"╔═════════════════════════╗\n"
                f"║ Código:       {retention.code}\n"
                f"║ Nome:         {retention.name}\n"
                f"║ Percentual:   {retention.rate:.2f}%\n"
                f"║ Base Cálculo: R$ {retention.base_amount:,.2f}\n"
                f"║ Ativo:        {'Sim' if retention.active else 'Não'}\n"
                f"╚═════════════════════════╝\n"
            )
        