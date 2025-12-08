"""TRECHO OO: implementação do carrinho usando encapsulamento e polimorfismo."""


class ItemCarrinho:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Carrinho:
    def __init__(self):
        self.itens = []
    
    def adicionar(self, produto, quantidade):
        """Adiciona `quantidade` do `produto` ao carrinho, atualiza estoque.

        Lança ValueError se estoque for insuficiente.
        """
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")

        if produto.get_estoque() < quantidade:
            raise ValueError("Estoque insuficiente")

        # procura item existente
        for item in self.itens:
            if item.produto.get_nome() == produto.get_nome():
                item.quantidade += quantidade
                produto.set_estoque(produto.get_estoque() - quantidade)
                return

        # novo item
        self.itens.append(ItemCarrinho(produto, quantidade))
        produto.set_estoque(produto.get_estoque() - quantidade)

    def remover(self, produto, quantidade=None):
        """Remove um produto do carrinho. Se `quantidade` for None remove totalmente; caso contrário reduz quantidade."""
        for i, item in enumerate(self.itens):
            if item.produto.get_nome() == produto.get_nome():
                if quantidade is None or quantidade >= item.quantidade:
                    # devolve todo o estoque
                    produto.set_estoque(produto.get_estoque() + item.quantidade)
                    self.itens.pop(i)
                else:
                    item.quantidade -= quantidade
                    produto.set_estoque(produto.get_estoque() + quantidade)
                return True
        return False

    def calcular_total(self):
        """Calcula o total usando os métodos da classe Produto (polimorfismo)."""
        total = 0.0
        for item in self.itens:
            total += item.quantidade * item.produto.calcularValorFinal()
        return total

    def clear(self):
        """Limpa os itens do carrinho (compatibilidade com lista: clear())."""
        self.itens.clear()

    def __len__(self):
        return len(self.itens)

    def __iter__(self):
        return iter(self.itens)
