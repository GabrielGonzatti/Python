'''
    TUPLAS

Variável -> Lanche
Uma variável se torna um espaço na memória, podendo atribuir valores a ela.

Lanche = Hamburger
Lanche = Bebida
Obs.: Neste caso, Lanche tem o valor substituído de Hamburger por Bebida!


'''
#tupla: lanche = ()
#Lista lanche = []
#Dicionário lanche = {}

lanche = ('Hambúrger🍔', 'Suco🍹', 'Pizza🍕', 'Pudim🍮', 'Batata Frita🍟')
for comida in lanche:
    print(f'Eu vou me alimentar de {comida}')
    print(sorted(lanche))
print('Comi bastante!')
