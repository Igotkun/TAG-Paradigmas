from dados import criarCliente, lerClientes, alterarCliente
from estruturado.produtos import listarProdutos
from estruturado.carrinho import adicionarProdutoCarrinho, removerProdutoCarrinho, calcularTotalCompra, mostraCarrinho
from oo.pagamento import processarPagamento
import os


def menu_lista(lista_produtos, carrinho):
    
    while True:
        os.system('cls')
        listarProdutos(lista_produtos)
        print("\n========== CATÁLOGO ==========")
        print("[1] Adicionar Produto ao Carrinho")
        print("[0] Sair")
        print("-" * 40)
        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                adicionarProdutoCarrinho(lista_produtos, carrinho)

            case 0:
                break

            case _:
                print("Opção inválida.")
                
def menu_carrinho(carrinho):
    
    while True:
        os.system('cls')
        print("\n========== CARRINHO ==========")
        mostraCarrinho()
        print("\n[1] Remover Produto do Carrinho") 
        print("[2] Finalizar Compra")
        print("[0] Sair")
        print("-" * 40)
        total = calcularTotalCompra(carrinho)
        print(f"\nTOTAL DA COMPRA: R${total:.2f}")
        
        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                removerProdutoCarrinho(carrinho)
            
            case 2:
                processarPagamento(total, carrinho)
            case 0:
                break

            case _:
                print("Opção inválida.")

def menu_perfil():

    while True:
        os.system('cls')
        print("\n========== MEU PERFIL ==========")
        print("[1] Cadastrar Cliente")
        print("[2] Listar Clientes")
        print("[3] Alterar Cliente")
        print("[0] Sair")
        print("-" * 40)

        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                criarCliente()

            case 2:
                lerClientes()
                input("Escolha: ")

            case 3:
                alterarCliente()

            case 0:
                break

            case _:
                print("Opção inválida.")

def iniciarLoja(lista_produtos, carrinho):

    while True:
        os.system('cls')
        print("\n========== LOJA MULTI-PARADIGMA ==========")
        print("[1] Ver Catálogo")
        print("[2] Meu Carrinho")
        print("[3] Meu Perfil") 
        print("[0] Sair")
        print("-" * 40)

        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                menu_lista(lista_produtos, carrinho)

            case 2:
                menu_carrinho(carrinho)
            
            case 3:
                menu_perfil()

            case 0:
                print("Obrigado por utilizar a loja! Saindo...")
                break

            case _:
                print("Opção inválida.")