from random import randint

lista = list()
jogos = list()

print('-'*30)
print(' JOGA NA MEGA SENA')
print('-'*30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))

tot = 1
while tot <= quant:
    cont = 0
    while True: #ENQUANTO FOR VERDADEIRA
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort() #DEIXANDO EM ORDEM CRESCENTE
    jogos.append(lista[:]) #CRIANDO UMA CÓPIA PARA LIMPAR LISTA ANTERIOR
    lista.clear()
    tot +=1
print(f'Os números sorteados foram {jogos}')
