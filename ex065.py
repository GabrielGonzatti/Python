'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
escolha = 'não'
cont = 0
soma = 0
maior = 0
menor = 0
media = 0
while escolha != 'sim':
    escolha = int(input('Escolha um número: '))
    soma = escolha + soma
    cont += 1
    if menor == 0:
        menor = escolha
    elif escolha < menor:
        menor = escolha
    if escolha > maior:
        maior = escolha
    resposta = input('Você quer continuar ou deseja parar? [sim] | [não]')
    if resposta == 'sim':
        media = soma/cont
        break
    else:
        print('Continuando...')
        continue
print(f'Você escolheu {cont} números e a soma deles foi {soma}, a média deles foi: {media}')
