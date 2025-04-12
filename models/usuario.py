class Usuario:
    def __init__(self, nome: str, perfil: str):
        self.nome = nome
        self.perfil = perfil.lower()  # 'operador' ou 'homologador'

    def pode_aprovar(self):
        return self.perfil == 'homologador'

    def __str__(self):
        return f"{self.nome} ({self.perfil})"