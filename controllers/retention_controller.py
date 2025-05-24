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
            1: self.show_retentions, 
            2: self.update_retentions, 
            0: self.back
        }
        while True:
            options_list[self.__retention_view.main_menu()]()

    ################################################################################
    # METHODS;

    def get_retention(self, retention: int = None):
        if not self.__retentions:
            self.__index_controller.get_view().show_message("❕- Não há retenções cadastradas.")
            return []

        retentions = self.__retentions

        if retention:
            retentions = next((r for r in self.__retentions if r.code == retention), None)

        if not retentions:
            self.__index_controller.get_view().show_message("❕- Nenhuma retenção encontrada com os códigos fornecidos.")
            return []
        else:
            return retentions
        

    def show_retentions(self, retentions_codes: list[int] = None):
        if not self.__retentions:
            self.__index_controller.get_view().show_message("❕- Não há retenções cadastradas.")
            return

        retentions = self.__retentions

        if retentions_codes:
            retentions = [r for r in self.__retentions if r.code in retentions_codes]

        if not retentions:
            self.__index_controller.get_view().show_message("❕- Nenhuma retenção encontrada com os códigos fornecidos.")
            return
        else:
            self.__retention_view.show_retentions(retentions)


    # Update Retention;
    def update_retentions(self):
        self.show_retentions()
        code = self.__retention_view.get_retention()
        if code is None:
            self.__index_controller.get_view().show_message("❕- Retenção não encontrada.")
            return
        
        retention = next((i for i in self.__retentions if i.code == code), None)
        active = self.__retention_view.form()
        retention.active = active
        self.__index_controller.get_view().show_message("✨ - Retenção atualizada com sucesso.")


    def view(self):
        return self.__retention_view

    # Back;
    def back(self):
        self.__index_controller.initialize()