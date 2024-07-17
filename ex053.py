frase = str(input('Digite uma frase para validar se seria um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'É igual {inverso} | {junto}')
else:
    print(f'Diferente {inverso} | {junto}')
