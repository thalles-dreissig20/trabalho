
# Views;
from views.commitment_view import CommitmentView

# Models;
from models.commitment import Commitment

class CommitmentController:
    def __init__(self, index_controller):
        self.__commitments = []
        self.__commitments_view = CommitmentView()
        self.__index_controller = index_controller


        # TODO: Temporary data;
        #c1 = Commitment("Compra de materiais", "01-10-2025", 10000, self.__index_controller.agency_controller().get_public_agency(), self.__index_controller.company_controller().get_company(company=1))
        #c2 = Commitment("Pagamento de serviços", "02-10-2025", 200000.00, self.__index_controller.agency_controller().get_public_agency(), self.__index_controller.company_controller().get_company(company=2))
        #c3 = Commitment("Compra de equipamentos", "03-11-2025", 150000.00, self.__index_controller.agency_controller().get_public_agency(), self.__index_controller.company_controller().get_company(company=3))
        #c4 = Commitment("Pagamento de fornecedores", "04-11-2025", 500000.00, self.__index_controller.agency_controller().get_public_agency(), self.__index_controller.company_controller().get_company(company=4))
        #for commitment in [c1, c2, c3, c4]:
        #    self.__commitments.append(commitment)
        #    self.__index_controller.agency_controller().get_public_agency().commitments = commitment



    ################################################################################
    # MENU;
    def open_screen(self):
        options_list = {
            1: self.register_commitment, 
            2: self.show_commitments, 
            3: self.update_commitment, 
            4: self.delete_commitment, 
            0: self.back
        }
        while True:
            options_list[self.__commitments_view.main_menu()]()
    
    
    ################################################################################
    # METHODS;

    # Obter compromisso;
    def get_commitment(self, commitment: int = None):
        if not self.__commitments:
            self.__index_controller.get_view().show_message("❕- Não há compromissos cadastrados.")
            return None

        commitments = self.__commitments

        # Filtrar compromissos por código;
        if commitment:
            commitments = next((i for i in commitments if i.code == commitment), None)

        if not commitments:
            self.__index_controller.get_view().show_message("❕- Nenhum compromisso encontrado com os códigos fornecidos.")
            return None
        else:
            return commitments
        
    
    # Listar compromissos;
    def show_commitments(self, commitment_codes: list[int] = None):
        if not self.__commitments:
            self.__index_controller.get_view().show_message("❕- Não há compromissos cadastrados.")
            return

        commitments = self.__commitments

        # Filtrar compromissos por código;
        if commitment_codes:
            commitments = [c for c in self.__commitments if c.code in commitment_codes]

        if not commitments:
            self.__index_controller.get_view().show_message("❕- Nenhum compromisso encontrado com os códigos fornecidos.")
            return None
        else:
            return self.__commitments_view.show_commitments(commitments)


    # Registrar um compromisso;
    def register_commitment(self):
        # Get form;
        description, date, amount = self.__commitments_view.form()

        # Get public agency;
        public_agency = self.__index_controller.agency_controller().get_public_agency()

        # Get company;
        self.__index_controller.company_controller().show_companies(agency=public_agency.code)
        company_code = self.__index_controller.company_controller().view().get_code(message="Código da empresa: ")
        if company_code is None:
            self.__index_controller.get_view().show_message("❕- Nenhuma empresa encontrada.")
            return
        company = next((i for i in self.__index_controller.company_controller().get_company() if i.code == company_code), None)

        # Register commitment;
        commitment = Commitment(description, date, amount, public_agency, company)
        self.__commitments.append(commitment)
        public_agency.commitments = commitment
        
        self.__index_controller.get_view().show_message("✨ - Compromisso cadastrado com sucesso.")


    # Atualizar um compromisso;
    def update_commitment(self):
        self.show_commitments()
        index = self.__commitments_view.get_code(message="Código do compromisso: ")

        if index is not None:
            commitment = next((i for i in self.__commitments if i.code == index), None)
            if commitment is None:
                self.__index_controller.get_view().show_message("❕- Compromisso não encontrado.")
                return

            # Atualizar os dados do compromisso
            description, date, amount = self.__commitments_view.form()
            commitment.description = description
            commitment.date = date
            commitment.amount = amount

            # Atualizar empresa associada automaticamente
            public_agency = commitment.public_agency
            self.__index_controller.company_controller().show_companies(agency=public_agency.code)

            company_code = self.__index_controller.company_controller().view().get_code(message="Código da empresa: ")
            if company_code is not None:
                company = next(
                    (i for i in self.__index_controller.company_controller().get_company() if i.code == company_code),
                    None
                )
                if company:
                    commitment.company = company
                else:
                    self.__index_controller.get_view().show_message("❕- Empresa não encontrada.")
                    return
            else:
                self.__index_controller.get_view().show_message("❕- Código de empresa inválido.")
                return

            self.__index_controller.get_view().show_message("✨ - Compromisso atualizado com sucesso.")
        else:
            self.__index_controller.get_view().show_message("❕- Nenhum compromisso encontrado.")

    
    
    # Excluir um compromisso;
    def delete_commitment(self):
        self.show_commitments()
        index = self.__commitments_view.get_code(message="Código do compromisso: ")
        if index is not None:
            commitment = next((i for i in self.__commitments if i.code == index), None)
            if commitment is None:
                self.__index_controller.get_view().show_message("❕- Compromisso não encontrado.")
                return
            
            self.__commitments.remove(commitment)
            self.__index_controller.get_view().show_message("✨ - Compromisso excluído com sucesso.")
        else:
            self.__index_controller.get_view().show_message("❕- Nenhum compromisso encontrado.")


    def view(self):
        return self.__commitments_view

    # Voltar;
    def back(self):
        return self.__index_controller.initialize()