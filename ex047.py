'''
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
for n in range(1,50):
    if (n%2==0):
        print(n, end=' ')
    else:
        print('')
print('Acabou!')
