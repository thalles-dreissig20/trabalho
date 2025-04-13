class Empresa:
    def __init__(self, cnpj: str, razao_social: str):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.documentos = []  # agregação

    def adicionar_documento(self, documento):
        self.documentos.append(documento)

    def __str__(self):
        return f"{self.razao_social} - CNPJ: {self.cnpj}"