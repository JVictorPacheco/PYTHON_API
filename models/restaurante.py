from  models.avaliacao import Avaliacao
from  models.cardapio.itemCardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""
    
    restaurantes = []
    
    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
   
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
        
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria} |  {self.status}'
    
    
    @classmethod
    def listar_restaurante(cls):
       """Exibe uma lista formatada de todos os restaurantes."""
       print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
       for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |  {restaurante._status}')
            
            
    @property        
    def status(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '✅' if self._status else '❌'
    
    
    def alternar_estado_status(self):
        self._status = not self._status
        
        
    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        
        if 0 < nota <= 5:
            avalicao = Avaliacao(cliente, nota)
            self._avaliacao.append(avalicao)
         
        
    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        
        return media
        
        
    def adicionar_item(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            
            
            
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            print(f'{i}. {item}')
                
            
 