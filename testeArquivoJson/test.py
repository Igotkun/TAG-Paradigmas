import json
import os
from testeArquivoJson import dados_cliente

ARQUIVO = "/testeArquivoJson/dados_cliente.json"

if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, 'w', ENCODING='utf-8') as f:
        f.write("[]")

#Carregando dados existentes

try:
    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        clientes = json.load(f)

except json.JSONDecodeError:
    clientes = []

nome = input("Nome do cliente: ")
cpf = input("CPF: ")
cidade = input("Cidade: ")


novo_cliente = {
    "nome": nome,
    "cpf" : cpf,
    "cidade" : cidade
}

clientes.append(novo_cliente)

with open(ARQUIVO, 'w', encoding='utf-8') as f:
    json.dump(clientes, f, indent=4, ensure_ascii=False)

print("Cliente salvo com sucesso!")

