from views.index import IndexView
from controllers.company_controller import CompanyController
from controllers.payment_controller import PaymentController
from controllers.invoice_controller import InvoiceController

class IndexController:
    def __init__(self):
        self.__company_controller = CompanyController(self)
        self.__invoices_controller = InvoiceController(self)
        self.pagamento_controller = PaymentController()
        self.__view = IndexView()

    def initialize(self):
        options_list = {
            1: self.companies,
            2: self.invoices,
            0: self.exit
        }
        
        while True:
            option = self.__view.main_menu()
            selected = options_list[option]
            selected()




    def companies(self):
        return self.__company_controller.open_screen()
    
    def invoices(self):
        return self.__invoices_controller.open_screen()

    def exit(self):
        exit(0)