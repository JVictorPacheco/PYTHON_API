from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato



restaurante_burguer = Restaurante('burgues do chefe', 'Hamburgueria Artesanal')
# restaurante_burguer.receber_avaliacao('Vitinho', 4)
# restaurante_burguer.receber_avaliacao('Vitinho', 10)
# restaurante_burguer.alternar_estado_status()
bebida_suco = Bebida('Suco de Leticia', 10.0, 'Grande Gourmet')
prato_de_churrasco = Prato('Prato de churrasco', 20.0, 'Melhor churrasco da cidade')


restaurante_burguer.adicionar_item(bebida_suco)
restaurante_burguer.adicionar_item(prato_de_churrasco)


def main():
     restaurante_burguer.exibir_cardapio
     


if __name__ == '__main__':
    main()