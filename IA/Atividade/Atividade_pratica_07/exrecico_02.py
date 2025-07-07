
# Atividade 2

# Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import csv
# Importa a biblioteca csv.
# Lista de dicionários com informações das pessoas (Nome, Idade e Cidade)
pessoas = [
    {"Nome": "Ladiane", "Idade": 25, "Cidade": "Belém"},
    {"Nome": "João", "Idade": 30, "Cidade": "São Paulo"},
    {"Nome": "Maria", "Idade": 28, "Cidade": "Fortaleza"},
]

# Define o nome do arquivo CSV que será criado
nome_arquivo = "pessoas.csv"

# Abre (ou cria) o arquivo 'pessoas.csv' para escrita ('w') com codificação UTF-8
# 'newline=""' evita linhas em branco extras no Windows
with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as file:
    # Define as colunas do arquivo CSV
    campos = ["Nome", "Idade", "Cidade"]
    # Cria um objeto escritor que escreve dicionários no arquivo CSV, usando as colunas definidas
    writer = csv.DictWriter(file, fieldnames=campos)
    
    # Escreve o cabeçalho (nomes das colunas) no arquivo CSV
    writer.writeheader()
    # Para cada pessoa na lista, escreve uma linha com seus dados no arquivo
    for pessoa in pessoas:
        writer.writerow(pessoa)

# Confirmação de que o arquivo foi criado
print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
