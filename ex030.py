'''
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar;
'''

#Resto> num%2==0

num = int(input('Me fale um número: '))
#teste - num = 4
if num%2==0:
    print('Este número {} é par!'.format(num))
else:
    print('Este número {} é ímpar!'.format(num))
