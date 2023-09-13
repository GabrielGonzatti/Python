dias = float(input('Quantos dias você andou com o carro?'))
valordiario = dias * 60
km = float(input('Quantos km você andou com o carro?'))
valorkm = km * 0.15
soma = valorkm + valordiario
print(f'Olá! como você andou {dias} dias com o carro e {km} km, o valor para pagar pelo aluguel é de {soma}')
