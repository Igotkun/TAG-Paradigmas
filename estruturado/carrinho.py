# Carrinho estruturado (simples, baseado em lista)
from funcional.funcoes_funcionais import confirma
from dados import carrinho
from functools import reduce
import os

  # memória temporária
def mostraCarrinho():
    if not carrinho:
            print("O carrinho está vazio")
            return
    
    for i, item in enumerate(carrinho):
        produto = item['produto']
        quantidade = item['quantidade']
        print( f"{produto.get_nome()} | Quantidade: {quantidade}x")
        print("-" * 30)

def adicionarProdutoCarrinho(lista_produtos, carrinho):
    if not lista_produtos:
        print("O catálogo de produtos está vazio.")
        return
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
        
        os.system("cls")
        print("Adicionar " f"{quantidade}x {produto_selecionado.get_nome()} no Carrinho?")
        if confirma() == 0:
            return

        if estoque_atual >= quantidade:
            #Adicionar item ao carrinho
            carrinho.append({'produto': produto_selecionado, 'quantidade': quantidade})
            
            #Debita o estoque
            novo_estoque = estoque_atual - quantidade
            produto_selecionado.set_estoque(novo_estoque)
            print(f"{quantidade}x {produto_selecionado.get_nome()} adicionado ao carrinho. Estoque atualizado: {novo_estoque}")
            input("Aperte Enter para voltar")
        
        else:
            print(f"Estoque insuficiente. Disponível:{estoque_atual} unidade.")
            input("Aperte Enter para voltar")
    else:
        print("Opção de produto ou quantidade inválida")
        input("Aperte Enter para voltar")
        
def removerProdutoCarrinho(codigo):
    mostraCarrinho()
    if not carrinho:
            return
    try:
        indice_input = int(input("Digite o NÚMERO do item que deseja remover: "))
        quantidade_remover = int(input("Digite a QUANTIDADE a ser removida: "))
    
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
        input("Aperte Enter para voltar")
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
                input("Aperte Enter para voltar")
        else:
            print(f"Quantidade a remover ({quantidade_remover}) é maior do que a quantidade no carrinho ({quantidade_atual_carrinho}).")
            input("Aperte Enter para voltar")
    else:
        print("Opção de item ou quantidade inválida")
        input("Aperte Enter para voltar")

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

