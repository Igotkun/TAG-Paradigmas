from estruturado.menu import iniciarLoja
from dados import lista_produtos, carrinho
from estruturado.produtos import carregar_estoque

if __name__ == "__main__":
    carregar_estoque()
    iniciarLoja(lista_produtos, carrinho)
