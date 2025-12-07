# Carrinho estruturado (simples, baseado em lista)
from functools import reduce

carrinho = []  # memória temporária

def adicionarProdutoCarrinho(codigo):
    pass

def removerProdutoCarrinho(codigo):
    pass

def calcularTotalCompra(carrinho):
    if not carrinho:
        return 0.0

    valores_itens = map(
        lambda item: item['quantidade'] * item['produto'].calcularValorFinal(), 
        carrinho
    )

    total = reduce(
        lambda acc, valor_item: acc + valor_item,
        valores_itens
    )

    return total