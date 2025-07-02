# Exercício 3
IA/Atividade/Atividade_pratica_06
# Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP.
# O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.​

import requests  # Importa a biblioteca para fazer requisições HTTP

def consultar_cep(cep):
    # Monta a URL da API ViaCEP com o CEP informado
    URL = f"https://viacep.com.br/ws/{cep}/json/"

    # Faz a requisição GET para a URL
    response = requests.get(URL)
    # Converte a resposta JSON em dicionário Python
    dados = response.json()

    # Verifica se a resposta contém erro (CEP inválido)
    if "erro" in dados:
        return "CEP inválido ou não encontrado."

    # Monta a string formatada com os dados do endereço
    endereco = f"""
    logradouro: {dados.get("logradouro", "N/A")}
    bairro: {dados.get("bairro", "N/A")}
    cidade: {dados.get("localidade", "N/A")}
    estado: {dados.get("uf", "N/A")}
    """

    return endereco  # Retorna os dados do endereço formatados

# Solicita ao usuário que digite o CEP, removendo traços e espaços
cep = input("Digite seu CEP (somente números): ").replace("-", "").strip()

# Chama a função para consultar o CEP informado
resultado = consultar_cep(cep)

# Exibe o resultado da consulta
print(resultado)
