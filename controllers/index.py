from views.index import IndexView
from controllers.entity_controller import EntityController
from controllers.company_controller import CompanyController
from controllers.invoice_controller import InvoiceController

class IndexController:
    def __init__(self):
        self.__entity_controller = EntityController(self)
        self.__company_controller = CompanyController(self)
        self.__invoices_controller = InvoiceController(self)
        self.__view = IndexView()


    ################################################################################
    # MENU;

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
        return self.__entity_controller.open_screen()

    def companies(self):
        return self.__company_controller.open_screen()
    
    def invoices(self):
        return self.__invoices_controller.open_screen()
    
    def exit(self):
        exit(0)