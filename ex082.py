'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
numeros = []
par = []
impar = []
while True:
    numeros.append(int(input('Informe um número inteiro: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for item in numeros:
        print(item)
        if item % 2 == 0:
            par.append(item)
        else:
            impar.append(item)
print(f'Numeros totais {numeros} \nImpar {impar} \nPar {par}')
