class Produto:
    def __init__(self, nome, preco, estoque=0):
        
        self._nome = nome
        self._preco = preco
        self.estoque = 0

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        if not nome:
            print("Nome inválido")
        else:
            self._nome = nome

    def get_preco(self):
        return self._preco

    def set_preco(self, p):
        if p < 0:
            print("Preço inválido")
        else:
            self._preco = p
    
    def get_estoque(self):
        return self._estoque

    def set_estoque(self, quant):
        if quant < 0:
            print("Estoque inválido")
        else:
            self._estoque = quant

    # Método polimórfico
    def calcularValorFinal(self):
        return self._preco # genérico


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso, estoque=0):  
            super().__init__(nome, preco, estoque)
            self._peso = peso
            
    def get_peso(self):
        return self._peso
    
    def set_peso(self, peso):
        if peso < 0:
            print("Peso inválido")
        else:
            self._peso = peso
        
    def calcularValorFinal(self):
        preco_base = self.get_preco()
        
    


class ProdutoDigital(Produto):
    def calcularValorFinal(self):
        pass  # desconto ou taxa digital
