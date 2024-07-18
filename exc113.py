'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
        except (KeyboardInterrupt):
            print('\033[31mERRO: usuário interrompeu a execução do programa\033[m')
        else:
            return n,
        finally:
            print('Acabamos! 👻') #SEMPRE EXECUTA
def leiaFloat():
    while True:
        try: #TENTAR FAZER OPERAÇÃO
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError): #ERRO DE VALOR OU TIPO
            print('\033[31mERRO: por favor, digite um número real válido\033[m')
        except (KeyboardInterrupt): #USUÁRIO INTERROMPE O PROGRAMA
            print('\033[31mERRO: usuário interrompeu a execução do programa\033[m')
        else: #SE NÃO TIVER ERRO: 
            return n
        finally:
            print('Acabamos! 👻') #SEMPRE EXECUTA

n = leiaInt()
print(f'Você digitou o número {n}')
n = leiaFloat()
print(f'Você digitou o número {n}')
                    