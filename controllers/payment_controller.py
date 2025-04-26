from models.pagamento import Pagamento

class PaymentController:
    def __init__(self):
        self.pagamentos = []

    def criar_pagamento(self, documento_fiscal, empenho, cod_liquidacao, data_liquidacao, cod_ob):
        pagamento = Pagamento(documento_fiscal, empenho, cod_liquidacao, data_liquidacao, cod_ob)
        self.pagamentos.append(pagamento)
        return pagamento

    def listar_pagamentos(self):
        return self.pagamentos

    def aprovar_pagamento(self, pagamento, usuario):
        pagamento.aprovar(usuario)

    def homologar_pagamento(self, pagamento, usuario):
        pagamento.homologar(usuario)
