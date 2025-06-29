from DAOs.dao import DAO
from models.company import Company

class CompanyDAO(DAO):
    def __init__(self):
        super().__init__('companies.pkl')

    def add(self, company: Company):
        if isinstance(company, Company):
            super().add(company.code, company)

    def update(self, company: Company):
        if isinstance(company, Company):
            super().update(company.code, company)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)