from models.public_agency import PublicAgency

class Company:
    _code = 1
    def __init__(self, cnpj: str, social_reason: str, public_agency: PublicAgency):
        if (isinstance(public_agency, PublicAgency)):
            self.__public_agency = public_agency

        self.__code = Company._code
        Company._code += 1  
        self.__cnpj = cnpj
        self.__social_reason = social_reason
        self.__invoices = []

    ################################################################################
    # METHODS;
    @property
    def code(self):
        return self.__code
    
    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def social_reason(self):
        return self.__social_reason
      
    @property
    def public_agency(self):
        return self.__public_agency
    
    @property
    def invoices(self):
        return self.__invoices

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @social_reason.setter
    def social_reason(self, social_reason):
        self.__social_reason = social_reason

    @public_agency.setter
    def public_agency(self, public_agency: PublicAgency):
        if (isinstance(public_agency, PublicAgency)):
            self.__public_agency = public_agency

    @invoices.setter
    def invoices(self, invoice):
        self.__invoices.append(invoice)