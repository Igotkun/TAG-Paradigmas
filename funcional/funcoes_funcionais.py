from functools import reduce

def aplicar_desconto(preco, desconto_percent=10):
    return round(preco * (1 - desconto_percent / 100), 2) #aplica um desconto percentual ao preço


def processar_precos(lista_precos, func):
    return list(map(func, lista_precos)) #usa map para aplicar a função nos elementos da lista


def gerar_multiplicador(n): #multiplica um valor por n
    def multiplicador(x):
        return x * n
    return multiplicador 


def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])