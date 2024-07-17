listanum = []
mai = 0
men = 0
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
        #deixando como padrão par pegar o valor inicial quando não houver nenhum salvo
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'Voce digitou os valores {listanum}. ')
print(f'O maior número foi {mai} na posição...')
for indice, valor in enumerate(listanum):
    if valor == mai:
        print(f'{indice}...', end='')

print(f'O menor número foi {men} na posição...')
for indice, valor in enumerate(listanum):
    if valor == men:
        print(f'{indice}...', end='')

