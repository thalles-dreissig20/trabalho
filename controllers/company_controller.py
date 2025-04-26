from models.company import Company
from models.entity import Entity
from views.company_view import CompanyView


class CompanyController:
    def __init__(self, index_controller, entity: Entity):
        self.__entity = entity
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
        cnpj, social_reason = self.__company_view.get_company_data()
        self.__entity.add_company(Company(cnpj, social_reason))
        self.__company_view.show_message("Empresa cadastrada com sucesso.")

    # Atualizar uma compania;
    def update_company(self):
        index = self.__company_view.select_company_index(self.__index_controller.get_entity().companies)
        if index is not None:
            cnpj, social_reason = self.__company_view.get_company_data()
            self.__index_controller.get_entity().companies[index].cnpj = cnpj
            self.__index_controller.get_entity().companies[index].social_reason = social_reason
            self.__company_view.show_message("Empresa atualizada.")

    # Listar companias;
    def list_companies(self):
        self.__company_view.show_companies(self.__index_controller.get_entity().companies)

    # Deletar uma compania;
    def delete_company(self):
        index = self.__company_view.select_company_index(self.__index_controller.get_entity().companies)
        if index is not None:
            company = self.__index_controller.get_entity().companies.pop(index)
            self.__company_view.show_message(f"{company.social_reason} removida com sucesso.")

    def get_companies(self):
        return self.__index_controller.get_entity().companies

    # Voltar;
    def back(self):
        print(self.__entity.list_companies())
        print(self.__entity)
        self.__index_controller.initialize()