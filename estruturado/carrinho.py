# Carrinho estruturado (simples, baseado em lista)
from estruturado.produtos import listarProdutos
from estruturado.dados import carrinho
from functools import reduce

  # memória temporária

def adicionarProdutoCarrinho(lista_produtos, carrinho):
    if not lista_produtos:
        print("O catálogo de produtos está vazio.")
        return

    listarProdutos(lista_produtos) 
    
    try:
        # Pede o número do produto (índice + 1)
        indice_input = int(input("Digite o NÚMERO do produto para adicionar: "))
        quantidade = int(input("Digite a QUANTIDADE: "))
        
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros.")
        return

    indice_produto = indice_input - 1 

    if 0 <= indice_produto < len(lista_produtos) and quantidade > 0:
        produto_selecionado = lista_produtos[indice_produto]
        estoque_atual = produto_selecionado.get_estoque()

        if estoque_atual >= quantidade:
            #Adicionar item ao carrinho
            carrinho.append({'produto': produto_selecionado, 'quantidade': quantidade})
            
            #Debita o estoque
            novo_estoque = estoque_atual - quantidade
            produto_selecionado.set_estoque(novo_estoque)
            print(f"{quantidade} X {produto_selecionado.get_nome()} adicionado ao carrinho. Estoque atualizado: {novo_estoque}")
        
        else:
            print(f"Estoque insuficiente. Disponível:{estoque_atual} unidade.")
    else:
        print("Opção de produto ou quantidade inválida")
        
def removerProdutoCarrinho(codigo):
    if not carrinho:
            print("O carrinho está vazio")
            return
    
    for i, item in enumerate(carrinho):
        produto = item['produto']
        quantidade = item['quantidade']
        print(f"[{i +1}] {produto.get_nome()} |Quantidade: {quantidade}")
        print("-" * 30)

    try:
        indice_input = int(input("Digite o NÚMERO do item que deseja remover: "))
        quantidade_remover = int(input("Digite a QUANTIDADE a ser removida: "))
    
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
        return
    
    indice_item = indice_input - 1

    if 0 <= indice_item < len(carrinho) and quantidade_remover > 0:
        item_selecionado = carrinho[indice_item]
        produto_selecionado = item_selecionado['produto']
        quantidade_atual_carrinho = item_selecionado['quantidade']

        if quantidade_remover <= quantidade_atual_carrinho:
            #Devolve quantidade ao estoque
            estoque_atual = produto_selecionado.get_estoque()
            produto_selecionado.set_estoque(estoque_atual + quantidade_remover)

            if quantidade_remover == quantidade_atual_carrinho:
                carrinho.pop(indice_item)
                print(f"Item'{produto_selecionado.get_nome()}' removido completamente. Estoque recuperado.")
            else:
                item_selecionado['quantidade'] -= quantidade_remover
                print(f"{quantidade_remover} x '{produto_selecionado.get_nome()} removido. Quantidade restante no carrinho: {item_selecionado['quantidade']}")
        else:
            print(f"Quantidade a remover ({quantidade_remover}) é maior do que a quantidade no carrinho ({quantidade_atual_carrinho}).")
    else:
        print("Opção de item ou quantidade inválida")

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