from models.company import Company
from views.company_view import CompanyView

class CompanyController:
    def __init__(self, index_controller):
        self.__companies = []
        self.__index_controller = index_controller
        self.__company_view = CompanyView()

    def open_screen(self):
        options_list = {1: self.register_company, 2: self.list_companies, 3: self.update_company, 4: self.delete_company, 0: self.back}
        while True:
            options_list[self.__company_view.main_menu()]()




    ################################################################################
    # METHODS;

    # Registrar uma compania;
    def register_company(self):
        cnpj, nome = self.__company_view.get_company_data()
        self.__companies.append(Company(cnpj, nome))
        self.__company_view.show_message("Empresa cadastrada com sucesso.")

    # Atualizar uma compania;
    def update_company(self):
        index = self.__company_view.select_company_index(self.__companies)
        if index is not None:
            cnpj, nome = self.__company_view.get_company_data()
            self.__companies[index].cnpj = cnpj
            self.__companies[index].razao_social = nome
            self.__company_view.show_message("Empresa atualizada.")

    # Listar companias;
    def list_companies(self):
        self.__company_view.show_companies(self.__companies)

    # Deletar uma compania;
    def delete_company(self):
        index = self.__company_view.select_company_index(self.__companies)
        if index is not None:
            empresa = self.__companies.pop(index)
            self.__company_view.show_message(f"{empresa.razao_social} removida com sucesso.")

    # Voltar;
    def back(self):
        self.__index_controller.initialize()