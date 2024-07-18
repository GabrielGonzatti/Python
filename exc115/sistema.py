from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        #opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarPessoa(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        cabeçalho('\033[31m[ERRO] Opção inválida. Tente novamente!\33[m')
        