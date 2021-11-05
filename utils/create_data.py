import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configurations.settings')
django.setup()

import string
import timeit
from random import choice, random, randint
from product.models import Product

class Utils:
    """ Métodos Genéricos """
    @staticmethod
    def gen_digits(max_length):
        # Função para gerar numeros aleatórios, baseados no max_length que passaremoos
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:

    @staticmethod
    def criar_produtos(produtos):
        Product.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                ProdutctsName=produto,
                CurrentStock=randint(10, 200),
            )
            obj = Product(**data)
            aux.append(obj)
        Product.objects.bulk_create(aux)


produtos = (
    'Papel sulfite A4 75g 210mmx297mm Chamex PT 500 FL'	,
    'Bloco Adesivo Post-it Novas Cores - 38 mm x 50 mm - 400 folhas'	,
    'Bloco adesivo 38mm x 51mm sortido - 50 folhas'	,
    'Clips nr.2/0 galvanizado (lata c/500g)'	,
    'Elástico amarelo n.18 c/ 1200 unidades'	,
    'Perfurador de papel 02 furos p/10 fls'	,
    'Grampeador médio 26/6 30fl O-300 Easy Office'	,
    'Cartão de ponto 86 x 180mm Spiral'	,
    'Bloco Adesivo Post-it® 76x76 Amarelo com 100 folhas'	,
    'Cola em bastão 20g Pritt 1905656 Henkel'	,
    'Molhador de dedos 12g Waleu'	,
    'Perfurador de papel 02 furos p/25 fls D-230 Easy Office CX	'	,
    'Marcador de Página Adesivo 76 mm x 15 mm - 180 folhas'	,
    'Clips nr.3/0 galvanizado (pt c/50un)'	,
    'Carimbo datador auto-entintado S120'	,
    'Perfurador de papel 2 furos 40/45 folhas'	,
    'Clips nr.0 galvanizado (pt c/100un)'	,
    'Kit Caneta Esferográfica BIC, Azul Ponta Média de 1.2mm'	,
    'Almofada carimbo N.3 azul 6,7x11,0cm Pilot'	,
    'Almofada carimbo N.2 preta 5,9x9,4cm Pilot'	,
    'Pincel marca texto c/4 cores grifpen MT/ESZF Faber Castell'	,
    'Pincel marca texto pastel 6 cores MT/TP6ZF Faber Castell'	,
    'Pincel marca texto amarelo Oval'	,
    'Pincel Marcador de Texto com Grip Cores Pastéis BIC Marking'	,
    'Pincel marca texto 6 cores sortido pastel 5113 Oval'	,
    'Pincel marca texto lumi-color 200-sl am/vd/rs Pilot 3 cores'	,
    'Caneta Esferográfica Retrátil BIC, 4 Cores, Ponta Média de 1.0mm'	,
    'Caneta Esferográfica 1,0mm Azul, SM-BK440-C6	'	,
    'Pacote Caneta Esferográfica 1,0mm Preta, Vermelha e Azul'	,
    'Caneta fixa c/corrente bolinha cromada'	,
    'Caneta Esferográfica BIC Cristal, Ponta Ultra Fina de 0.7mm'	,
    'Pacote Caneta esferográfica 0.7mm metálica Preta, Vermelha e Azul'	,
    'Caneta Esferográfica 0.7mm Preta'	,
    'Corretivo em fita 5mmx6m folha Oval'	,
    'Cola em bastão 20g Pritt'	,
    'Lápis preto n.2 max redondo Faber Castell CX 4 UN'	,
    'Pacote Caneta esferográfica 1.0mm Verde, Preta, Vermelha e Azul'	,
    'Régua em aço 30cm	'	,
    'Caderno universitário capa dura 10x1 160fls'	,
    'Caderno Universitário Capa Dura 10x1 200fls'	,
    'Lapiseira Bic 0.3mm'	,
    'Lapiseira Bic 0.5mm'	,
    'Lapiseira Bic 0.7mm'	,
    'Tesoura Média corte fino'	,
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)


toc = timeit.default_timer()

print('Tempo:', toc - tic)