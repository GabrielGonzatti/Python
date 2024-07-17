'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
escolha = 1
cont = 0
soma = 0
while escolha != 999:
    escolha = int(input('Escolha um número entre 1 a 999, sendo 999 a condição de parada: '))
    if escolha != 999:
        print('Continuando...')
        soma = escolha + soma
        cont += 1
    else:
        print('Encerrando...')
        break
print(f'Você escolheu {cont} números e a soma deles foi {soma}')

