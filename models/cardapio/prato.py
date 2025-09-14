from models.cardapio.itemCardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
        
           
    def __str__(self):
        return f'{self._nome.ljust(20)} | R$ {str(self._preco).ljust(8)} | Descrição: {self.descricao}'
    
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)