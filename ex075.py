'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''
numb = 0
par = 0
nove = 0
tres = 0

while numb <= 4:
    numb = numb + 1
    escolha_numero = (int(input(f'Olá, informe o {numb}º número: ')))
    if escolha_numero % 2 == 0:
        par = par + 1
    if escolha_numero == 9:
        nove = nove + 1
    if escolha_numero == 3 and tres == 0:
        tres = numb
    if numb == 4:
        break
print(f'O número 9 foi repetido {nove} vezes. | O número três foi digitado na posição {tres} | Teve {par} números pares.')