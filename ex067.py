'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
numero = int(input('Informe um número para ser feito a tabuada: '))
cont = 1
while cont <= 10:
    resultado = (numero * cont)
    print(f'Tabuada: {numero} X {cont} = {resultado}')
    cont += 1
