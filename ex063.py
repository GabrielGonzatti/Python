'''
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
N primeiros elementos de uma Sequência de Fibonacci.
Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8
'''

'''Sequencia de fibonacci pega o número N e soma ele com ele mesmo, pegando o último e o atual os somando e criando novo atual'''

print('Sequencia de fibonacci')
ate = int(input('Quantos termos você gostaria de ver da sequencia de fibonacci? '))
t1 = 0
t2 = 1
print(f'{t1} + {t2} ', end='')
cont = 1
while cont <= ate:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'+ {t3} ', end='')
    cont +=1
