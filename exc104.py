'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
'''
def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido')
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar o valor')
        else:
            print(f'Você digitou o número {n}')
            break

n = leiaInt()