nome = input('Qual seu nome?')
num = int(input(f'{nome}, Escolha um número para eu mostrar a tabuada:'))
print (f'{nome}, a tabuada de {num} é: ')
print('------------')
for c in range(1, 11):
    tab = num * c
    print(f'{num} * {c} = {tab}')
    print('------------')


