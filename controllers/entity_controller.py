from models.entity import Entity
from views.entity_view import EntityView

class EntityController:
    def __init__(self, index_controller):
        self.__entity = Entity(
            cnpj="12.345.678/0001-90", 
            social_reason="Minha Empresa LTDA", 
            amount=50000.00,
            email="contato@minhaempresa.com", 
            phone="(11) 1234-5678"
        )
        self.__index_controller = index_controller
        self.__entity_view = EntityView()


    ################################################################################
    # METHODS;

    def open_screen(self):
        options_list = {
            1: self.about, 
            2: self.list_companies, 
            3: self.list_invoices, 
            0: self.back
        }
        while True:
            options_list[self.__entity_view.main_menu()]()


    def get_entity(self):
        return self.__entity
    
    # Dados;
    def about(self):
        return self.__entity_view.show_entity(self.__entity)
    
    # Listar companias;
    def list_companies(self):
        return self.__entity_view.show_companies(self.__entity)
    
    # Listar notas;
    def list_invoices(self):
        return self.__entity_view.show_invoices(self.__entity)

    # Voltar;
    def back(self):
        self.__index_controller.initialize()