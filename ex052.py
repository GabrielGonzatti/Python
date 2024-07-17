num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot = tot+1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')

if tot == 2:
    print(f'\n Foi encontrado {tot} números primos! Em um total de {c} números!')
else:
    print(f'\n Não foi encontrado números primos! Mas há {tot} números que podem ser divididos, em um total de {c} números!')



