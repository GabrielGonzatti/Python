'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.

'''
m = 0
f = 0
pessoas = 0

while True:
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? [M]/[F]')).upper()
    if idade > 18:
        pessoas = pessoas +1
    if sexo == "M":
        m = m+1
    elif sexo == "F" and idade < 20:
        f = f+1
    resposta = str(input('Quer continuar? [SIM]/[NAO]')).upper()
    if resposta == 'NAO':
        print(f'Quantidade de pessoas maiores que 18: {pessoas} | Quantidade de homens: {m} | Quantidadae de mulhers menos que vinte anos: {f}')
        break
    else:
        pass



