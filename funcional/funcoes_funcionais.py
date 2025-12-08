from functools import reduce

# Função pura
def aplicar_desconto(preco):
    pass

# Função de ordem superior (recebe outra função)
def processar_precos(lista_precos, func):
    pass

# Função que retorna outra função
def gerar_multiplicador(n):
    pass

# Recursão
def soma_recursiva(lista):
    pass

# Uso de map, filter e reduce
def exemplo_map_filter_reduce(produtos):
    pass

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