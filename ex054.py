from  datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é maior de idade')
        totmaior +=1
    else:
        print('Essa pessoa é menor de idade')
        totmenor +=1
