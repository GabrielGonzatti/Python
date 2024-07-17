'''
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
'''
num = int(input('Informe por favor um número? '))
c = num
fat = 1
print(f'Calculando fatorial de !{c}')
while c > 0:
    print(f'{c} X ' if c > 1 else '1 = ', end='')
    fat = fat * c
    c -= 1
print(f'{fat}')


