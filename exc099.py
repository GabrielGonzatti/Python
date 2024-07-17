'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados.')
    for valor in num:
        print(valor)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

#programa principal
maior(2,9,5,7,2,1)
maior(4,7,3)
maior()