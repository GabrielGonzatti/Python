'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
while True:
    computador = randint(0,10)
    jogada = int(input('Escolha um número para jogar PAR ou IMPAR: '))
    tipo = str(input('Escolha um tipo entre PAR ou IMPAR: ')).upper()
    soma = computador + jogada
    if soma % 2 == 0 and tipo == 'PAR':
        print(computador)
        print(soma)
        print('PAR')
    else:
        print('Impar')
        print(computador)
        print(soma)

