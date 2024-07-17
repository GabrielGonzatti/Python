'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Qual seu ano de nascimento? '))
idade = ano_atual-ano_nasc
if(idade>25):
    print('Atleta Master!')
elif(idade>19 and idade<=25):
    print('Atleta Sênior')
elif(idade<=19 and idade >14):
    print('Atleta Junior')
elif(idade<=14 and idade>9):
    print('Atleta infantil')
else:
    print('MIRIM')

