from abc import ABC, abstractmethod
import os
import json

from estruturado.produtos import salvar_estoque
from dados import lista_produtos
from oo.pedido import Pedido
from funcional.funcoes_funcionais import aplicar_desconto, gerar_multiplicador


class Pagamento(ABC):
    def __init__(self, valor_total):
        self.valor_total = valor_total

    @abstractmethod
    def processar_pagamento(self):
        pass

    def ajustar_valor(self):
        return self.valor_total


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

    def ajustar_valor(self):
        multiplicador_taxa = gerar_multiplicador(1.025)
        return round(multiplicador_taxa(self.valor_total), 2)


class PagamentoPix(Pagamento):
    def __init__(self, valor_total):
        super().__init__(valor_total)

    def processar_pagamento(self):
        print("\n=== PAGAMENTO VIA PIX ===")
        chave = input("Digite sua chave PIX: ")
        print("Gerando QR Code...")
        print("Pagamento confirmado!")
        return True

    def ajustar_valor(self):
        return aplicar_desconto(self.valor_total, desconto_percent=10)


class PagamentoBoleto(Pagamento):
    def __init__(self, valor_total):
        super().__init__(valor_total)

    def processar_pagamento(self):
        print("\n=== PAGAMENTO VIA BOLETO ===")
        print("Gerando código de barras...")
        print("Boleto emitido! Pagamento será compensado em até 2 dias.")
        return True

    def ajustar_valor(self):
        multiplicador_taxa = gerar_multiplicador(1.01)
        return round(multiplicador_taxa(self.valor_total), 2)


def processarPagamento(total, carrinho, cliente):
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
    
    total_ajustado = metodo.ajustar_valor()
    print(f"\nValor base: R${total:.2f}")
    if total_ajustado != total:
        print(f"Valor com taxa/desconto ({metodo.__class__.__name__}): R${total_ajustado:.2f}")
    else:
        print(f"Valor a pagar: R${total_ajustado:.2f}")

    confirmar = input("\nConfirmar e prosseguir com o pagamento? [s/N]: ").strip().lower()
    if confirmar != 's':
        print("Pagamento cancelado pelo usuário.")
        return

    aprovado = metodo.processar_pagamento()

    if aprovado:
        os.system('cls')
        print("\nCOMPRA FINALIZADA COM SUCESSO!")
        
        try:
            pedido = Pedido(cliente, carrinho.itens, total_ajustado)
            salvar_pedidos(pedido)
            print(f"Número do pedido: {pedido.codigo}")
        except Exception as e:
            print(f"Aviso: não foi possível gerar o pedido ({e})")
        
        try:
            salvar_estoque(lista_produtos)
        except Exception:
            pass

        carrinho.clear()
        input("\nPressione Enter para continuar...")
    else:
        print("Pagamento não aprovado.")


def salvar_pedidos(pedido):
    arquivo = "pedidos.json"
    pedidos = []
    
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                pedidos = json.load(f)
        except:
            pedidos = []
    
    novo_pedido = {
        "codigo": pedido.codigo,
        "cliente_cpf": pedido.cliente.cpf,
        "cliente_nome": pedido.cliente.nome,
        "itens": [
            {
                "produto_nome": item.produto.nome,
                "produto_categoria": item.produto.categoria,
                "quantidade": item.quantidade,
                "valor_unitario": item.produto.preco
            }
            for item in pedido.itens
        ],
        "total": pedido.total,
        "data": pedido.data.isoformat()
    }
    
    pedidos.append(novo_pedido)
    
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=2)
