class Entity:
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
        
    ################################################################################
    # METHODS;

    def list_companies(self):
        for idx, company in enumerate(self.companies, start=1):
            print(f"{idx}. {company.social_reason} - CNPJ: {company.cnpj}")

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