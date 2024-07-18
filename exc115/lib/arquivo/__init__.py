from lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # R -> READ || T -> TEXT 
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # W -> WRITE || T -> TEXT || + -> CRIA SE NÃO EXISTE
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
def lerArquivo(nome):
    try:
        a = open(nome, 'rt') # R -> READ || T -> TEXT
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';') # Separa os dados por ponto e vírgula
            dado[1] = dado[1].replace('\n','')
            print(f'Nome: {dado[0]:<30}| Idade: {dado[1]:>3}')
def cadastrarPessoa(nome, nomePessoa='desconhecido', idade=0):
    try:
        a = open(nome, 'at') # A -> APPEND || T -> Text
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        a.write(f'{nomePessoa};{idade}\n')
        a.close()
        print(f'{nomePessoa} foi cadastrado com sucesso!')
