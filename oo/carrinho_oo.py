class ItemCarrinho:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto, quantidade):
        pass

    def remover(self, produto):
        pass

    def calcular_total(self):
        pass
