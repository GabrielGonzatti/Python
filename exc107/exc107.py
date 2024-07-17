'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import moeda

p = float(input('Digite o preço: R$'))
taxa = float(input('Caso queira aumentar ou diminuir, informe a taxa: R$'))
print(f'A metade de {p} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {p} é {moeda.moeda(moeda.dobro(p))}')
print(f'O Aumento de {p} é {moeda.moeda(moeda.aumentar(p))}')
print(f'A diminuição de {p} é {moeda.moeda(moeda.diminuir(p))}')