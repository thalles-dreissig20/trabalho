from models.company import Company
from models.public_agency import PublicAgency

class Invoice:
    def __init__(self, code: str, type: str, date: str, total_price: float, company: Company, public_agency: PublicAgency):
        self.__code = code
        self.__type = type
        self.__date = date
        self.__total_price = total_price
        self.__company = company
        self.__public_agency = public_agency
        self.__approved = False
        self.__taxes = []

    @property
    def code(self):
        return self.__code

    @property
    def type(self):
        return self.__type   
    
    @property
    def date(self):
        return self.__date  
    
    @property
    def total_price(self):
        return self.__total_price  
    
    @property
    def company(self):
        return self.__company
    
    @property
    def public_agency(self):
        return self.__public_agency
    
    @property
    def approved(self):
        return self.__approved
    
    @property
    def taxes(self):
        return self.__taxes

    @code.setter
    def code(self, code):
        self.__code = code

    @type.setter
    def type(self, type):
        self.__type = type

    @date.setter
    def social_reason(self, date):
        self.__date = date

    @total_price.setter
    def total_price(self, total_price):
        self.__total_price = total_price

    @company.setter
    def company(self, company):
        self.__company = company

    @public_agency.setter
    def public_agency(self, public_agency):
        self.__public_agency = public_agency

    @approved.setter
    def approved(self, approved):
        self.__approved = approved

    @taxes.setter
    def taxes(self, tax):
        self.__taxes.append(tax)