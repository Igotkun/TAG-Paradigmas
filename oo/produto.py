"""TRECHO OO: classes Produto e subclasses — encapsulamento, herança e polimorfismo."""

class Produto:
    def __init__(self, nome, preco, categoria, estoque):
        self._nome = nome
        self._preco = float(preco)
        self._categoria = categoria
        self._estoque = int(estoque)

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        if not nome:
            print("Nome inválido")
        else:
            self._nome = nome

    def get_preco(self):
        return self._preco

    def set_preco(self, preco):
        if preco < 0:
            print("Preço inválido")
        else:
            self._preco = preco
            
    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_estoque(self):
        return self._estoque

    def set_estoque(self, estoque):
        if estoque < 0:
            print("Estoque não pode ser negativo")
        else:
            self._estoque = int(estoque)

    # Properties para acesso simplificado
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def categoria(self):
        return self._categoria

    @property
    def estoque(self):
        return self._estoque


    # Método polimórfico — por padrão retorna o preço base
    def calcularValorFinal(self):
        return self._preco
    
    def __str__(self):
        return f"Produto: {self._nome} | Preço: R${self._preco} | Categoria: {self._categoria} | Estoque: {self._estoque}"


class Notebook(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, "Eletrônicos", estoque)
        
    def calcularValorFinal(self):
        return super().calcularValorFinal()


class Alimento(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, "Alimentos", estoque)
        
    def calcularValorFinal(self):
        return super().calcularValorFinal()


class Livro(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, "Livros", estoque)
        
    def calcularValorFinal(self):
        return super().calcularValorFinal()


