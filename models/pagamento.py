from models.retencao import Retencao

class Pagamento:
    def __init__(self, documento_fiscal, empenho, cod_liquidacao, data_liquidacao, cod_ob):
        self.documento_fiscal = documento_fiscal  # associação
        self.empenho = empenho  # associação
        self.retencao = Retencao("RET001", 5.0)  # composição
        self.retencao.calcular(documento_fiscal.valor_total)

        self.valor_liquido = round(documento_fiscal.valor_total - self.retencao.valor, 2)
        self.codigo_liquidacao = cod_liquidacao
        self.data_liquidacao = data_liquidacao
        self.codigo_ordem_bancaria = cod_ob

        self.aprovado = False
        self.homologado = False

    def aprovar(self, usuario):
        if usuario.pode_aprovar():
            self.aprovado = True

    def homologar(self, usuario):
        if self.aprovado and usuario.pode_aprovar():
            self.homologado = True

    def __str__(self):
        return (f"Pagamento de R$ {self.valor_liquido:.2f} (líquido) - "
                f"{self.documento_fiscal.tipo} {self.documento_fiscal.codigo}")
