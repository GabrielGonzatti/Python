r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
'Para ser formado um triângulo, nenhuma soma de dois lados, deve ser maior que o terceiro lado'
if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print('Os segmentos acima PODEM FORMAR triângulo')
    if r1 == r2 and r2 ==r3:
        print('O triângulo é Equilatero!')
    elif r1 != r2 !=r3:
        print('O triângulo é Escaleno!')
    else:
        print('O triângulo é Isóceles')
else:
    print('Os segmentos NÃO PODEM FORMAR triângulo')

