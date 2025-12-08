from dados import criarCliente, lerClientes, alterarCliente, selecionar_cliente
from estruturado.produtos import listarProdutos
from oo.pagamento import processarPagamento
import os

def menu_lista(lista_produtos, carrinho): #Adicionar produtos ao carrinho
    
    while True:
        os.system('cls')
        print("\n========== CATÁLOGO ==========")
        listarProdutos(lista_produtos)
        print("[1] Adicionar Produto ao Carrinho")
        print("[0] Sair")
        print("-" * 40)
        opcao_raw = input("Escolha: ")
        try:
            opcao = int(opcao_raw)
        except ValueError:
            print("Entrada inválida. Digite um número.")
            input("Pressione Enter para continuar...")
            continue

        match opcao:
            case 1:
                carrinho.adicionarProdutoCarrinho(lista_produtos) #usa a função adicionarProdutoCarrinho da classe Carrinho
            case 0:
                break
            case _:
                print("Opção inválida.")
                input("Pressione Enter para continuar...")
                
def menu_carrinho(carrinho, cliente): #Remover produtos do carrinho e finalizar compra
    
    while True:
        os.system('cls')
        print("\n========== CARRINHO ==========")
        carrinho.mostraCarrinho()
        print("\n[1] Remover Produto do Carrinho") 
        print("[2] Finalizar Compra")
        print("[0] Voltar")
        print("-" * 40)
        total = carrinho.calcularTotalCompra()
        print(f"\nTOTAL DA COMPRA: R${total:.2f}")
        
        opcao_raw = input("Escolha: ")
        try:
            opcao = int(opcao_raw)
        except ValueError:
            print("Entrada inválida. Digite um número.")
            input("Pressione Enter para continuar...")
            continue

        match opcao:
            case 1:
                carrinho.removerProdutoCarrinho() #usa a função removerProdutoCarrinho da classe Carrinho
            case 2:
                if cliente is None:
                    print("Selecione um cliente em 'Meu Perfil' antes de finalizar a compra.")
                    input("Pressione Enter para continuar...")
                else:
                    processarPagamento(total, carrinho, cliente) #usa a função processarPagamento do arquivo pagamento.py
            case 0:
                break
            case _:
                print("Opção inválida.")
                input("Pressione Enter para continuar...")

def menu_perfil(cliente_atual): #Trocar cliente, criar novo cliente, alterar dados do cliente

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

        opcao_raw = input("Escolha: ")
        try:
            opcao = int(opcao_raw)
        except ValueError:
            print("Entrada inválida. Digite um número.")
            input("Pressione Enter para continuar...")
            continue

        match opcao:
            case 1:
                return selecionar_cliente() #seleciona o cliente e retorna o objeto cliente
            case 2:
                lerClientes() #Lê e mostra os clientes do arquivo JSON
                input("Pressione Enter para continuar...")
            case 3 | 4:
                if opcao == 3:
                    criarCliente() #Cria um novo cliente e salva no arquivo JSON
                else:
                    alterarCliente() #Altera os dados do cliente no arquivo JSON
            case 0:
                break
            case _:
                print("Opção inválida.")
                input("Pressione Enter para continuar...")
    
    return cliente_atual

def iniciarLoja(lista_produtos, carrinho): #Função inicial do programa que dá acesso as outras funções

    cliente_atual = None
    
    while True:
        os.system('cls')
        print("\n========== LOJA MULTI-PARADIGMA ==========") #Menu principal
        if cliente_atual:
            print(f"✓ Cliente: {cliente_atual.nome}")
        else:
            print("⊘ Nenhum cliente selecionado")
            
        print("[1] Ver Catálogo")
        print("[2] Meu Carrinho")
        print("[3] Meu Perfil") 
        print("[0] Sair do Programa")
        print("-" * 40)

        opcao_raw = input("Escolha: ")
        try:
            opcao = int(opcao_raw)
        except ValueError:
            print("Entrada inválida. Digite um número.")
            input("Pressione Enter para continuar...")
            continue

        match opcao: #Switch para as opções do menu (match nesse caso)
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
                input("Pressione Enter para continuar...")