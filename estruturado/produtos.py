# Aqui ficará o estoque (persistência)
# Também aqui ficam funções estruturadas

from oo.produto import Produto
from estruturado.dados import lista_produtos

def carregar_estoque():
    
    notebook = Produto("Notebook", 3500.00, "Eletrônicos", 5)
    leite = Produto("Leite", 5.90, "Alimentos", 50)
    livro = Produto("O senhor dos Anéis", 89.90, "Livros", 15)

    lista_produtos.append(notebook)
    lista_produtos.append(leite)
    lista_produtos.append(livro)

def salvar_estoque(estoque):
    pass

def listarProdutos(lista_produtos):
    
    print("\n## CATÁLOGO DE PRODUTOS ##")
    if not lista_produtos:
        print("Nenhum produto cadastrado")
        return
    
    for i, produto in enumerate(lista_produtos):
        print(f"[{i + 1}] {produto}")

    print("-" * 30)
    

def alterarEstoque(codigo, nova_qtd):
    pass
