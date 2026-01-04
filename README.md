# 🛒 Projeto-Paradigmas

Simulação de uma **loja online** desenvolvida como trabalho acadêmico em Python.  
O sistema utiliza arquivos **JSON** para armazenar dados de clientes, produtos e pedidos, dispensando o uso de banco de dados tradicional.

## 🧠 Descrição

Este projeto tem como objetivo aplicar e comparar diferentes **paradigmas de programação**, simulando o funcionamento básico de uma loja virtual.

Funcionalidades principais:
- Cadastro de clientes
- Gerenciamento de estoque
- Realização de pedidos
- Persistência de dados em arquivos JSON

O projeto foi desenvolvido com fins **educacionais**, focado no aprendizado prático de paradigmas de programação.

---

## 📁 Estrutura do Repositório

Projeto-Paradigmas/

├── estruturado/ # Implementação usando paradigma estruturado

├── funcional/ # Implementação usando paradigma funcional

├── oo/ # Implementação usando orientação a objetos

├── dados.py # Funções de leitura e escrita em JSON

├── main.py # Arquivo principal de execução

├── dados_cliente.json # Dados dos clientes

├── estoque.json # Dados do estoque

└── pedidos.json # Dados dos pedidos


---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- Arquivos **JSON**
- Biblioteca padrão do Python

---

## 📦 Requisitos

- Python 3.x instalado

Não é necessário instalar bibliotecas externas.

---

## ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/JordanAguiar/Projeto-Paradigmas.git
```
Acesse a pasta do projeto:
```bash
cd Projeto-Paradigmas
```

Execute o programa principal:
```bash
python main.py
```

# 📘 Funcionalidades

📋 Listagem de produtos

➕ Cadastro de novos produtos

👤 Cadastro de clientes

🛍️ Realização de pedidos

💾 Armazenamento persistente em JSON

# 🗂️ Estrutura dos Dados (JSON)

👤 Clientes (dados_cliente.json)

```bash
[
  {
    "id": 1,
    "nome": "João Silva",
    "email": "joao@email.com"
  }
]
```

📦 Estoque (estoque.json)

```bash

[
  {
    "id": 101,
    "nome": "Produto Exemplo",
    "preco": 50.0,
    "quantidade": 10
  }
]
```

🧾 Pedidos (pedidos.json)

```bash

[
  {
    "cliente_id": 1,
    "itens": [
      {
        "produto_id": 101,
        "quantidade": 2
      }
    ],
    "total": 100.0
  }
]
```
⚠️ Estrutura ilustrativa — pode variar conforme a implementação.

# 👨‍💻 Autores

[Jordan Aguiar](https://github.com/JordanAguiar)

[Igor Lyra](https://github.com/Igotkun)

Kelvyn Dantas

Trabalho acadêmico – Paradigmas de Programação

Python • JSON • Lógica de Programação
