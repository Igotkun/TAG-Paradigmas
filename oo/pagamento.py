class Pagamento:
    def processarPagamento(self, valor):
        pass  # método polimórfico


class PagamentoCartao(Pagamento):
    def processarPagamento(self, valor):
        pass


class PagamentoPix(Pagamento):
    def processarPagamento(self, valor):
        pass


class PagamentoBoleto(Pagamento):
    def processarPagamento(self, valor):
        pass
