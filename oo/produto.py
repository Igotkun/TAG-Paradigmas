class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def get_nome(self):
        pass

    def set_nome(self, valor):
        pass

    def get_preco(self):
        pass

    def set_preco(self, valor):
        pass

    # Método polimórfico
    def calcularValorFinal(self):
        pass


class ProdutoFisico(Produto):
    def calcularValorFinal(self):
        pass  # frete ou taxa de envio


class ProdutoDigital(Produto):
    def calcularValorFinal(self):
        pass  # desconto ou taxa digital
