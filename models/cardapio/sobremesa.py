from models.cardapio.itemCardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao
        
    def __str__(self):
        return f'{self._nome.ljust(20)} | R$ {str(self._preco).ljust(8)} | Tipo: {self.tipo} | Tamanho: {self.tamanho} | Descrição: {self.descricao}'
        
        
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.10)
        