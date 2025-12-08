class Cliente:
    def __init__(self, nome, cpf, birth, cel, cidade):
        self._nome = nome
        self._cpf = cpf
        self._birth = birth
        self._cel = cel
        self._cidade = cidade

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
    
    def get_cidade(self):
        return self._cidade 
    
    def set_cidade(self, cidade):
        if not cidade:
            print("Cidade inválida")
        else:
            self._cidade = cidade
    
    def __str__(self):
        return f"Nome: {self._nome} | CPF: {self._cpf} | Data de Nascimento: {self._birth} | Celular: {self._cel} | Cidade: {self._cidade}"