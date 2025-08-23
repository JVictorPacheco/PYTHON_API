from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremesa import Sobremesa



restaurante_burguer = Restaurante('burgues do chefe', 'Hamburgueria Artesanal')
# restaurante_burguer.receber_avaliacao('Vitinho', 4)
# restaurante_burguer.receber_avaliacao('Vitinho', 10)
# restaurante_burguer.alternar_estado_status()
bebida_suco = Bebida('Suco de Leticia', 10.0, 'Grande Gourmet')
bebida_suco.aplicar_desconto()

prato_de_churrasco = Prato('Prato de churrasco', 20.0, 'Melhor churrasco da cidade')
prato_de_churrasco.aplicar_desconto()

sobremesa_brownie = Sobremesa('Doce',  'Grande Gourmet', 'Brownie com petit gateau cremoso com massa e chocolate feito na casa', 'Brownie com petit gateau', 25.50)
sobremesa_brownie.aplicar_desconto()



restaurante_burguer.adicionar_item(bebida_suco)
restaurante_burguer.adicionar_item(prato_de_churrasco)
restaurante_burguer.adicionar_item(sobremesa_brownie)


def main():
     #print(restaurante_burguer)
     restaurante_burguer.exibir_cardapio
     


if __name__ == '__main__':
    main()