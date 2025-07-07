# Atividade 4

# Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.

import json
# Importa a biblioteca json para trabalhar com arquivos JSON (leitura e escrita).

# Dados da pessoa em formato de dicionário Python
pessoa = {
    "nome": "Ladiane Santana",
    "idade": 25,
    "cidade": "Belém"
}

# Abre (ou cria) um arquivo chamado "pessoa.json" para escrita com codificação UTF-8
with open("pessoa.json", "w", encoding="utf-8") as file:
    # Salva o dicionário 'pessoa' no arquivo JSON, formatando com indentação e caracteres especiais preservados
    json.dump(pessoa, file, ensure_ascii=False, indent=4)

print("Dados salvos no arquivo 'pessoa.json'.")

# Abre o arquivo "pessoa.json" para leitura, também com codificação UTF-8
with open("pessoa.json", "r", encoding="utf-8") as file:
    # Carrega os dados do arquivo JSON para um dicionário Python chamado 'dados'
    dados = json.load(file)

# Exibe no terminal os dados lidos do arquivo JSON
print("Dados lidos do arquivo JSON:")
print(f"Nome: {dados['nome']}")
print(f"Idade: {dados['idade']}")
print(f"Cidade: {dados['cidade']}")
