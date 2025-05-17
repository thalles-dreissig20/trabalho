from models.public_agency import PublicAgency
from views.public_agency_view import PublicAgencyView

class PublicAgencyController:
    def __init__(self, index_controller):
        self.__public_agency = PublicAgency(
            cnpj="12.345.678/0001-90", 
            social_reason="Minha Empresa LTDA", 
            amount=50000.00,
            email="contato@minhaempresa.com", 
            phone="(11) 1234-5678"
        )    

        self.__index_controller = index_controller
        self.__public_agency_view = PublicAgencyView()


    ################################################################################
    # MENU;

    def open_screen(self):
        options_list = {
            1: self.about, 
            2: self.list_companies, 
            3: self.list_invoices, 
            4: self.report,
            0: self.back
        }
        while True:
            options_list[self.__public_agency_view.main_menu()]()

    ################################################################################
    # METHODS;

    def get_public_agency(self):
        return self.__public_agency
    
    # Dados;
    def about(self):
        return self.__public_agency_view.show_public_agency(self.__public_agency)
    
    # Listar companias;
    def list_companies(self):
        return self.__public_agency_view.show_companies(self.__public_agency)
    
    # Listar notas;
    def list_invoices(self):
        return self.__public_agency_view.show_invoices(self.__public_agency)
    
    def report(self):
        return self.__public_agency_view.report(self.__public_agency)

    # Voltar;
    def back(self):
        self.__index_controller.initialize()