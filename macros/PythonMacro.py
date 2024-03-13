from functools import partial
import customtkinter
from customtkinter import *
import tkinter
from tkinter import messagebox
from tkinter import Frame
import keyboard
import json

# Função para atualizar os atalhos e textos associados
macros = {}
option = ""

def main():
    def delete_macro(key):
        print(key)
        
            
    def atualizar_macros():
        print("Atualizando macros...")
        try:
            # Serializando o objeto JSON
            json_object = json.dumps(binds, indent=4)
            with open("binds.json", "w") as outfile:
                outfile.write(json_object)
            
            # Adicionar novos atalhos
            for bind in binds["binds"]:
                for key, value in bind.items():
                    keyboard.add_abbreviation(key, value)
            
            update_labels()
            print("Macros atualizadas...")
        except Exception as e:
            print("Ocorreu um erro na atualização:", e)

    # Função para adicionar uma nova macro
    def adicionar_macro():
        atalho = atalho_entry.get()
        texto = texto_entry.get()
        if atalho and texto:
            macros[atalho] = texto
            binds["binds"].append({"@" + atalho: texto})
            print(f"Macro '{atalho}' sendo salva!")
            atualizar_macros()
            messagebox.showinfo("Sucesso", f"Macro '{atalho}' adicionada com sucesso!")
            texto_entry.delete(0, tkinter.END)
            texto_entry.insert(0, "")
            atalho_entry.delete(0, tkinter.END)
            atalho_entry.insert(0, "")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    # Função para atualizar as labels
    def update_labels():
        # Limpa as labels existentes
        for widget in left_frame.winfo_children():
            widget.destroy()

        # Cria novas labels com base nas binds atualizadas
        for bind in binds["binds"]:
            for key, value in bind.items():
                bold_font = customtkinter.CTkFont(weight="bold")
                frame = customtkinter.CTkFrame(left_frame)
                frame.pack(pady=5, anchor="w")  # Adicionando um pouco de espaçamento entre cada par de atalho e texto

                atalho_label = customtkinter.CTkLabel(frame, text=key, fg_color="#026ec1",corner_radius=6, text_color="#1f1f1f", font=bold_font)
                atalho_label.pack(side="left",padx=2,pady=5)

                texto_label = customtkinter.CTkLabel(frame, text=f"Texto: {value[:50]}...", fg_color="#444444",corner_radius=6)
                texto_label.pack(side="left",padx=2,pady=5)
                
                btn = customtkinter.CTkButton(frame, text="Edit", command=partial(delete_macro, key))
                btn.pack(side="right",padx=0,pady=0)

    # Criar ou carregar o arquivo de binds
    try:
        with open("binds.json") as file:
            binds = json.load(file)
        atualizar_macros()
    except FileNotFoundError:
        binds = {"binds": []}
        print("Criamos o arquivo para você!")

    # Configuração da interface gráfica
    customtkinter.set_appearance_mode("Dark")
    root = customtkinter.CTk()
    root.title("Macros - Renner")
    root.geometry("800x400")

    # Define o tamanho máximo e mínimo da janela
    root.minsize(width=1200, height=800)

    # Widgets
    frame = customtkinter.CTkFrame(root, width=350, height=350,)
    left_frame = customtkinter.CTkScrollableFrame(root, width=600, height=450)

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    left_frame.grid(row=0, column=0, padx=20, pady=20)
    frame.grid(row=0, column=1, padx=20, pady=20,sticky="n")

    customtkinter.CTkLabel(frame, text="Atalho:").pack()
    atalho_entry = customtkinter.CTkEntry(frame, height=30, width=150)
    atalho_entry.pack(padx=15, pady=15)

    customtkinter.CTkLabel(frame, text="Texto:").pack()
    texto_entry = customtkinter.CTkEntry(frame, height=30, width=150)
    texto_entry.pack(padx=15, pady=15)

    adicionar_button = customtkinter.CTkButton(frame, text="Adicionar Macro", command=adicionar_macro)
    adicionar_button.pack(padx=15, pady=15)

    customtkinter.CTkLabel(left_frame, text="Lista de atalhos").pack(side="top")

    # Atualiza as labels pela primeira vez
    update_labels()

    # Rodar a aplicação
    root.mainloop()

if __name__ == "__main__":
    main()
