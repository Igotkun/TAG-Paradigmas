from estruturado.menu import iniciarLoja
from dados import lista_produtos
from estruturado.produtos import carregar_estoque
from oo.carrinho import Carrinho

if __name__ == "__main__":
    carregar_estoque()
    # Usa a implementação do carrinho OO por padrão
    carrinho = Carrinho()
    iniciarLoja(lista_produtos, carrinho)
