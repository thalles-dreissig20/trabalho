from views.invoice_view import InvoiceView
from models.invoice import Invoice


class InvoiceController:
    def __init__(self, index_controller):
        self.__invoices = []
        self.__index_controller = index_controller
        self.__invoice_view = InvoiceView()

    def open_screen(self):
        options_list = {1: self.register_invoice, 2: self.list_invoices, 3: self.update_invoice, 4: self.delete_invoice, 0: self.back}
        while True:
            options_list[self.__invoice_view.main_menu()]()



    ################################################################################
    # METHODS;

    # Registrar uma invoice;
    def register_invoice(self):
        codigo, tipo, data, valor_total, empresa = self.__invoice_view.get_invoice_data()
        invoice = Invoice(codigo, tipo, data, valor_total, empresa)
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

        invoice = self.__invoices[index]
        self.__invoice_view.update_invoice_fields(invoice)

        self.__invoice_view.show_message("Nota fiscal atualizada.")

    # Deletar uma invoice;
    def delete_invoice(self):
        index = self.__invoice_view.select_invoice_index(self.__invoices)
        if index is not None:
            removida = self.__invoices.pop(index)
            self.__invoice_view.show_message(f"Nota {removida.codigo} removida com sucesso.")


    # Voltar;
    def back(self):
        self.__index_controller.initialize()