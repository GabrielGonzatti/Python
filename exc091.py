'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter # vai servir para em dicionários apontarmos a posição key=itemgetter(0 ou 1)
jogo = {'jogador1': randint(1,20),
         'jogador2': randint(1,20),
         'jogador3': randint(1,20),
         'jogador4': randint(1,20)}
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(3)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
