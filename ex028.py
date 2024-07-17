'''Escreva um programa que faça o computador pensar em um número inteiro
entre 0 a 5 e peça ao usuário para tentar descobrir qual foi o número escolhido pelo computador'''
#INT-> num -- compt
#input-> qual foi o num? IF(valida se acertou) ELSE (OPS)

import random
nome = str(input('Qual seu nome? '))
num = (random.randrange(1, 5))
#teste: num = 5
resposta = int(input('Adivinhe de 1 a 5 quanto o Mister ? tirou no dado! Fale um número: '))
if(resposta == num):
    print('Parabéns {}, a resposta foi {}!'.format(nome, resposta))
else:
    print('OPS! Quase conseguiu!')
#consertei um erro inicial bem simples, passei a resposta como inteiro pois estava lendo insta como str
