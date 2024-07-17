'''
Consigo criar um dicionário:

dados = {'nome':'Pedro','idaade':25}
print(dados['nome']) >> Pedro



locadora = []

filme = {
    'titulo':'Star Wars',
    'ano':'1977',
    'diretor':'George Lucas'
}

#KEYS => TITULO, ANO, DIRETOR
#VALUES => STAR WARS, 1977, GEORGE LUCAS
#ITEMS => AMBOS VALORES ACIMA

print(filme['titulo'])

for k, v in filme.items(): #k -> keys and v -> values
    print(f'O {k} é {v}')

'''
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')


