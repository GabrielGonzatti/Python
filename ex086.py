matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]] #uma LISTA como uma MATRIZ, onde dentro da lista, há outras 3 listas, cada outra, com 3 valores;
for l in range(0,3): #entra em cada lista interna
    for c in range(0, 3): #entra em cada valor interno da lista interna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) #apenas um modo para adicionar valores
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]}:^5', end=' ')
    print()
