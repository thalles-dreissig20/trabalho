from views.invoice_view import InvoiceView
from views.company_view import CompanyView
from models.invoice import Invoice
from models.entity import Entity


class InvoiceController:
    def __init__(self, index_controller, entity: Entity):
        self.__invoices = []
        self.__entity = entity
        self.__index_controller = index_controller
        self.__invoice_view = InvoiceView()
        self.__company_view = CompanyView()

    def open_screen(self):
        options_list = {1: self.register_invoice, 2: self.list_invoices, 3: self.update_invoice, 4: self.approve, 5: self.delete_invoice, 0: self.back}
        while True:
            options_list[self.__invoice_view.main_menu()]()



    ################################################################################
    # METHODS;

    # Registrar uma invoice;
    def register_invoice(self):
        companies = self.__entity.get_companies()

        if not companies:
            self.__company_view.show_message("Nenhuma empresa cadastrada. Cadastre uma empresa antes.")
            return

        # Listar empresas para o usuário escolher
        self.__company_view.show_companies(companies)

        try:
            index = int(input("Escolha o número da empresa: "))
            company = companies[index]
        except (ValueError, IndexError):
            self.__company_view.show_message("Empresa inválida.")
            return

        # Coletar os outros dados da nota
        code, type, date, total_price = self.__invoice_view.get_invoice_data()
        
        invoice = Invoice(code, type, date, total_price, company)
        self.__invoices.append(invoice)
        self.__invoice_view.show_message("Nota fiscal cadastrada com sucesso.")


    # Listar invoices;
    def list_invoices(self):
        if not self.__invoices:
            self.__invoice_view.show_message("Nenhuma nota cadastrada.")
        else:
            self.__invoice_view.show_invoices(self.__invoices)

    # Atualizar uma invoice;
    def update_invoice(self):
        index = self.__invoice_view.select_invoice_index(self.__invoices)
        if index is None:
            return
        
        # Validação se já foi aprovada;
        invoice = self.__invoices[index]
        if invoice.approved:
            self.__invoice_view.show_message("Não é possível atualizar uma nota já aprovada.")
            return

        self.__invoice_view.update_invoice_fields(invoice)
        self.__invoice_view.show_message("Nota fiscal atualizada.")

    # Aprovar uma invoice;
    def approve(self):
        if not self.__invoices:
            self.__invoice_view.show_message("Nenhuma nota cadastrada para aprovar.")
            return

        pending_invoices = [inv for inv in self.__invoices if not inv.approved]

        if not pending_invoices:
            self.__invoice_view.show_message("Todas as notas já foram aprovadas.")
            return

        self.__invoice_view.show_invoices(pending_invoices)

        try:
            index = int(input("Escolha o número da nota para aprovar: "))
            invoice_to_approve = pending_invoices[index]
        except (ValueError, IndexError):
            self.__invoice_view.show_message("Nota inválida.")
            return

        invoice_to_approve.approved = True
        self.__invoice_view.show_message(f"Nota {invoice_to_approve.code} aprovada com sucesso.")


    # Deletar uma invoice;
    def delete_invoice(self):
        index = self.__invoice_view.select_invoice_index(self.__invoices)
        if index is None:
            return

        # Validação se já foi aprovada;
        invoice = self.__invoices[index]
        if invoice.approved:
            self.__invoice_view.show_message("Não é possível deletar uma nota já aprovada.")
            return

        target = self.__invoices.pop(index)
        self.__invoice_view.show_message(f"Nota {target.code} removida com sucesso.")


    # Voltar;
    def back(self):
        self.__index_controller.initialize()