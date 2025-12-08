"""TRECHO OO: classe Cliente com encapsulamento (getters/setters)."""

class Cliente:
    def __init__(self, nome, cpf, birth, cel, endereco):
        self._nome = nome
        self._cpf = cpf
        self._birth = birth
        self._cel = cel
        self._endereco = endereco

    # Propriedades (properties) para acesso simplificado
    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def birth(self):
        return self._birth

    @property
    def cel(self):
        return self._cel

    @property
    def endereco(self):
        return self._endereco

    # Getters tradicionais
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        if not nome:
            print("Nome inválido")
        else:
            self._nome = nome

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        if not cpf:
            print("CPF inválido")
        else:
            self._cpf = cpf
            
    def get_birth(self):
        return self._birth

    def set_birth(self, birth):
        if not birth:
            print("Data de Nascimento inválida")
        else:
            self._birth = birth

    def get_cel(self):
        return self._cel

    def set_cel(self, cel):
        if not cel:
            print("Celular inválido")
        else:
            self._cel = cel
    
    def get_endereco(self):
        return self._endereco
    
    def set_endereco(self, endereco):
        if not endereco:
            print("Endereço inválida")
        else:
            self._endereco = endereco
    
    def __str__(self):
        return f"Nome: {self._nome} | CPF: {self._cpf} | Data de Nascimento: {self._birth} | Celular: {self._cel} | Endereco: {self._endereco}"