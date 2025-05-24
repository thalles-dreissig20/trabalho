from models.public_agency import PublicAgency
from views.public_agency_view import PublicAgencyView

class PublicAgencyController:
    def __init__(self, index_controller):
        self.__public_agency = PublicAgency(
            cnpj="12.345.678/0001-90", 
            social_reason="Empresa complicada LTDA", 
            amount=50000.00,
            email="contato@empresacomplicada.com", 
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

    # Obter agencia;
    def get_public_agency(self):
        return self.__public_agency
    
    # Dados;
    def about(self):
        values = {
            "Nome": self.__public_agency.social_reason,
            "CNPJ": self.__public_agency.cnpj,
            "Capital": f"R$ {self.__public_agency.amount:,.2f}",
            "Email": self.__public_agency.email or "N/A",
            "Telefone": self.__public_agency.phone or "N/A"
        }
        return self.__public_agency_view.show_public_agency(values)
    
    # Listar companias;
    def list_companies(self):
        agencyCode = self.__public_agency.code
        return self.__index_controller.company_controller().show_companies(agency=agencyCode)
    
    # Listar notas;
    def list_invoices(self):
        agencyCode = self.__public_agency.code
        return self.__index_controller.invoices_controller().show_invoices(agency=agencyCode)
    
    # Relatório;
    def report(self):
        return self.__index_controller.report_controller().open_screen()

    # Voltar;
    def back(self):
        self.__index_controller.initialize()