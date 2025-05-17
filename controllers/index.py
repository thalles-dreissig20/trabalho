# Views;
from views.index import IndexView

# Controllers;
from controllers.public_agency_controller import PublicAgencyController
from controllers.company_controller import CompanyController
from controllers.invoice_controller import InvoiceController
from controllers.commitment_controller import CommitmentController
from controllers.retention_controller import RetentionController

class IndexController:
    def __init__(self):
        # Views;
        self.__view = IndexView()

        # Controllers;
        self.__public_agency_controller = PublicAgencyController(self)
        self.__company_controller = CompanyController(self)
        self.__invoices_controller = InvoiceController(self)
        self.__commitment_controller = CommitmentController(self)
        self.__retention_controller = RetentionController(self)
        

    ################################################################################
    # MENU;

    def initialize(self):
        options_list = {
            1: self.public_agency,
            2: self.companies,
            3: self.invoices,
            4: self.commitments,
            5: self.retention,
            0: self.exit
        }
        while True:
            options_list[self.__view.main_menu()]()

    ################################################################################
    # METHODS;

    def public_agency(self):
        return self.__public_agency_controller.open_screen()

    def companies(self):
        return self.__company_controller.open_screen()
    
    def invoices(self):
        return self.__invoices_controller.open_screen()
    
    def commitments(self):
        return self.__commitment_controller.open_screen()
    
    def retention(self):
        return self.__retention_controller.open_screen()
    
    def agency(self):
        return self.__public_agency_controller
    
    def get_view(self):
        return self.__view

    def exit(self):
        exit(0)