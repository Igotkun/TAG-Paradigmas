"""TRECHO OO: classe Pedido com relação 1..* com ItemPedido e relação com Cliente."""
import random
from datetime import datetime


class Pedido:
    """Representa um pedido: contém 1 ou mais itens, associado a um cliente, com código único."""
    
    def __init__(self, cliente, itens_carrinho, total):
        """
        Args:
            cliente: instância de Cliente
            itens_carrinho: lista de ItemCarrinho do carrinho
            total: valor total do pedido (float)
        """
        self._cliente = cliente
        self._codigo = self._gerar_codigo()  # Número aleatório 6 dígitos
        self._data = datetime.now()
        self._itens = []  # Lista de ItemPedido (1..*)
        self._total = total
        
        # Converter itens do carrinho para itens do pedido
        for item_carrinho in itens_carrinho:
            item_pedido = ItemPedido(item_carrinho.produto, item_carrinho.quantidade)
            self._itens.append(item_pedido)
    
    @staticmethod
    def _gerar_codigo():
        """Gera um código de pedido aleatório (6 dígitos)."""
        return random.randint(100000, 999999)
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def data(self):
        return self._data
    
    @property
    def itens(self):
        return self._itens
    
    @property
    def total(self):
        return self._total
    
    def get_codigo(self):
        return self._codigo
    
    def get_cliente(self):
        return self._cliente
    
    def get_data(self):
        return self._data
    
    def get_itens(self):
        return self._itens
    
    def get_total(self):
        return self._total
    
    def __str__(self):
        itens_str = ', '.join([f"{item.get_quantidade()}x {item.get_produto().get_nome()}" for item in self._itens])
        return f"Pedido #{self._codigo} | Cliente: {self._cliente.get_nome()} | Data: {self._data.strftime('%d/%m/%Y %H:%M')} | Itens: {itens_str} | Total: R${self._total:.2f}"


class ItemPedido:
    """Representa um item dentro de um pedido (quantidade × produto)."""
    
    def __init__(self, produto, quantidade):
        self._produto = produto
        self._quantidade = quantidade
    
    @property
    def produto(self):
        return self._produto
    
    @property
    def quantidade(self):
        return self._quantidade
    
    def get_produto(self):
        return self._produto
    
    def get_quantidade(self):
        return self._quantidade
    
    def __str__(self):
        return f"{self._quantidade}x {self._produto.get_nome()} - R${self._produto.get_preco() * self._quantidade:.2f}"
