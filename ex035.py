'''TRIANGULO'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
#nenhuma soma de dois segmentos deve ser maior que a outra!
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode ser formado um triângulo 📐')
else:
    print('Não pode ser formado um triângulo📐')
