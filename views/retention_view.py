# Exceptions;
from exceptions.index import MenuOptionError
from tabulate import tabulate
from views.AbstractCodeView import AbstractCodeView
class RetentionView(AbstractCodeView):
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU RETENÇAO =====")
                print("1. Listar retenções")
                print("2. Atualizar retenções ")
                print("0. Retornar")
                opcao = int(input("Escolha a opção: "))
                
                if opcao not in [0, 1, 2]:
                    raise MenuOptionError()
                return opcao
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)
    
    
    def form(self):
        active = int(input("A retenção está ativa? (1 - Sim, 0 - Não): "))
        return active
    

    def show_retentions(self, retentions):
        if not retentions:
            print("Nenhuma retenção cadastrada.")
            return
        print('\n\n')
        headers = ["Código", "Nome", "Percentual (%)", "Ativo"]
        table_data = []

        for retention in retentions:
            table_data.append([
                retention.code,
                retention.name,
                f"{retention.rate:.2f}%",
                "Sim" if retention.active else "Não"
            ])

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", stralign="left", numalign="right"))
        print()