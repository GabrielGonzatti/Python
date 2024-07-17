import pandas as pd
import os

# Função para contar as macros em um único arquivo
def contar_macros(file_path):
    # Leitura do arquivo Excel
    df = pd.read_excel(file_path)

    # Contar a quantidade de vezes que cada macro foi acionada
    macro_count = df['Macro'].value_counts()

    return macro_count

# Diretório contendo os arquivos .xlsx
diretorio = 'caminho/para/seus/arquivos'

# Dicionário para armazenar a contagem total de cada macro
total_macro_count = {}

# Loop através de todos os arquivos .xlsx no diretório
for file_name in os.listdir(diretorio):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(diretorio, file_name)
        macro_count = contar_macros(file_path)

        # Atualizar a contagem total de cada macro
        for macro, count in macro_count.items():
            if macro in total_macro_count:
                total_macro_count[macro] += count
            else:
                total_macro_count[macro] = count

# Exibir a contagem total de cada macro
for macro, count in total_macro_count.items():
    print(f'Macro: {macro}, Contagem: {count}')
