'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
pesomaior = 0.0
pesomenor = 0
for pessoa in range(1,6):
    peso = float(input('Qual é seu peso? '))
    if peso > pesomaior:
        pesomaior = peso
    elif peso < pesomenor or pesomenor == 0:
        pesomenor = peso
print(f'O maior peso foi: {pesomaior}kg e o menor peso foi: {pesomenor}kg')

