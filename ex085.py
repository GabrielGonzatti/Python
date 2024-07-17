'''
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Me informe um valor: ')))
    for p in lista:
        if p % 2 == 0:
            print('oi')
            par.append(p)
        else:
            impar.append(p)
    lista.clear()
    resposta = str(input('Quer continuar? [S/N]')).upper()
    if resposta in 'N':
        break
    else:
        continue
par.sort()
impar.sort()
print(f'Valores Pares: {par}')
print(f'Valores Impares: {impar}')
