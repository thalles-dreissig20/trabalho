# Views;
from views.report_view import ReportView

class ReportController:
    def __init__(self, index_controller):
        self.__index_controller = index_controller
        self.__report_view = ReportView()



    ################################################################################
    # MENU;
    def open_screen(self):
        options_list = {
            1: self.general_report, 
            2: self.per_company_report, 
            3: self.per_invoice_report,
            4: self.per_commitment_report,
            5: self.per_date_report, 
            0: self.back
        }
        while True:
            options_list[self.__report_view.main_menu()]()

    ################################################################################
    # METHODS;

    def general_report(self):
        agency = self.__index_controller.agency_controller().get_public_agency()
        return self.__report_view.general_report(agency)
    
    def per_company_report(self):
        agency = self.__index_controller.agency_controller().get_public_agency()
        if not agency.companies:
            print("Nenhuma companhia cadastrada.")
            return
        
        company = self.__index_controller.company_controller().get_company(agency_code=agency.code)
        print(company.code)
        invoices = self.__index_controller.invoices_controller().get_invoices(company=company.code)
        return self.__report_view.per_company_report(company, invoices)
    
    
    def per_invoice_report(self):
        return self.__report_view.per_invoice_report()
    
    def per_commitment_report(self):
        return self.__report_view.per_commitment_report()
    
    def per_date_report(self):
        agency = self.__index_controller.agency_controller().get_public_agency()
        if not agency.invoices:
            print("Nenhuma nota cadastrada.")
            return
        invoices = self.__index_controller.invoices_controller().get_invoices()
        return self.__report_view.per_date_report(invoices)

    
    # Voltar;
    def back(self):
        self.__index_controller.initialize()

