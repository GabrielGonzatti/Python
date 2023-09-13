valorSalarial = float(input('Qual o valor do salário?'))
aumento = (valorSalarial/100) * 15
salarioAtual = aumento + valorSalarial
print(f'Olá! o seu salário era de R${valorSalarial} mas após o aumento de 15% foi para R$ {salarioAtual:.3f}')
