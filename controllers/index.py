from views.index import IndexView
from controllers.company_controller import CompanyController
from controllers.invoice_controller import InvoiceController
from models.entity import Entity

class IndexController:
    def __init__(self):
        self.__entity = Entity(
            cnpj="12.345.678/0001-90", 
            social_reason="Minha Empresa LTDA", 
            amount=50000.00,
            email="contato@minhaempresa.com", 
            phone="(11) 1234-5678"
        )

        self.__company_controller = CompanyController(self, self.__entity)
        self.__invoices_controller = InvoiceController(self, self.__entity)
        self.__view = IndexView()

    def initialize(self):
        options_list = {
            1: self.entity,
            2: self.companies,
            3: self.invoices,
            0: self.exit
        }
        while True:
            options_list[self.__view.main_menu()]()




    ################################################################################
    # METHODS;

    

    def entity(self):
        print(self.__entity)

    def companies(self):
        return self.__company_controller.open_screen()
    
    def invoices(self):
        return self.__invoices_controller.open_screen()
    
    def exit(self):
        exit(0)