# Views;
from views.invoice_view import InvoiceView
from views.company_view import CompanyView
from datetime import datetime

# Models;
from models.invoice import Invoice

class InvoiceController:
    def __init__(self, index_controller):
        self.__invoices = []
        self.__index_controller = index_controller
        self.__invoice_view = InvoiceView()

        # TODO: Temporary data;
        i1 = Invoice("NF", datetime.strptime("21-10-2025", "%d-%m-%Y").date(), 1000, self.__index_controller.company_controller().get_company(agency=1, company=1), self.__index_controller.agency_controller().get_public_agency(), [self.__index_controller.retention_controller().get_retention(2), self.__index_controller.retention_controller().get_retention(1)], self.__index_controller.commitment_controller().get_commitment(commitment=1))
        i2 = Invoice("NF", datetime.strptime("22-10-2025", "%d-%m-%Y").date(), 2000, self.__index_controller.company_controller().get_company(agency=1, company=1), self.__index_controller.agency_controller().get_public_agency(), [self.__index_controller.retention_controller().get_retention(5)], self.__index_controller.commitment_controller().get_commitment(commitment=1))
        i3 = Invoice("Fatura", datetime.strptime("23-11-2025", "%d-%m-%Y").date(), 3000, self.__index_controller.company_controller().get_company(agency=1, company=1), self.__index_controller.agency_controller().get_public_agency(), [self.__index_controller.retention_controller().get_retention(1)], self.__index_controller.commitment_controller().get_commitment(commitment=1))
        i4 = Invoice("Fatura", datetime.strptime("24-11-2025", "%d-%m-%Y").date(), 4000, self.__index_controller.company_controller().get_company(agency=1, company=1), self.__index_controller.agency_controller().get_public_agency(), [self.__index_controller.retention_controller().get_retention(6)], self.__index_controller.commitment_controller().get_commitment(commitment=1))
        for i in [i1, i2, i3, i4]:
            self.__invoices.append(i)
            self.__index_controller.agency_controller().get_public_agency().invoices.append(i)
            self.__index_controller.company_controller().get_company(1, 1).invoices.append(i)


    ################################################################################
    # MENU;
    def open_screen(self):
        options_list = {
            1: self.register_invoice,
            2: self.show_invoices,
            3: self.update_invoice,
            4: self.approve,
            5: self.delete_invoice,
            0: self.back
        }
        while True:
            options_list[self.__invoice_view.main_menu()]()

    ################################################################################
    # METHODS;

    
    # Listar invoices;
    def get_invoices(self, agency: int = None, company: int = None, commitment: int = None, code: int = None):
        if not self.__invoices:
            self.__index_controller.get_view().show_message("❕- Não há notas cadastradas.")
            return []

        invoices = self.__invoices
        # Filtrar pela agencia?
        if agency:
            agency = self.__index_controller.agency_controller().get_public_agency()
            invoices = [i for i in self.__invoices if i.public_agency.code == agency]
        
        # Filtrar pela empresa?
        if company:
            invoices = [i for i in self.__invoices if i.company.code == company]

        # Filtrar pelo compromisso?
        if commitment:
            invoices = [i for i in self.__invoices if i.commitment.code == commitment]

        # Filtrar pelos notas?
        if code:
            invoices = next((i for i in self.__invoices if i.code == code), None)

        if not invoices:
            self.__index_controller.get_view().show_message("❕- Nenhuma nota encontrada com os códigos fornecidos.")
            return []
        else:
            return invoices
        

    # Show invoices;
    def show_invoices(self, agency: int = None, company: int = None, code: int = None):
        if not self.__invoices:
            self.__index_controller.get_view().show_message("❕- Não há notas cadastradas.")
            return []

        invoices = self.__invoices
        # Filtrar pela agencia?
        if agency:
            agency = self.__index_controller.agency_controller().get_public_agency()
            invoices = [i for i in self.__invoices if i.public_agency.code == agency.code]

        # Filtrar pela empresa?
        if company:
            invoices = [i for i in self.__invoices if i.company.code == company]
        
        # Filtrar pelos notas?
        if code:
            invoices = next((i for i in self.__invoices if i.code == code), None)
        
        if not invoices:
            self.__index_controller.get_view().show_message("❕- Nenhuma nota encontrada com os códigos fornecidos.")
            return []
        else:            
            return self.__invoice_view.show_invoices(invoices)


    # Registrar uma invoice;
    def register_invoice(self):
        # Pegar agencia;
        public_agency = self.__index_controller.agency_controller().get_public_agency()

        if not public_agency.companies:
            self.__index_controller.get_view().show_message("❕- Nenhuma empresa cadastrada. Cadastre uma empresa antes.")
            return

        self.__index_controller.commitment_controller().show_commitments()
        commitment_code = self.__index_controller.commitment_controller().view().get_commitment()
        if commitment_code is None:
            return
        
        commitment = self.__index_controller.commitment_controller().get_commitment(commitment=commitment_code)
        
        # Pegar empresa;
        self.__index_controller.company_controller().show_companies()

        while True:
            company_code = self.__index_controller.company_controller().view().get_company()
            if company_code != commitment.company.code:
                self.__index_controller.get_view().show_message("❕- A empresa informada não corresponde ao compromisso selecionado. Tente novamente.")
                continue
            break

        if company_code is None:
            self.__index_controller.get_view().show_message("❕- Código inválido.")
            return

        company = self.__index_controller.company_controller().get_company(agency=public_agency.code, company=company_code)
        if company is None:
            self.__index_controller.get_view().show_message("❕- Código inválido.")
            return    
    
        # Coletar dados;
        type, date, total_price, tax = self.__invoice_view.form(commitment.amount)

        # Taxas;
        retentions = []
        if tax.upper() == "S":
            while True:
                self.__index_controller.retention_controller().show_retentions()
                retention_code = self.__index_controller.retention_controller().view().get_retention()

                retention = self.__index_controller.retention_controller().get_retention(retention=retention_code)
                retentions.append(retention)

                continue_adding = input("Deseja adicionar mais retenções? (S/N): ").strip().upper()
                if continue_adding == "N":
                    break
                elif continue_adding != "S":
                    self.__index_controller.get_view().show_message("❕- Opção inválida. Tente novamente.")


        # Registrar nota;
        invoice = Invoice(type, date, total_price, company, public_agency, retentions, commitment)
        self.__invoices.append(invoice)
        public_agency.invoices.append(invoice)
        company.invoices.append(invoice)

        self.__index_controller.get_view().show_message("✨ - Nota fiscal cadastrada com sucesso.")


    # Atualizar uma invoice;
    def update_invoice(self):
        self.show_invoices()
        invoice_code = self.__invoice_view.get_invoice()
        invoice = next((i for i in self.__invoices if i.code == invoice_code), None)

        if invoice is None:
            self.__index_controller.get_view().show_message("❕- Nota não encontrada.")
            return
        
        if invoice.approved:
            self.__index_controller.get_view().show_message("❕- Não é possível atualizar uma nota já aprovada.")
            return
        
        self.__invoice_view.update_invoice_fields(invoice)

        self.__index_controller.get_view().show_message("✨ - Nota fiscal atualizada com sucesso.")


    # Aprovar uma invoice;
    def approve(self):
        if not self.__invoices:
            self.__index_controller.get_view().show_message("❕- Nenhuma nota cadastrada para aprovar.")
            return

        pending_invoices = [inv for inv in self.__invoices if not inv.approved]

        if not pending_invoices:
            self.__index_controller.get_view().show_message("✨ - Todas as notas já foram aprovadas.")
            return

        self.__invoice_view.show_invoices(pending_invoices)

        try:
            invoice_code = self.__invoice_view.get_invoice()
            invoice_to_approve = next((i for i in pending_invoices if i.code == invoice_code), None)
            if invoice_to_approve is None:
                self.__index_controller.get_view().show_message("❕- Nota não encontrada.")
                return

        except (ValueError, IndexError):
            self.__index_controller.get_view().show_message("❕- Nota inválida.")
            return

        invoice_to_approve.approved = True
        invoice_to_approve.commitment.amount -= invoice_to_approve.total_price

        self.__index_controller.get_view().show_message(f"✨ - Nota {invoice_to_approve.code} aprovada com sucesso.")



    # Deletar uma invoice;
    def delete_invoice(self):
        self.show_invoices()
        if not self.__invoices:
            self.__index_controller.get_view().show_message("❕- Nenhuma nota cadastrada.")
            return

        invoice_code = self.__invoice_view.get_invoice()
        invoice = next((i for i in self.__invoices if i.code == invoice_code), None)

        if invoice is None:
            self.__index_controller.get_view().show_message("❕- Nota não encontrada.")
            return

        if invoice.approved:
            self.__index_controller.get_view().show_message("❕- Não é possível excluir uma nota já aprovada.")
            return

        self.__invoices.remove(invoice)
        self.__index_controller.get_view().show_message("✨ - Nota fiscal excluída com sucesso.")
        

    # Voltar;
    def back(self):
        self.__index_controller.initialize()