'''
EX034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%
Para os inferiores, o aumento é 15%
'''
#input --> salario(int)
#se salario > 1.250,00 +10% aumento se não, 15% aumento;

salario = float(input('Qual é o seu salário? Obs.: informe conforme seguinte regra: 101.000 ou 1.500 por exemplo. '))

if salario>=1.25000:
    newSalario = salario + (salario*10/100)
else:
    newSalario = salario + (salario*15/100)

print('Seu novo salário é {:.2f}, meus parabéns!'.format(newSalario))
