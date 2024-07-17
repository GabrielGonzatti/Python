'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
somaidade = 0
idademaior = 0
quant_mulher = 0
for pessoa in range(1,5):
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo [M -> MASCULINO | F -> FEMININO]'))
    if sexo == 'M' and idade > idademaior:
        idademaior = idade
        nome_idademaior = nome
    elif sexo == 'F' and idade < 20:
        quant_mulher =+ 1


    somaidade += idade

media = somaidade / 4
print(f'Media de idades: {media}')
print(f'Homem mais velho: {nome_idademaior} com {idademaior} anos.')
print(f'Há {quant_mulher} mulheres com menos de 20 anos.')
