n1 = int(input('Olá, me informe o primeiro número por favor: '))
n2 = int(input('Olá, me informe o segundo número por favor: '))
option = 0
while option != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    option = int(input('Qual é sua opção? '))
    if option == 1:
        soma = n1 + n2
        print(f'A soma é {soma}')
    elif option == 2:
        mult = n1 * n2
        print(f'A multiplicação de {n1} X {n2} é igual a {mult}')
    elif option == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 == n2:
            print('Ambos são iguais!')
        else:
            print(f'{n2} é maior que {n1}')
    elif option == 4:
        print('Informe os novos números: ')
        n1 = int(input('Informe o primeiro valor'))
        n2 = int(input('Informe o segundo valor'))

    elif option == 5:
        print('Saindo...')
        break
    else:
        print('Ops, não consegui entender, pode repetir? ')

print('Fim do programa! Volte sempre!')

