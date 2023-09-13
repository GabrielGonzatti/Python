nome = input('Qual seu nome?')
nota1 = float(input('Olá {}, me informe sua nota no primeiro semestre?'.format(nome)))
nota2 = float(input('Olá {}, me informe sua nota no segundo semestre?'.format(nome)))
media = (nota1+nota2)/2
#não esquecer de deixar entre parenteses a soma para ela ganhar prioridade
print(f'A média da sua nota {nome} foi de {media}')
