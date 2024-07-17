'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

#ler o nome do produto --> produto_name | produto_price --> Preço do produto
produtos_maisMil = 0
produtos_gasto = 0
produto_mais_caro = 0
produto_mais_barato = 0

while True:
    produto_name = str(input("Qual o nome deste produto? ")).upper()
    produto_price = int(input("Qual o preço deste produto? "))
    if produto_mais_barato == 0:
        produto_mais_barato = produto_price

    produtos_gasto = produtos_gasto + produto_price

    if produto_price > 1000:
        produtos_maisMil = produtos_maisMil + 1
    if produto_price > produto_mais_caro:
        produto_mais_caro = produto_price
    if produto_price < produto_mais_barato:
        produto_mais_barato = produto_name

    escolha = str(input('Você deseja continuar? [S] para sim & [N] para não: ')).upper()

    if escolha == 'N':
        print(f'Aqui estão os resultados da pesquisa: \n {produtos_gasto}R$ | Total de compras mais que mil: {produtos_maisMil} | A compra mais barata: {produto_mais_barato}')
        break
    else:
        continue
