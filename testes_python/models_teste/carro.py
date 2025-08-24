from models_teste.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
        
        
    def __str__(self):
        return self.modelo
        
        
        
    def ligar(self):
        print(f'O carro {self.modelo} esta ligado')
    