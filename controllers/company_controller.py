from models.company import Company
from views.company_view import CompanyView
from DAOs.company_dao import CompanyDAO

class CompanyController:
    def __init__(self, index_controller):
        self.__companies = []
        self.__index_controller = index_controller
        self.__company_DAO = CompanyDAO()
        self.__company_view = CompanyView()



        # TODO: Temporary data;
        #c1 = Company("12.345.678/0001-95", "Empresa A", self.__index_controller.agency_controller().get_public_agency())
        #c2 = Company("98.765.432/0001-96", "Empresa B", self.__index_controller.agency_controller().get_public_agency())
        #c3 = Company("12.345.678/0001-97", "Empresa C", self.__index_controller.agency_controller().get_public_agency())
        #c4 = Company("12.345.678/0001-98", "Empresa D", self.__index_controller.agency_controller().get_public_agency())
        #for company in [c1, c2, c3, c4]:
        #    self.__companies.append(company)
        #    self.__index_controller.agency_controller().get_public_agency().companies = company



    ################################################################################
    # MENU;
    def open_screen(self):
        options_list = {
            1: self.register_company, 
            2: self.show_companies, 
            3: self.update_company, 
            4: self.delete_company, 
            0: self.back
        }
        while True:
            options_list[self.__company_view.main_menu()]()


    ################################################################################
    # METHODS;

    # Obter compania;
    def get_company(self, agency: int = None, company: int = None):
        companies = list(self.__company_DAO.get_all())

        if not companies:
            self.__index_controller.get_view().show_message("❕- Não há empresas cadastradas.")
            return None

        # Filtrar por agência?
        if agency:
            agency_obj = self.__index_controller.agency_controller().get_public_agency()
            companies = [c for c in companies if c.public_agency.code == agency_obj.code]

        # Buscar por código específico?
        if company:
            return next((c for c in companies if c.code == company), None)

        return companies

        
    # Obter lista de companias;
    def show_companies(self, agency: int = None, companies_codes: list[int] = None):
        companies = list(self.__company_DAO.get_all())  # pega todas as empresas salvas

        if not companies:
            self.__index_controller.get_view().show_message("❕- Não há empresas cadastradas.")
            return

        # Filtrar por agência?
        if agency:
            agency_obj = self.__index_controller.agency_controller().get_public_agency()
            companies = [c for c in companies if c.public_agency.code == agency_obj.code]

        # Filtrar por códigos de empresa?
        if companies_codes:
            companies = [c for c in companies if c.code in companies_codes]

        if not companies:
            self.__index_controller.get_view().show_message("❕- Nenhuma empresa encontrada com os critérios fornecidos.")
            return

        # Exibir no view
        return self.__company_view.show_companies(companies)


    # Registrar uma compania;
    def register_company(self):
        # Get form;
        cnpj, social_reason = self.__company_view.form()
        # Set Company;
        public_agency = self.__index_controller.agency_controller().get_public_agency()
        company = Company(cnpj, social_reason, public_agency)
        #self.__companies.append(company)
        self.__company_DAO.add(company)
        public_agency.companies = company
        
        self.__index_controller.get_view().show_message("✨ - Empresa cadastrada com sucesso.")


    # Atualizar uma compania;
    def update_company(self):
        companies = list(self.__company_DAO.get_all())
        self.show_companies()

        if not companies:
            self.__index_controller.get_view().show_message("❕- Não há empresas cadastradas.")
            return

        # Get company;
        code = self.__company_view.get_code(message="Código da empresa: ")
        company = next((c for c in companies if c.code == code), None)

        if company is None:
            self.__index_controller.get_view().show_message("❕- Empresa não encontrada.")
            return

        # Get form;
        cnpj, social_reason = self.__company_view.form()
        company.cnpj = cnpj
        company.social_reason = social_reason

        self.__company_DAO.update(company)

        self.__index_controller.get_view().show_message("✨ - Empresa atualizada.")

    # Deletar uma compania;
    def delete_company(self):
        companies = list(self.__company_DAO.get_all())
        self.show_companies()

        if not companies:
            self.__index_controller.get_view().show_message("❕- Não há empresas cadastradas.")
            return

        # Get company;
        code = self.__company_view.get_code(message="Código da empresa: ")
        company = next((c for c in companies if c.code == code), None)

        if company is None:
            self.__index_controller.get_view().show_message("❕- Empresa não encontrada.")
            return

        # Deletar empresa;
        self.__company_DAO.remove(code)
        self.__index_controller.get_view().show_message("✨ - Empresa excluída com sucesso.")


    def view(self):
        return self.__company_view

    # Voltar;
    def back(self):
        self.__index_controller.initialize()