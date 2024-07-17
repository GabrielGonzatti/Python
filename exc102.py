'''
 Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
 o primeiro que indique o número a calcular e outro chamado show, 
 que será um valor lógico (opcional) indicando se será mostrado ou 
 não na tela o processo de cálculo do fatorial.
'''
def fatorial(n, show=False):
    f = 1 
    for c in range(n, 0, -1):
        if show == True:
            if c > 1:
                print(c, end=' ')
                print('x', end=' ')
            else: 
                print('=', end=' ')
                print(f' = {f}') 
            f *= c
        else:
            f *= c
            return ('Você escolheu não mostrar o cálculo. Resultado: {f}')

resposta = fatorial(10, False)
print(resposta)
