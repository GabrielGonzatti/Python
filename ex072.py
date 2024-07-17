cont = ('zero','um','dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze',
        'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20:'))
    if 0 <= num <=20:
        print('Tente de novo...')
        break
    resposta = str(input('Voce quer continuar? [S] para sim ou [N] para não').strip().upper())
    if resposta == 'N':
        print('Volte sempre!')
        break
print(f'Voce digitou o número {cont[num]}')
