from dados import criarCliente, lerClientes, alterarCliente, selecionar_cliente
from estruturado.produtos import listarProdutos
from estruturado.carrinho import adicionarProdutoCarrinho, removerProdutoCarrinho, calcularTotalCompra, mostraCarrinho
from oo.pagamento import processarPagamento
import os

# TRECHO ESTRUTURADO: menus e fluxos procedurais. Aqui usamos `match` (equivalente a switch)


def menu_lista(lista_produtos, carrinho):
    
    while True:
        os.system('cls')
        print("\n========== CATÁLOGO ==========")
        listarProdutos(lista_produtos)
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
                
def menu_carrinho(carrinho, cliente):
    
    while True:
        os.system('cls')
        print("\n========== CARRINHO ==========")
        mostraCarrinho(carrinho)
        print("\n[1] Remover Produto do Carrinho") 
        print("[2] Finalizar Compra")
        print("[0] Voltar")
        print("-" * 40)
        total = calcularTotalCompra(carrinho)
        print(f"\nTOTAL DA COMPRA: R${total:.2f}")
        
        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                removerProdutoCarrinho(carrinho)
            
            case 2:
                if cliente is None:
                    print("Selecione um cliente em 'Meu Perfil' antes de finalizar a compra.")
                    input("Pressione Enter para continuar...")
                else:
                    processarPagamento(total, carrinho, cliente)
            case 0:
                break

            case _:
                print("Opção inválida.")

def menu_perfil(cliente_atual):

    while True:
        os.system('cls')
        print("\n========== MEU PERFIL ==========")
        if cliente_atual:
            print(f"Cliente Ativo: {cliente_atual.nome} (CPF: {cliente_atual.cpf})")
            print("[1] Trocar Cliente")
            print("[2] Listar Clientes")
            print("[3] Criar Novo Cliente")
            print("[4] Alterar Dados do Cliente")
        else:
            print("Nenhum cliente selecionado")
            print("[1] Selecionar Cliente")
            print("[2] Listar Clientes")
            print("[3] Criar Novo Cliente")
        print("[0] Sair")
        print("-" * 40)

        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                return selecionar_cliente()
            case 2:
                lerClientes()
                input("Pressione Enter para continuar...")
            case 3 | 4:
                if opcao == 3:
                    criarCliente()
                else:
                    alterarCliente()
            case 0:
                break
            case _:
                print("Opção inválida.")
    
    return cliente_atual


def iniciarLoja(lista_produtos, carrinho):

    cliente_atual = None  # TRECHO OO: Rastreia cliente selecionado para Pedido
    
    while True:
        os.system('cls')
        print("\n========== LOJA MULTI-PARADIGMA ==========")
        if cliente_atual:
            print(f"✓ Cliente: {cliente_atual.nome}")
        else:
            print("⊘ Nenhum cliente selecionado")
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
                menu_carrinho(carrinho, cliente_atual)
            
            case 3:
                cliente_atual = menu_perfil(cliente_atual)

            case 0:
                print("Obrigado por utilizar a loja! Saindo...")
                break

            case _:
                print("Opção inválida.")