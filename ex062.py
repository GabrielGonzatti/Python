print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
resposta = 1
num_ate = 10
while resposta != 0:
    while cont <= num_ate:
        print('{} ->'.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    resposta = int(input('Você gostaria de ver mais quantas razões? '))
    if resposta != 0:
        print('Você escolheu repetir, um momento...')
        num_ate = resposta
        cont = 1
    else:
        print('FIM')
        break
