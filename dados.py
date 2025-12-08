import json
import os
from oo.cliente import Cliente

carrinho = [] # memória temporária
lista_produtos = [] # memória temporária


def criarCliente():

    ARQUIVO = "dados_cliente.json"

    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            f.write("[]")

    #Carregando dados existentes

    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            clientes = json.load(f)

    except json.JSONDecodeError:
        clientes = []

    nome = input("Nome: ")
    cpf = input("CPF: ")
    birth = input("Data de Nascimento: ")
    cel = input("Celular: ")
    endereco = input("Endereço: ")

    novo_cliente_obj = Cliente(nome, cpf, birth, cel, endereco)

    novo_cliente = {
        "nome": novo_cliente_obj.get_nome(),
        "cpf" : novo_cliente_obj.get_cpf(),
        "birth" : novo_cliente_obj.get_birth(),
        "cel" : novo_cliente_obj.get_cel(),
        "endereco" : novo_cliente_obj.get_endereco()
    }

    clientes.append(novo_cliente)

    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

    print("Cliente salvo com sucesso!")


def lerClientes():
    ARQUIVO = "dados_cliente.json"

    if not os.path.exists(ARQUIVO):
        print("Nenhum cliente cadastrado ainda!")
        return []

    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            clientes = json.load(f)
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON!")
        return []
    
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return []
    
    os.system("cls")
    print("\n--- LISTA DE CLIENTES ---")
    for i, c in enumerate(clientes, 1):
        print(f"[{i}] {c['nome']} - CPF: {c['cpf']}")
    print("-------------------------")
    return clientes
    

def alterarCliente():

    
    ARQUIVO = "dados_cliente.json"

    if not os.path.exists(ARQUIVO):
        print("Nenhum cliente cadastrado ainda!")
        return

    try:
        with open(ARQUIVO, 'r', encoding='utf') as f:
            clientes = json.load(f)
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo!")
        return
    
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado para alterar.")
        return

    os.system("cls")
    print("\n--- CLIENTES CADASTRADOS ---")
    for i, c in enumerate(clientes):
        print(f"{i} - {c['nome']} ({c['cpf']})")
    print("----------------------------")

    #Escolher cliente pelo indice
    try:
        indice = int(input("Digite o índice do cliente que deseja alterar:"))
        cliente = clientes[indice]
    except (ValueError, IndexError):
        print("Índice inválido!")
        return

    print("\nDeixe o campo vazio para manter o valor atual. \n")

    nome = input(f"Nome [{cliente['nome']}]: ") or cliente['nome']
    cpf = input(f"CPF [{cliente['cpf']}]: ") or cliente['cpf']
    birth = input(f"Data de Nascimento: [{cliente['birth']}]") or cliente['birth']
    cel = input(f"Celular: [{cliente['cel']}]") or cliente['cel']
    endereco = input(f"Endereço: [{cliente['endereco']}]") or cliente['endereco']

    #Update
    clienteUpdate = {
        "nome": nome,
        "cpf" : cpf,
        "birth" : birth,
        "cel" : cel,
        "endereco" : endereco
    }

    clientes[indice] = clienteUpdate

    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

    print("\nCliente alterado com sucesso!")


def selecionar_cliente():
    """TRECHO OO: Permite seleção de Cliente para compra (relação UML Cliente 0..* Pedido)."""
    clientes = lerClientes()
    if not clientes:
        print("Nenhum cliente disponível.")
        input("Pressione Enter para continuar...")
        return None
    
    print("\nSelecione um cliente:")
    for i, cliente_dict in enumerate(clientes, 1):
        print(f"[{i}] {cliente_dict['nome']} - CPF: {cliente_dict['cpf']}")
    
    try:
        idx = int(input("Escolha: ")) - 1
        if 0 <= idx < len(clientes):
            c = clientes[idx]
            cliente = Cliente(c['nome'], c['cpf'], c['birth'], c['cel'], c['endereco'])
            print(f"Cliente {cliente.nome} selecionado com sucesso!")
            input("Pressione Enter para continuar...")
            return cliente
    except:
        pass
    
    print("Seleção inválida.")
    input("Pressione Enter para continuar...")
    return None