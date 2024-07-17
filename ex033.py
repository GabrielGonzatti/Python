'''Faça um programa para ler 3 número e verificar qual é o maior e o menor'''
#num1,num2,num3
#se num1>num2 -- maior = num1 -- menor = num2 | se nao maior = num2 -- menor =num1
#se num2>num3 -- maior = num2 --

num1 = int(input('Fala um número aí: '))
num2 = int(input('Fala um número aí: '))
num3 = int(input('Fala um número aí: '))
#verificando o menor
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3

#verificando o maior:

maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num2
print('O maior é {} e o maior é {}'.format(maior, menor))
