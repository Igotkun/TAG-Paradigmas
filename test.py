import json
import os

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


    novo_cliente = {
        "nome": nome,
        "cpf" : cpf,
        "birth" : birth,
        "cel" : cel,
        "endereço" : endereco
    }

    clientes.append(novo_cliente)

    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

    print("Cliente salvo com sucesso!")

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
        "endereço" : endereco
    }

    clientes[indice] = clienteUpdate

    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

    print("\nCliente alterado com sucesso!")