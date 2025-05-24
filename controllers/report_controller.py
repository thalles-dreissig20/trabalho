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
            2: self.per_commitment_report,
            3: self.per_date_report, 
            0: self.back
        }
        while True:
            options_list[self.__report_view.main_menu()]()

    ################################################################################
    # METHODS;

    def general_report(self):
        agency = self.__index_controller.agency_controller().get_public_agency()
        retentions = self.__index_controller.retention_controller().get_retention()
        return self.__report_view.general_report(agency, retentions)
    

    def per_commitment_report(self):
        self.__index_controller.commitment_controller().show_commitments()
        commitment_code = self.__index_controller.commitment_controller().view().get_code(message="Código do compromisso: ")
        if not commitment_code:
            print("❕- Nenhum compromisso encontrado.")
            return
        
        commitments = self.__index_controller.commitment_controller().get_commitment(commitment=commitment_code)
        invoices = self.__index_controller.invoices_controller().get_invoices(commitment=commitment_code)
        if not invoices:
            return

        retentions = self.__index_controller.retention_controller().get_retention()
        return self.__report_view.per_commitment_report(commitments, invoices, retentions)


    def per_date_report(self):
        agency = self.__index_controller.agency_controller().get_public_agency()
        if not agency.invoices:
            print("❕- Nenhuma nota cadastrada.")
            return
        invoices = self.__index_controller.invoices_controller().get_invoices()
        retentions = self.__index_controller.retention_controller().get_retention()
        return self.__report_view.per_date_report(invoices, retentions)

    
    # Voltar;
    def back(self):
        self.__index_controller.initialize()

