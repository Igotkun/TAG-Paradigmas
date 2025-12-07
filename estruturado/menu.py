# --------------------------
# MENU COM SWITCH (match-case)
# --------------------------

from estruturado.produtos import listarProdutos, alterarEstoque
from estruturado.carrinho import adicionarProdutoCarrinho, removerProdutoCarrinho, calcularTotalCarrinho

def menu_principal():

    while True:
        print("""
        ======== MENU ========
        1 - Listar produtos
        2 - Adicionar ao carrinho
        3 - Remover do carrinho
        4 - Calcular total
        5 - Alterar estoque
        0 - Sair
        """)

        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                listarProdutos()

            case 2:
                cod = int(input("Código: "))
                adicionarProdutoCarrinho(cod)

            case 3:
                cod = int(input("Código: "))
                removerProdutoCarrinho(cod)

            case 4:
                calcularTotalCarrinho()

            case 5:
                cod = int(input("Código: "))
                qtd = int(input("Novo estoque: "))
                alterarEstoque(cod, qtd)

            case 0:
                print("Saindo...")
                break

            case _:
                print("Opção inválida.")
