'''
Qual número é maior?
'''

num1 = int(input('Me informe o primeiro número: '))
num2 = int(input('Me informe o segundo número: '))

if(num1>num2):
    print(f'Número {num1} é maior que o número {num2}!')
elif(num1==num2):
    [print(f'Números {num1} e {num2} são iguais!')]
else:
    print(f'Número {num2} é maior que o número {num1}')
