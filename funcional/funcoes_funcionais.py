from functools import reduce

# TRECHO FUNCIONAL
# Função pura: aplica um desconto percentual e retorna novo preço (sem efeitos colaterais)
def aplicar_desconto(preco, desconto_percent=10):
    """Retorna o preço com desconto aplicado (valor arredondado)."""
    return round(preco * (1 - desconto_percent / 100), 2)


# Função de ordem superior (recebe outra função)
def processar_precos(lista_precos, func):
    """Aplica `func` a cada preço em `lista_precos` e retorna nova lista (imutável)."""
    return list(map(func, lista_precos))


# Função que retorna outra função
def gerar_multiplicador(n):
    """Retorna uma função que multiplica seu argumento por `n`."""
    def multiplicador(x):
        return x * n
    return multiplicador


# Recursão
def soma_recursiva(lista):
    """Soma os valores de uma lista recursivamente."""
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])


# Uso de map, filter e reduce
def exemplo_map_filter_reduce(produtos):
    """Exemplo real usando map, filter e reduce sobre uma lista de objetos Produto.

    - map: transforma cada produto para um dicionário enxuto
    - filter: filtra apenas produtos com estoque > 0
    - reduce: soma o preço dos produtos disponíveis
    Retorna um dicionário com as listas transformadas e o total.
    """
    # transforma para formato legível/serializável
    lista_simples = list(map(lambda p: {
        'nome': p.get_nome(),
        'preco': p.get_preco(),
        'categoria': p.get_categoria(),
        'estoque': p.get_estoque()
    }, produtos))

    # filtra apenas disponíveis
    disponiveis = list(filter(lambda p: p['estoque'] > 0, lista_simples))

    # reduz para o total de preços dos disponíveis
    total = reduce(lambda acc, item: acc + item['preco'], disponiveis, 0.0)

    return {'simples': lista_simples, 'disponiveis': disponiveis, 'total': total}


def confirma():
    while True:
        print("[1] Confirmar")
        print("[0] Voltar")
        print("-" * 40)
        opcao = int(input("Escolha: "))
        match opcao:
            case 1:
                return 1
                
            case 0:
                return 0

            case _:
                print("Opção inválida.")