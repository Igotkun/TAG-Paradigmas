from functools import reduce

def aplicar_desconto(preco, desconto_percent=10):
    return round(preco * (1 - desconto_percent / 100), 2)


def processar_precos(lista_precos, func):
    return list(map(func, lista_precos))


def gerar_multiplicador(n):
    def multiplicador(x):
        return x * n
    return multiplicador


def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])


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