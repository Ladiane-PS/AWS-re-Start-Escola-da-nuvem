# Exercício 4

# Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).
# O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual,
# máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.​

import requests  # Para fazer requisições HTTP

def consultar_cotacao(moeda):
    # API da AwesomeAPI para cotação BRL x moeda informada
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    response = requests.get(url)  # Requisição GET
    dados = response.json()       # Converte resposta em dicionário

    # A chave esperada é, por exemplo, 'USD' + 'BRL' = 'USDBRL'
    chave = f"{moeda}BRL"

    # Verifica se a chave existe no resultado (moeda válida)
    if chave not in dados:
        return "Código de moeda inválido ou não suportado."

    cotacao = dados[chave]

    # Monta a string com as informações pedidas
    resultado = f"""
    Moeda: {moeda}
    Valor atual: R$ {cotacao['bid']}
    Valor máximo do dia: R$ {cotacao['high']}
    Valor mínimo do dia: R$ {cotacao['low']}
    Última atualização: {cotacao['create_date']}
    """

    return resultado

# Solicita o código da moeda ao usuário (exemplo: USD, EUR, GBP)
codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()

# Chama a função para consultar a cotação
resultado_cotacao = consultar_cotacao(codigo_moeda)

# Exibe o resultado na tela
print(resultado_cotacao)
