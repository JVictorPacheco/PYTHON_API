class Pessoa:
    
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        

    @property
    def nomePessoa(self):
        return self._nome
    
    
    
mulher = Pessoa('Leticia', 26)
print(mulher.nomePessoa)
    
    