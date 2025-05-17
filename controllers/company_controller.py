from models.company import Company
from views.company_view import CompanyView


class CompanyController:
    def __init__(self, index_controller):
        self.__companies = []
        self.__index_controller = index_controller
        self.__company_view = CompanyView()



    ################################################################################
    # MENU;
    def open_screen(self):
        options_list = {
            1: self.register_company, 
            2: self.list_companies, 
            3: self.update_company, 
            4: self.delete_company, 
            0: self.back
        }
        while True:
            options_list[self.__company_view.main_menu()]()


    ################################################################################
    # METHODS;

    # Obter compania;
    def get_company(self, company):
        return self.__companies[company]
    
    # Listar companias;
    def list_companies(self):
        if len(self.__companies) == 0:
            self.__company_view.show_message("Não há empresas cadastradas.")
        else:
            self.__company_view.show_companies(self.__companies)
    
    # Registrar uma compania;
    def register_company(self):
        # Get form;
        cnpj, social_reason = self.__company_view.form()
        # Set Company;
        public_agency = self.__index_controller.get_public_agency().get_public_agency()
        company = Company(cnpj, social_reason, public_agency)
        self.__companies.append(company)
        public_agency.companies = company
        
        self.__company_view.show_message("Empresa cadastrada com sucesso.")

    # Atualizar uma compania;
    def update_company(self):
        index = self.__company_view.get_company(self.__companies)
        if index is not None:
            cnpj, social_reason = self.__company_view.form()
            self.__companies[index].cnpj = cnpj
            self.__companies[index].social_reason = social_reason
            self.__company_view.show_message("Empresa atualizada.")

    # Deletar uma compania;
    def delete_company(self):
        if len(self.__companies) == 0:
            self.__company_view.show_message("Não há empresas cadastradas.")
        else:
            index = self.__company_view.get_company(self.__companies)
            if index is not None:
                company = self.__companies[index]
                public_agency = self.__index_controller.get_public_agency().get_public_agency()

                public_agency.companies.remove(company)
                self.__companies.remove(company)

    # Voltar;
    def back(self):
        self.__index_controller.initialize()