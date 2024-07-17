'''
Um programa que pergunte apenas o ano de nascimento e consiga distinguir pelo ano atual a idade e tempo faltante para alistamento.

ano_nasc -> ano de nascimento
ano_atual -> ano atual
idade -> ano_atual - ano_nasc

se idade = 18 {
alistar
} elif > 18{
DEVERIA ter se alistado
}
else {
anos_faltante = 18 - iadde
}

'''
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Qual seu ano de nascimento? '))
idade = ano_atual-ano_nasc
if(idade==18):
    print(f'Sua idade é de {idade} anos e deve se ALISTAR!')
elif(idade>18):
    ano_alist = idade - 18
    ano_passado = ano_atual - ano_alist
    print(f'Sua idade é de {idade} anos e Deveria/Deve ter se alistado a {ano_alist} anos. No ano de {ano_passado}')
elif(idade<18):
    ano_alist = 18 - idade
    ano_futuro = ano_atual + ano_alist
    print(f'Sua idade é de {idade} anos e Deverá se alistar em {ano_alist} anos, que será no Ano {ano_futuro} ')
