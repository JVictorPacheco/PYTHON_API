from models.cardapio.itemCardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        
        
    def __str__(self):
        return f'{self._nome.ljust(20)} | R$ {str(self._preco).ljust(8)} | Tamanho: {self.tamanho}'
    
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
    