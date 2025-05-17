class PublicAgency:
    def __init__(
        self,
        cnpj: str,
        social_reason: str,
        amount: float,
        email: str = "",
        phone: str = ""
    ):
        self.__cnpj = cnpj
        self.__social_reason = social_reason
        self.__amount = amount 
        self.__email = email
        self.__phone = phone
        self.__companies = []
        self.__invoices = []
        self.__commitments = []
        
    ################################################################################
    # METHODS;

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def social_reason(self):
        return self.__social_reason 
    
    @property
    def amount(self):
        return self.__amount 
    
    @property
    def email(self):
        return self.__email  
    
    @property
    def phone(self):
        return self.__phone  
    
    @property
    def companies(self):
        return self.__companies  
    
    @property
    def invoices(self):
        return self.__invoices
    
    @property
    def commitments(self):
        return self.__commitments

    @cnpj.setter
    def codcnpje(self, cnpj):
        self.__cnpj = cnpj

    @social_reason.setter
    def social_reason(self, social_reason):
        self.__social_reason = social_reason

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @email.setter
    def email(self, email):
        self.__email = email

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @companies.setter
    def companies(self, company):
        self.__companies.append(company)
    
    @invoices.setter
    def invoices(self, invoice):
        self.__invoices.append(invoice)

    @commitments.setter
    def commitments(self, commitment):
        self.__commitments.append(commitment)