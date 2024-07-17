'''
MÉDIA
'''

nota1 = float(input('Me informa sua primeira nota: '))
nota2 = float(input('Me informa sua segunda nota: '))
media = (nota1+nota2)/2

if(media==10):
    print(f'PARABÉNS!!! Você passou e tirou uma nota MÁXIMA! Média: {media}')
elif(media>=9):
    print(f'PARABÉNS!!! Você passou e tirou uma nota ALTA! Média: {media}')
elif(media>=7.0):
    print(f'ESTÁ APROVADO! Tirou uma nota maior ou igual a média. Sua média: {media}')
elif(media<6 and media>4):
    nota_faltante = 7 - media
    print(f'Faltou pouco para conseguir sua NOTA! Média {media} e faltou {nota_faltante:.2f}')
elif(media<4):
    nota_faltante = 7 - media
    print(f'ESTUDE MAIS!!! Sua nota não chegou perto de passar! Média: {media} e faltou {nota_faltante:.2f} para alcançar.')


