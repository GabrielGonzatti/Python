resposta = str(input('Me informe seu sexo por favor: ')).strip().upper()[0]
while resposta not in 'MmFf':
    resposta = str(input('Dados inválidos. Me informe seu sexo por favor: ')).strip().upper()[0]
if (resposta == 'M'):
    print(f'Sexo Masculino registrado com sucesso!')
else:
    print(f'Sexo Feminino registrado com sucesso!')

