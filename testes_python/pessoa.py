class Pessoa:
    
        def __init__(self, nome, idade, profissao):
            self.nome = nome
            self.idade = idade
            self.profissao = profissao
            
            
            
        def __str__(self): #check
                return f'Nome: {self.nome} | Idade {self.idade} | Profissão {self.profissao}'
            
            
        def aniversario(self):
            self.idade += 1
            
            
            
        @property
        def saudacao(self):
            if self.profissao:
                return f'Olá eu me chamo {self.nome} e trabalho como {self.profissao}'
            else:
                return f'Olá, sou {self.nome}'
        
       
       
    
pessoa_leticia = Pessoa('Leticia Souza', 26, 'Nutricionista')
aniversario_27 = pessoa_leticia.aniversario()


print(f"{pessoa_leticia}")

print(pessoa_leticia.saudacao)




