'''
31:
Desenvolva um programa que pergunte a distância de uma viagem KM.
Calcule o preço da passagem, cobrando 0.50 RS por KM para viagens até 200Km e 0.45 para viagens mais longas.
'''
#dist -> input;
#se dist <= 200 valor 0.50 * km | se não (se for maior) --> 0.45 * km;

dist = int(input('Qual a distância em KM desta viagem? '))

if dist<=200:
    valor = dist*0.50
    print('O valor da viagem ficou: {} R$'.format(valor))
else:
    valor = dist*0.45
    print('O valor da viagem ficou: {} R$'.format(valor))
