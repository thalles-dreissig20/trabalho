# Views;
from views.retention_view import RetentionView
# Models;
from models.retention import Retention

class RetentionController:
    def __init__(self, index_controller):
        self.__retention_view = RetentionView()
        self.__index_controller = index_controller

        # TODO: Temporary data;
        self.__retentions = [
            Retention("IRRF", 1.5),
            Retention("INSS", 11.0),
            Retention("ISS", 5.0),
            Retention("CSLL", 9.0),
            Retention("Cofins", 3.0),
            Retention("PIS", 0.65)
        ]

    ################################################################################
    # MENU;
    def open_screen(self):
        options_list = {
            1: self.list_retentions, 
            2: self.update_retentions, 
            0: self.back
        }
        while True:
            options_list[self.__retention_view.main_menu()]()

    ################################################################################
    # METHODS;

    def get_retention(self):
        return self.__retention_view.get_retention(self.__retentions)

    # List Retention;
    def list_retentions(self):
        if len(self.__retentions) == 0:
            self.__index_controller.get_view().show_message("Não há retenções cadastradas.")
        else:
            self.__retention_view.show_retentions(self.__retentions)

    # Update Retention;
    def update_retentions(self):
        index = self.__retention_view.get_retention(self.__retentions)
        if index is not None:
            retention = self.__retentions[index]
            active = self.__retention_view.form()
            retention.active = active
            self.__index_controller.get_view().show_message("Retenção atualizada com sucesso.")
        else:
            self.__index_controller.get_view().show_message("Retenção não encontrada.")

    # Back;
    def back(self):
        self.__index_controller.initialize()