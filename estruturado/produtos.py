from oo.produto import Produto
from dados import lista_produtos
import json
import os

ARQUIVO_ESTOQUE = 'estoque.json'


def carregar_estoque():
    lista_produtos.clear()

    if os.path.exists(ARQUIVO_ESTOQUE):
        try:
            with open(ARQUIVO_ESTOQUE, 'r', encoding='utf-8') as f:
                items = json.load(f)
            for it in items:
                    cat = it.get('categoria', '')
                    nome = it.get('nome')
                    preco = float(it.get('preco', 0))
                    estoque = int(it.get('estoque', 0))

                    if cat == 'Eletrônicos':
                        try:
                            from oo.produto import Notebook
                            p = Notebook(nome, preco, estoque)
                        except Exception:
                            p = Produto(nome, preco, cat, estoque)
                    elif cat == 'Alimentos':
                        try:
                            from oo.produto import Alimento
                            p = Alimento(nome, preco, estoque)
                        except Exception:
                            p = Produto(nome, preco, cat, estoque)
                    elif cat == 'Livros':
                        try:
                            from oo.produto import Livro
                            p = Livro(nome, preco, estoque)
                        except Exception:
                            p = Produto(nome, preco, cat, estoque)
                    else:
                        p = Produto(nome, preco, cat, estoque)

                    lista_produtos.append(p)
            return
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            pass

    from oo.produto import Notebook, Alimento, Livro

    notebook = Notebook("Notebook", 3500.00, 5)
    leite = Alimento("Leite", 5.90, 50)
    livro = Livro("O senhor dos Anéis", 89.90, 15)

    lista_produtos.append(notebook)
    lista_produtos.append(leite)
    lista_produtos.append(livro)
    salvar_estoque(lista_produtos)

def salvar_estoque(estoque):
    data = []
    for p in estoque:
        data.append({
            'nome': p.get_nome(),
            'preco': p.get_preco(),
            'categoria': p.get_categoria(),
            'estoque': p.get_estoque()
        })
    with open(ARQUIVO_ESTOQUE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def listarProdutos(lista_produtos):
    if not lista_produtos:
        print("Nenhum produto cadastrado")
        return
    
    for i, produto in enumerate(lista_produtos):
        nome = produto.get_nome()
        preco = produto.get_preco()
        categoria = produto.get_categoria()
        estoque = produto.get_estoque()
        print(f"[{i + 1}] {categoria} | {nome} | Preço: R${preco:.2f} | Estoque: {estoque}")

    print("-" * 30)
    

def alterarEstoque(codigo, nova_qtd):
    try:
        indice = int(codigo) - 1
        if 0 <= indice < len(lista_produtos):
            lista_produtos[indice].set_estoque(int(nova_qtd))
            return True
    except Exception:
        return False
    return False
