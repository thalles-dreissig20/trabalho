from models.entity import Entity

class Company:
    def __init__(self, cnpj: str, social_reason: str, entity: Entity):
        if (isinstance(entity, Entity)):
            self.__entity = entity
        self.__cnpj = cnpj
        self.__social_reason = social_reason
        self.__invoices = []

    ################################################################################
    # METHODS;
    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def social_reason(self):
        return self.__social_reason
      
    @property
    def entity(self):
        return self.__entity
    
    @property
    def invoice(self):
        return self.__invoices

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @social_reason.setter
    def social_reason(self, social_reason):
        self.__social_reason = social_reason

    @entity.setter
    def entity(self, entity: Entity):
        if (isinstance(entity, Entity)):
            self.__entity = entity

    @invoice.setter
    def invoice(self, invoice):
        self.__invoices.append(invoice)