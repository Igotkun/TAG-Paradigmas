from abc import ABC, abstractmethod
import os

class Pagamento(ABC):
    def __init__(self, valor_total):
        self.valor_total = valor_total

    @abstractmethod
    def processar_pagamento(self):
        pass


class PagamentoCartao(Pagamento):
    def __init__(self, valor_total):
        super().__init__(valor_total)

    def processar_pagamento(self):
        print("\n=== PAGAMENTO NO CARTÃO ===")
        numero = input("Digite o número do cartão: ")
        nome = input("Nome do titular: ")
        cvv = input("CVV: ")
        print("Processando pagamento no cartão...")
        print("Pagamento aprovado!")
        return True


class PagamentoPix(Pagamento):
    def __init__(self, valor_total):
        super().__init__(valor_total)

    def processar_pagamento(self):
        print("\n=== PAGAMENTO VIA PIX ===")
        chave = input("Digite sua chave PIX: ")
        print("Gerando QR Code...")
        print("Pagamento confirmado!")
        return True


class PagamentoBoleto(Pagamento):
    def __init__(self, valor_total):
        super().__init__(valor_total)

    def processar_pagamento(self):
        print("\n=== PAGAMENTO VIA BOLETO ===")
        print("Gerando código de barras...")
        print("Boleto emitido! Pagamento será compensado em até 2 dias.")
        return True


def processarPagamento(total, carrinho):
    if not carrinho:
        print("Carrinho vazio! Não é possível finalizar a compra.")
        return

    os.system('cls')
    print("\n=== MÉTODOS DE PAGAMENTO ===")
    print("[1] Cartão")
    print("[2] PIX")
    print("[3] Boleto")
    
    opcao = int(input("Escolha: "))

    match opcao:
        case 1:
            metodo = PagamentoCartao(total)
        
        case 2:
            metodo = PagamentoPix(total)

        case 3:
            metodo = PagamentoBoleto(total)

        case _:
            print("Opção inválida!")
            return
    
    # Chama o método polimórfico
    aprovado = metodo.processar_pagamento()

    if aprovado:
        os.system('cls')
        print("\nCOMPRA FINALIZADA COM SUCESSO!")
        carrinho.clear()
        input("\nPressione Enter para continuar...")
    else:
        print("Pagamento não aprovado.")
