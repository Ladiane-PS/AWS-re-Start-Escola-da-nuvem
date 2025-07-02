# Atividade 3

# Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.


import datetime

def idade_em_dias(ano_nascimento, mes_nascimento=1, dia_nascimento=1):
    # Data de nascimento
    data_nasc = datetime.date(ano_nascimento, mes_nascimento, dia_nascimento)
    # Data atual
    hoje = datetime.date.today()
    # Diferença em dias entre hoje e nascimento
    idade_dias = (hoje - data_nasc).days
    return idade_dias

# Exemplo: nasceu em 15/04/2000
resultado = idade_em_dias(2000, 4, 15)

print(f"Idade em dias: {resultado}")

