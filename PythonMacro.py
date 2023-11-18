import keyboard
import sys

# Dicionário para armazenar atalhos e textos associados
macros = {}

option = ""

#menu do programa:
def menu():
    option = " "
    print("Bem-vindo à sua MacroPython! \nProgramado por Gonzatti & Max")
    index = 0
    while(option != "#"):

        if(index > 0):
            res = input("Você quer adicionar uma nova Macro? SIM para adicionar uma nova | NAO para salvar e sair \n")
            if(res != "SIM"):
                print ("Sistema dormindo, nenhuma funcionalidade irá funcionar, ESC para acordá-lo!")
                keyboard.wait("esc")
                index= 0
                menu()
        option = input("Olá quer adicionar uma nova Macro? Digite a opção 1 para adicionar uma nova Macro ou # para sair: ")
        if(option == "1"):
            adicionar_macro()
            exit
        elif(option == "#"):
            sys.exit(0)

        index = index+1

#Função para adicionar uma nova macro
def adicionar_macro():
    atalho = input("Digite o atalho desejado: ")
    texto = input(f"Digite o texto associado ao atalho '{atalho}': ")
    macros[atalho] = texto
    print(f"Macro '{atalho}' Macro sendo salva!")
    keyboard.add_abbreviation("@" + atalho, texto)

menu()
