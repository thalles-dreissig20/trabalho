# Exceptions;
from exceptions.index import MenuOptionError
from tabulate import tabulate

from views.AbstractCodeView import AbstractCodeView
import dearpygui.dearpygui as dpg

class CompanyView(AbstractCodeView): 
    def main_menu(self):
        while True:
            try:
                print("\n===== MENU EMPRESAS =====")
                print("1. Cadastrar empresa")
                print("2. Listar empresas")
                print("3. Alterar empresa")
                print("4. Excluir empresa")
                print("0 - Retornar")
                opcao = int(input("Escolha a opção: "))
                
                if opcao not in [0, 1, 2, 3, 4]:
                    raise MenuOptionError()
                return opcao

            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except MenuOptionError as e:
                print(e)

    
    def form(self):
        self.input_cnpj = ""
        self.input_name = ""

        def submit_callback():
            self.input_cnpj = dpg.get_value("cnpj_input")
            self.input_name = dpg.get_value("name_input")
            dpg.stop_dearpygui()

        dpg.create_context()
        with dpg.window(label="Cadastro de Empresa", width=400, height=250):
            dpg.add_input_text(label="CNPJ", tag="cnpj_input")
            dpg.add_input_text(label="Razão Social", tag="name_input")
            dpg.add_button(label="Confirmar", callback=submit_callback)

        dpg.create_viewport(title='Formulário Empresa', width=400, height=250)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

        return self.input_cnpj, self.input_name


    def get_code(self, message="Digite o código:"):
        code_value = {"value": None}

        def submit():
            try:
                code_value["value"] = int(dpg.get_value("code_input"))
                dpg.stop_dearpygui()
            except ValueError:
                dpg.set_value("error_text", "❌ Digite um número válido.")

        dpg.create_context()
        with dpg.window(label="Código da Empresa", width=400, height=200):
            dpg.add_text(message)
            dpg.add_input_text(label="Código", tag="code_input")
            dpg.add_button(label="Confirmar", callback=submit)
            dpg.add_text("", tag="error_text", color=(255, 0, 0))

        dpg.create_viewport(title='Código da Empresa', width=400, height=200)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

        return code_value["value"]


    def show_companies(self, companies):
        dpg.create_context()
        with dpg.window(label="Empresas Cadastradas", width=800, height=500):
            if not companies:
                dpg.add_text("Nenhuma empresa cadastrada.")
            else:
                dpg.add_text("Lista de Empresas Cadastradas")
                with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp, row_background=True):
                    dpg.add_table_column(label="Código")
                    dpg.add_table_column(label="Razão Social")
                    dpg.add_table_column(label="CNPJ")
                    dpg.add_table_column(label="Agência Pública")

                    for company in companies:
                        with dpg.table_row():
                            dpg.add_text(str(company.code))
                            dpg.add_text(company.social_reason)
                            dpg.add_text(company.cnpj)
                            dpg.add_text(company.public_agency.social_reason)

        dpg.create_viewport(title='Empresas', width=800, height=500)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()