'''
PROGRAMA DEVE PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR
CALCULAR O VALOR DA PRESTAÇÃO MENSAL -- NÃO PODE EXCEDER 30% DO SALÁRIO ou SALÁRIO SERÁ NEGADO

INPUT -> VALUE_CASA
INPUT -> SAL
INPUT -> TEMP_ANO

ANO = 12 MESES

TEMP_MES = TEMP_ANO * 12

VALUE_CASA % TEMP_MES

'''

value_casa = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
temp_ano = float(input('Quantos anos você quer parcelar? '))

temp_mes = temp_ano*12
value_final = value_casa/temp_mes

#SE {100% == sal}
#   {30% == x}
#   x = (sal * 30)/100
x = (sal * 30)/100
print('CONSULTORIA')
print(f'30% do salário: {x:.3f}')
if(value_final<x):
    print(f'Você vai pagar em {temp_mes} meses o valor mensal de {value_final:.3f} durante {temp_ano} anos. ')
else:
    print(f'Você não pode obter o imóvel pois em {temp_mes} meses teria de pagar o valor mensal de {value_final:.3f} darante {temp_ano} anos. O banco não permite devido ao seu atual saldo.')


