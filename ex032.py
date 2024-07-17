'''
Faça um programa que leia uma ano e veja se ele é bissexto.
'''
#ano%4==0
#ano --> input
#se (divisão) é ano bi | se não é ano comum

ano = int(input('Me fale um ano: '))

if ano%4==0:
    print('Este ano é bissexto!')
else:
    print('Este ano é comum!')
