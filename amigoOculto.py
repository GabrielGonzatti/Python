import keyboard
import sys

# Dicionário para armazenar atalhos e textos associados
macros = {}
option = ""

# menu do programa:
def menu():
    option = ""
    print("Bem-vindo à sua MacroPython! \nProgramado por Gonzatti & Max")
    index = 0
    while (option != "2"):
        #caso o index não for maior que zero, executa:
        option = input("Olá quer adicionar uma nova Macro? Digite a opção 1 para adicionar uma nova Macro ou 2 para sair: ")
        if (option == "1"):
            adicionar_macro()
            exit
        elif (option == "2"):
            print("Sistema dormindo, nenhuma funcionalidade irá funcionar, ESC para acordá-lo!")
            keyboard.wait("esc")
            #sistema aguardando ESC, em caso de ESC, executa:
            index = 0
            menu()

        index = index+1

# Função para adicionar uma nova macro
def adicionar_macro():
    atalho = input("Digite o atalho desejado: ")
    texto = input(f"Digite o texto associado ao atalho '{atalho}': ")
    macros[atalho] = texto
    print(f"Macro '{atalho}' Macro sendo salva!")
    keyboard.add_abbreviation("@" + atalho, texto)

#chamando a função
menu()
