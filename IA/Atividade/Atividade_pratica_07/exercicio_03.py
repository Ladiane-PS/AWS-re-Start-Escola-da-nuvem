# Atividade 3

# Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import csv
# Importa a biblioteca csv para trabalhar com arquivos CSV.

# Define o nome do arquivo CSV que será lido
nome_arquivo = "pessoas.csv"

# Abre o arquivo 'pessoas.csv' no modo leitura ('r') com codificação UTF-8
with open(nome_arquivo, mode="r", encoding="utf-8") as file:
    # Cria um leitor de CSV que interpreta cada linha como um dicionário, usando o cabeçalho como chave
    leitor = csv.DictReader(file)
    
    # Percorre cada linha do arquivo CSV
    for linha in leitor:
        # Para cada linha, imprime os valores das colunas Nome, Idade e Cidade formatados
        print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
