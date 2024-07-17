temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('=-' *30)
print(f'Os dados foram {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O maior peso foi {maior} e o menor peso foi {menor}')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')
