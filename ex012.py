valorproduto = float(input('Qual o valor do produto?'))
desconto5 = (valorproduto/100) * 5
valoratual = (valorproduto-desconto5)
print(f'O produto que inicialmente custava {valorproduto}R$, agora com o desconto de 5% irá custar R${valoratual}')
