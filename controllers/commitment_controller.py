
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
        c1 = Commitment("Compra de materiais", "2023-10-01", 100000.00, self.__index_controller.agency_controller().get_public_agency())
        c2 = Commitment("Pagamento de serviços", "2023-10-15", 200000.00, self.__index_controller.agency_controller().get_public_agency())
        c3 = Commitment("Compra de equipamentos", "2023-11-01", 150000.00, self.__index_controller.agency_controller().get_public_agency())
        c4 = Commitment("Pagamento de fornecedores", "2023-11-15", 500000.00, self.__index_controller.agency_controller().get_public_agency())
        for commitment in [c1, c2, c3, c4]:
            self.__commitments.append(commitment)
            self.__index_controller.agency_controller().get_public_agency().commitments = commitment



    ################################################################################
    # MENU;
    def open_screen(self):
        options_list = {
            1: self.register_commitment, 
            2: self.list_commitment, 
            3: self.update_commitment, 
            4: self.delete_commitment, 
            0: self.back
        }
        while True:
            options_list[self.__commitments_view.main_menu()]()
    
    
    ################################################################################
    # METHODS;

    # Obter compromisso;
    def get_commitment(self, commitment):
        return self.__commitments[commitment]
    
    # Listar compromissos;
    def list_commitment(self):
        if len(self.__commitments) == 0:
            self.__index_controller.get_view().show_message("Não há compromissos cadastrados.")
        else:
            self.__commitments_view.show_commitments(self.__commitments)


    # Registrar um compromisso;
    def register_commitment(self):
        # Get form;
        description, date, amount = self.__commitments_view.form()
        # Set Company;
        public_agency = self.__index_controller.agency_controller().get_public_agency()
        commitment = Commitment(description, date, amount, public_agency)
        self.__commitments.append(commitment)
        public_agency.commitments = commitment
        
        self.__index_controller.get_view().show_message("Compromisso cadastrado com sucesso.")


    # Atualizar um compromisso;
    def update_commitment(self):
        index = self.__commitments_view.get_commitment(self.__commitments)
        if index is not None:
            description, date, amount = self.__commitments_view.form()
            self.__commitments[index].description = description
            self.__commitments[index].date = date
            self.__commitments[index].amount = amount
            self.__index_controller.get_view().show_message("Compromisso atualizado com sucesso.")

    
    # Excluir um compromisso;
    def delete_commitment(self):
        if len(self.__commitments) == 0:
            self.__index_controller.get_view().show_message("Não há compromissos cadastrados.")
        else:
            index = self.__commitments_view.get_commitment(self.__commitments)
            if index is not None:
                del self.__commitments[index]
                self.__index_controller.get_view().show_message("Compromisso excluído com sucesso.")


    # Voltar;
    def back(self):
        return self.__index_controller.initialize()