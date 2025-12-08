class ItemCarrinho:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")

        if produto.get_estoque() < quantidade:
            raise ValueError("Estoque insuficiente")

        for item in self.itens:
            if item.produto.get_nome() == produto.get_nome():
                item.quantidade += quantidade
                produto.set_estoque(produto.get_estoque() - quantidade)
                return

        self.itens.append(ItemCarrinho(produto, quantidade))
        produto.set_estoque(produto.get_estoque() - quantidade)

    def remover(self, produto, quantidade=None):
        for i, item in enumerate(self.itens):
            if item.produto.get_nome() == produto.get_nome():
                if quantidade is None or quantidade >= item.quantidade:
                    produto.set_estoque(produto.get_estoque() + item.quantidade)
                    self.itens.pop(i)
                else:
                    item.quantidade -= quantidade
                    produto.set_estoque(produto.get_estoque() + quantidade)
                return True
        return False

    def calcular_total(self):
        total = 0.0
        for item in self.itens:
            total += item.quantidade * item.produto.calcularValorFinal()
        return total

    def clear(self):
        self.itens.clear()

    def __len__(self):
        return len(self.itens)

    def __iter__(self):
        return iter(self.itens)

    def mostraCarrinho(self):
        if not self.itens or len(self.itens) == 0:
            print("O carrinho está vazio")
            return
        print("\n========== ITENS DO CARRINHO ==========")
        for i, item in enumerate(self.itens, 1):
            produto = item.produto
            quantidade = item.quantidade
            try:
                nome = produto.get_nome()
                preco = produto.get_preco()
            except Exception:
                nome = getattr(produto, 'nome', str(produto))
                preco = getattr(produto, 'preco', 0.0)
            print(f"[{i}] {nome} | Quantidade: {quantidade}x | R${preco:.2f}")
        print("-" * 40)

    def adicionarProdutoCarrinho(self, lista_produtos):
        if not lista_produtos:
            print("O catálogo de produtos está vazio.")
            return
        try:
            indice_input = int(input("Digite o NÚMERO do produto para adicionar: "))
            quantidade = int(input("Digite a QUANTIDADE: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")
            return

        indice_produto = indice_input - 1

        if 0 <= indice_produto < len(lista_produtos) and quantidade > 0:
            produto_selecionado = lista_produtos[indice_produto]
            estoque_atual = produto_selecionado.get_estoque()

            import os
            os.system('cls')
            print(f"Adicionar {quantidade}x {produto_selecionado.get_nome()} no Carrinho?")
            from funcional.funcoes_funcionais import confirma
            if confirma() == 0:
                return

            if estoque_atual >= quantidade:
                self.adicionar(produto_selecionado, quantidade)
                print(f"{quantidade}x {produto_selecionado.get_nome()} adicionado ao carrinho.")
                input("Aperte Enter para voltar")
            else:
                print(f"Estoque insuficiente. Disponível: {estoque_atual} unidade(s).")
                input("Aperte Enter para voltar")
        else:
            print("Opção de produto ou quantidade inválida")
            input("Aperte Enter para voltar")

    def removerProdutoCarrinho(self):
        self.mostraCarrinho()
        if not self.itens or len(self.itens) == 0:
            input("Aperte Enter para voltar")
            return
        try:
            indice_input = int(input("Digite o NÚMERO do item que deseja remover: "))
            quantidade_remover = int(input("Digite a QUANTIDADE a ser removida: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
            input("Aperte Enter para voltar")
            return

        indice_item = indice_input - 1

        if 0 <= indice_item < len(self.itens) and quantidade_remover > 0:
            item_selecionado = self.itens[indice_item]
            produto_selecionado = item_selecionado.produto
            quantidade_atual = item_selecionado.quantidade

            if quantidade_remover <= quantidade_atual:
                estoque_atual = produto_selecionado.get_estoque()
                produto_selecionado.set_estoque(estoque_atual + quantidade_remover)

                if quantidade_remover == quantidade_atual:
                    self.itens.pop(indice_item)
                    print(f"Item removido completamente.")
                else:
                    item_selecionado.quantidade -= quantidade_remover
                    print(f"{quantidade_remover}x removido. Restante: {item_selecionado.quantidade}")
                input("Aperte Enter para voltar")
            else:
                print(f"Quantidade inválida.")
                input("Aperte Enter para voltar")
        else:
            print("Opção inválida")
            input("Aperte Enter para voltar")

    def calcularTotalCompra(self):
        return self.calcular_total()
