'''
Conversor de Bases Numéricas

'''

NUM = int(input('Digite um número: '))

RESP = int(input('Faça uma escolha para conversão: \n [ 1 ] Converter para BINÁRIO \n [ 2 ] Converter para OCTAL \n [ 3 ] Converter para Hexadecimal \n Sua opção:'))

if(RESP == 1):
    print('{} convertido para BINÁRIO é igual a {}'.format(NUM, bin(NUM)))
elif(RESP == 2):
    print('{} convertido para OCTAL é igual a {}'.format(NUM, oct(NUM)))
elif(RESP == 3):
    print('{} convertido para OCTAL é igual a {}'.format(NUM, hex(NUM)))
else:
    print('[opção incorreta!] Digite 1, 2 ou 3 como escolha!')
