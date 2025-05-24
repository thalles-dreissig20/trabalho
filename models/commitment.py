# Models;
from models.public_agency import PublicAgency
from models.company import Company

class Commitment:
    _code = 1

    def __init__(self, descrition: str, date: str, amount: float, public_agency: PublicAgency, company: Company):
        self.__code = Commitment._code
        Commitment._code += 1  
        self.__description = descrition
        self.__date = date
        self.__amount = amount
        self.__public_agency = public_agency
        self.__paid = False
        self.__company = company

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
    
    @property
    def company(self):
        return self.__company

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

    @company.setter
    def company(self, company):
        self.__company = company