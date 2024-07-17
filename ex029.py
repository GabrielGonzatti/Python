'''
Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
ele foi multado. Multa --> R$ 7K para cada KM acima do limite.
'''
#veloc --> input

print('SUA VELOCIDADE LHE DÁ UMA MULTA? CALCULE!')
veloc = int(input('Qual sua velocidade atual? '))
print('...VERIFICANDO... ')

if veloc<=80:
    print('Você tomou cuidado e não está multado!')
else:
    multa = veloc-80
    multatot = multa*7
    print('Você foi descuidado, com uma velocidade de {} e tomou uma multa de {:.2f} R$'.format(veloc, multatot))
