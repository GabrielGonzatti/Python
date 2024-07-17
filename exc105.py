'''
Faça um programa que tenha uma função notas() 
que pode receber várias notas de alunos e 
vai retornar um dicionário com as seguintes informações:
– Quantidade de notas  
– A maior nota   
– A menor nota
– A média da turma 
– A situação (opcional)
'''
def notas():
    notas = dict()
    while True:
        notas = int(input('Me informe um número: '))   
        notas['notas'] = notas
        notas['maior'] = max(notas['notas'])
        notas['menor'] = min(notas['notas'])
        
notas()
