class Produto:
    def __init__(self, nome, preco, categoria, estoque):
        self._nome = nome
        self._preco = preco
        self._categoria = categoria
        self._estoque = estoque

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
            self._estoque = estoque


    # Método polimórfico
    def calcularValorFinal(self):
        return self._preco # genérico
    
    def __str__(self):
        return f"Produto: {self._nome} | Preço: R${self._preco} | Categoria: {self._categoria} | Estoque: {self.estoque}"


class Notebook(Produto):
    def __init__(self, nome, preco, estoque, marca):
        super().__init__(nome, preco, "Eletrônicos", estoque)
        self.__marca = marca
        
    def calcularValorFinal(self):
        return super().calcularValorFinal()
    
    def __str__(self):
        return f"{super().__str__()} | Marca: {self.__marca} | Valor Final: {self.calcularValorFinal():.2f}"

class Alimento(Produto):
    def __init__(self, nome, preco, estoque, marca):
        super().__init__(nome, preco, "Alimentos", estoque)
        self.__marca = marca
        
    def calcularValorFinal(self):
        return super().calcularValorFinal()
    
    def __str__(self):
        return f"{super().__str__()} | Marca: {self.__marca} | Valor Final: {self.calcularValorFinal():.2f}"


class Livro(Produto):
    def __init__(self, nome, preco, estoque, autor):
        super().__init__(nome, preco, "Livros", estoque)
        self.__autor = autor
        
    def calcularValorFinal(self):
        return super().calcularValorFinal()
    
    def __str__(self):
        return f"{super().__str__()} | Autor: {self.__autor} | Valor Final: {self.calcularValorFinal():.2f}"


