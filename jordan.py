from functools import reduce

class Produto:
    def __init__(self, nome, preco, categoria, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__categoria = categoria
        self.__estoque = estoque
    
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço invalido")
            
    def get_categoria(self):
        return self.__categoria
    
    def set_categoria(self, categoria):
        self.__categoria = categoria

    def get_estoque(self):
        return self.__estoque
    
    def set_estoque(self, novo_estoque):
        if novo_estoque >= 0:
            self.__estoque = novo_estoque
        else:
            print("Estoque não pode ser negativo")

    def calcularValorFinal(self):
        return self.__preco

    def __str__(self):
        return f"Produto: {self.__nome} | Preço: R${self.__preco} | Catergoria: {self.__categoria} | Estoque: {self.__estoque}"       

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

carrinho = [] 
lista_produtos = []

notebook = Produto("Notebook", 3500.00, "Eletrônicos", 5)
leite = Produto("Leite", 5.90, "Alimentos", 50)
livro = Produto("O senhor dos Anéis", 89.90, "Livros", 15)

lista_produtos.append(notebook)
lista_produtos.append(leite)
lista_produtos.append(livro)


def listarProdutos(lista_produtos):
    print("\n## CATÁLOGO DE PRODUTOS ##")
    if not lista_produtos:
        print("Nenhum produto cadastrado")
        return
    
    for i, produto in enumerate(lista_produtos):
        print(f"[{i + 1}] {produto}")

    print("-" * 30)


def adicionarProdutoCarrinho(lista_produtos, carrinho):
    None


def removerProdutoCarrinho(carrinho):
    None


def exibir_menu():
    """Menu atualizado com a opção [3] Remover."""
    print("\n========== LOJA MULTI-PARADIGMA ==========")
    print("[1] Listar Produtos")
    print("[2] Adicionar Produto ao Carrinho")
    print("[3] Remover Produto do Carrinho") 
    print("[4] Calcular Total da Compra")
    print("[5] Sair")
    print("-" * 40)

def iniciarLoja(lista_produtos, carrinho):
   
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        # Uso de if/elif/else para simular o switch
        if opcao == 1:
            listarProdutos(lista_produtos)
        elif opcao == 2:
            adicionarProdutoCarrinho(lista_produtos, carrinho) 
        elif opcao == 3:
            removerProdutoCarrinho(carrinho) 
        elif opcao == 4:
            total = calcularTotalCompra(carrinho)
            print(f"\nTOTAL DA COMPRA: R${total:.2f}")
        elif opcao == 5:
            print("Obrigado por utilizar a loja! Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def calcularTotalCompra(carrinho):
    if not carrinho:
        return 0.0

    valores_itens = map(
        lambda item: item['quantidade'] * item['produto'].calcularValorFinal(), 
        carrinho
    )

    total = reduce(
        lambda acc, valor_item: acc + valor_item,
        valores_itens
    )

    return total


iniciarLoja(lista_produtos, carrinho)