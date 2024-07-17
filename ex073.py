'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''
brasileirao = ('Grêmio', 'Flamengo', 'Palmeiras', 'Corinthans', 'Inter', 'Chapecoense', 'Bahia', 'Fluminense', 'São Paulo',
               'Vitória', 'Juventude', 'Cruzeiro', 'Atletico MG', 'Atletico PR', 'Criciuma', 'Santos', 'Botafogo', 'Vasco',
               'Avaí','Ceará')
print('=---=' * 20)
print('Primeiros colocados: ')
for c in range(0,5):
    colocado = c+1
    print(f'{colocado}º colocado: {brasileirao[c]}')
print('=---=' * 20)
print('Últimos colocados:')
print(f'{brasileirao[-4:]}')
print(f'Localização da chapecoense: {brasileirao.index("Chapecoense")+1}')

