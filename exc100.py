'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
numeros = list() #CRIANDO UMA LISTA CHAMADA NUMEROS

def sorteia(): #UMA FUNÇÃO CHAMADA SORTEIA
    from random import randint #IMPORTANDO RANDOM QUE É PARA ALEATORIZAR
    for c in range(0, 5): #PARA C DE 0 ATÉ 5
        numeros.append(randint(0, 20)) #SORTEANDO UM NÚMERO DE 1 A 10
        print(f'{c+1}º valor sorteado foi {numeros[c]}') 
        print('Fim da execução da função sorteia()') #FIM DA EXECUÇÃO DA FUNÇÃO SORTEIA
    somaPar()

def somaPar(): #UMA FUNÇÃO CHAMADA SOMAPAR
    soma = 0 #VARIÁVEL SOMA
    for c in range(0, len(numeros)): #PARA C DE 0 ATE OS NUMEROS SORTEADOS NA LISTA NUMEROS
        if numeros[c] % 2 == 0: #SE O NUMERO FOR PAR...
            soma += numeros[c] #SOMA O NUMERO
    print(f'A soma dos valores pares é {soma}') #IMPRIMINDO RESULTADO

sorteia()