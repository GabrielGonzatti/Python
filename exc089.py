ficha = []

while True:
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) #NOME POSICAO 0 | NOTAS NA POSICAO 1 | MEDIA NA POSICAO 2
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp in 'N':
        break
print('-'*26)
print(f'{"Nº.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
    print('.'*16)
