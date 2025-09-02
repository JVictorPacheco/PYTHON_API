class Produto:
    
    def __init__(self, preco):
        self._preco = preco
        
        
        
        
    @property
    def preco(self):
        return self._preco
    
    
    
    @preco.setter # permite definir valor
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")        
        self._preco = valor
        
        
    # @preco.setter  # Permite definir o valor
    # def preco(self, valor):
    #     if valor < 0:
    #         raise ValueError("Preço não pode ser negativo")
    #     self._preco = valor
            
            
            
#uso
produto = Produto(-10)
print(produto.preco)
#produto.preco = -50
