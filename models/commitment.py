from models.public_agency import PublicAgency

class Commitment:
    _code = 1

    def __init__(self, descrition: str, date: str, amount: float, public_agency: PublicAgency):
        self.__code = Commitment._code
        Commitment._code += 1  
        self.__description = descrition
        self.__date = date
        self.__amount = amount
        self.__public_agency = public_agency
        self.__paid = False

    @property
    def code(self):
        return self.__code
    
    @property
    def description(self):
        return self.__description
    
    @property
    def date(self):
        return self.__date
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def public_agency(self):
        return self.__public_agency
    
    @property
    def paid(self):
        return self.__paid
    
    @code.setter
    def code(self, code):
        self.__code = code

    @description.setter
    def description(self, description):
        self.__description = description

    @date.setter
    def date(self, date):
        self.__date = date
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @public_agency.setter
    def public_agency(self, public_agency):
        self.__public_agency = public_agency

    @paid.setter
    def paid(self, paid):
        self.__paid = paid