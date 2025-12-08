from abc import ABC, abstractmethod
import os
import json
from datetime import datetime

"""TRECHO OO: hierarquia de Pagamento com polimorfismo em processar_pagamento()."""

from estruturado.produtos import salvar_estoque
from dados import lista_produtos
from oo.pedido import Pedido


class Pagamento(ABC):
    def __init__(self, valor_total):
        self.valor_total = valor_total

    @abstractmethod
    def processar_pagamento(self):
        """Executa a coleta de dados e confirma o pagamento (simulação)."""
        pass

    def ajustar_valor(self):
        """Retorna o valor ajustado por taxas/descontos da forma de pagamento (por padrão sem alteração)."""
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
        # Cartão: acréscimo de 2.5% sobre o total (taxa de processamento)
        taxa = 0.025
        ajustado = round(self.valor_total * (1 + taxa), 2)
        return ajustado


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
        # PIX: desconto de 10% quando pago via PIX
        desconto = 0.10
        ajustado = round(self.valor_total * (1 - desconto), 2)
        return ajustado


class PagamentoBoleto(Pagamento):
    def __init__(self, valor_total):
        super().__init__(valor_total)

    def processar_pagamento(self):
        print("\n=== PAGAMENTO VIA BOLETO ===")
        print("Gerando código de barras...")
        print("Boleto emitido! Pagamento será compensado em até 2 dias.")
        return True

    def ajustar_valor(self):
        # Boleto: pequena taxa administrativa de 1%
        taxa = 0.01
        ajustado = round(self.valor_total * (1 + taxa), 2)
        return ajustado


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
    
    # Exibe o total ajustado pela forma de pagamento (polimorfismo via ajustar_valor)
    total_ajustado = metodo.ajustar_valor()
    print(f"\nValor base: R${total:.2f}")
    if total_ajustado != total:
        print(f"Valor com taxa/desconto ({metodo.__class__.__name__}): R${total_ajustado:.2f}")
    else:
        print(f"Valor a pagar: R${total_ajustado:.2f}")

    confirmar = input("Confirmar e prosseguir com o pagamento? [s/N]: ").strip().lower()
    if confirmar != 's':
        print("Pagamento cancelado pelo usuário.")
        return

    # Chama o método polimórfico (simula coleta de dados e aprovação)
    aprovado = metodo.processar_pagamento()

    if aprovado:
        os.system('cls')
        print("\nCOMPRA FINALIZADA COM SUCESSO!")
        
        # TRECHO OO: Cria Pedido e persiste (UML: Cliente 0..* Pedido)
        try:
            pedido = Pedido(cliente, carrinho.itens, total_ajustado)
            salvar_pedidos(pedido)
            print(f"Número do pedido: {pedido.codigo}")
        except Exception as e:
            print(f"Aviso: não foi possível gerar o pedido ({e})")
        
        # Atualiza persistência do estoque apenas quando a compra for finalizada
        try:
            salvar_estoque(lista_produtos)
        except Exception:
            # salvamento não crítico — seguir mesmo se falhar
            pass

        carrinho.clear()
        input("\nPressione Enter para continuar...")
    else:
        print("Pagamento não aprovado.")


def salvar_pedidos(pedido):
    """TRECHO OO: Persiste Pedido em JSON (relação UML Cliente 0..* Pedido)."""
    arquivo = "pedidos.json"
    pedidos = []
    
    # Carrega pedidos existentes
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                pedidos = json.load(f)
        except:
            pedidos = []
    
    # Adiciona novo pedido
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
    
    # Salva no arquivo
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=2)
