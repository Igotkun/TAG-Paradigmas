from estruturado.produtos import listarProdutos
from estruturado.carrinho import adicionarProdutoCarrinho, removerProdutoCarrinho, calcularTotalCompra


def exibir_menu():
    print("\n========== LOJA MULTI-PARADIGMA ==========")
    print("[1] Listar Produtos")
    print("[2] Adicionar Produto ao Carrinho")
    print("[3] Remover Produto do Carrinho") 
    print("[4] Calcular Total da Compra")
    print("[5] Sair")
    print("-" * 40)


def iniciarLoja(lista_produtos, carrinho):

    while True:
        exibir_menu()

        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                listarProdutos(lista_produtos)
                break

            case 2:
                adicionarProdutoCarrinho(lista_produtos, carrinho)
                break

            case 3:
                removerProdutoCarrinho(carrinho)
                break

            case 4:
                total = calcularTotalCompra(carrinho)
                print(f"\nTOTAL DA COMPRA: R${total:.2f}")
                break

            case 5:
                print("Obrigado por utilizar a loja! Saindo...")
                break

            case _:
                print("Opção inválida.")
            