'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p)
# print(f'A metade de {p} é {moeda.metade(p, True)}')
# print(f'O dobro de {p} é {moeda.dobro(p, True)}')
# print(f'O Aumento de {p} é {moeda.aumentar(p,10, True)}')
# print(f'A diminuição de {p} é {moeda.diminuir(p,13, True)}')