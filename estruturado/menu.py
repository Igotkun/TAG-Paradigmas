from estruturado.produtos import listarProdutos
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
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case 0:
                print("Saindo...")
                break

            case _:
                print("Opção inválida.")
