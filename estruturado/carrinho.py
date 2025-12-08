# TRECHO ESTRUTURADO: funções procedurais para operações de carrinho OO
from funcional.funcoes_funcionais import confirma
from estruturado.produtos import listarProdutos
from functools import reduce
import os


def mostraCarrinho(carrinho):
    """Exibe os itens do carrinho OO."""
    if not carrinho or len(carrinho) == 0:
        print("O carrinho está vazio")
        return
    
    print("\n========== ITENS DO CARRINHO ==========")
    for i, item in enumerate(carrinho.itens, 1):
        produto = item.produto
        quantidade = item.quantidade
        print(f"[{i}] {produto.nome} | Quantidade: {quantidade}x | R${produto.preco:.2f}")
    print("-" * 40)


def adicionarProdutoCarrinho(lista_produtos, carrinho):
    """Adiciona produto ao carrinho OO."""
    if not lista_produtos:
        print("O catálogo de produtos está vazio.")
        return
    try:
        indice_input = int(input("Digite o NÚMERO do produto para adicionar: "))
        quantidade = int(input("Digite a QUANTIDADE: "))
        
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros.")
        return
    
    indice_produto = indice_input - 1 

    if 0 <= indice_produto < len(lista_produtos) and quantidade > 0:
        produto_selecionado = lista_produtos[indice_produto]
        estoque_atual = produto_selecionado.get_estoque()
        
        os.system('cls')
        print(f"Adicionar {quantidade}x {produto_selecionado.get_nome()} no Carrinho?")
        if confirma() == 0:
            return

        if estoque_atual >= quantidade:
            # Adiciona ao carrinho usando método OO
            carrinho.adicionar(produto_selecionado, quantidade)
            print(f"{quantidade}x {produto_selecionado.get_nome()} adicionado ao carrinho.")
            input("Aperte Enter para voltar")
        else:
            print(f"Estoque insuficiente. Disponível: {estoque_atual} unidade(s).")
            input("Aperte Enter para voltar")
    else:
        print("Opção de produto ou quantidade inválida")
        input("Aperte Enter para voltar")


def removerProdutoCarrinho(carrinho):
    """Remove produto do carrinho OO."""
    mostraCarrinho(carrinho)
    if not carrinho or len(carrinho) == 0:
        input("Aperte Enter para voltar")
        return
    
    try:
        indice_input = int(input("Digite o NÚMERO do item que deseja remover: "))
        quantidade_remover = int(input("Digite a QUANTIDADE a ser removida: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
        input("Aperte Enter para voltar")
        return
    
    indice_item = indice_input - 1

    if 0 <= indice_item < len(carrinho.itens) and quantidade_remover > 0:
        item_selecionado = carrinho.itens[indice_item]
        produto_selecionado = item_selecionado.produto
        quantidade_atual = item_selecionado.quantidade

        if quantidade_remover <= quantidade_atual:
            estoque_atual = produto_selecionado.get_estoque()
            produto_selecionado.set_estoque(estoque_atual + quantidade_remover)

            if quantidade_remover == quantidade_atual:
                carrinho.itens.pop(indice_item)
                print(f"Item removido completamente.")
            else:
                item_selecionado.quantidade -= quantidade_remover
                print(f"{quantidade_remover}x removido. Restante: {item_selecionado.quantidade}")
            input("Aperte Enter para voltar")
        else:
            print(f"Quantidade inválida.")
            input("Aperte Enter para voltar")
    else:
        print("Opção inválida")
        input("Aperte Enter para voltar")


def calcularTotalCompra(carrinho):
    """Calcula total do carrinho usando TRECHO FUNCIONAL (map/reduce)."""
    if not carrinho or len(carrinho) == 0:
        return 0.0

    # TRECHO FUNCIONAL: map + reduce
    valores_itens = map(
        lambda item: item.quantidade * item.produto.calcularValorFinal(),
        carrinho.itens
    )

    total = reduce(
        lambda acc, valor: acc + valor,
        valores_itens,
        0.0
    )

    return total