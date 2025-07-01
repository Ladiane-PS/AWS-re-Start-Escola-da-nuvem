from datetime import date

def idade_em_dias_completa(ano, mes, dia):
    nascimento = date(ano, mes, dia)
    hoje = date.today()
    diferenca = hoje - nascimento
    return diferenca.days

# Exemplo de uso:
dias = idade_em_dias_completa(2000, 2, 29)  # exemplo com ano bissexto
print(f"Idade exata em dias: {dias} dias")
