# Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes. 

# atividade_01.py
import pandas as pd

# Leitura do arquivo de log (coluna: tempo_execucao)
df = pd.read_csv("log.csv")

# Cálculo da média e do desvio padrão
media = df["tempo_execucao"].mean()
desvio = df["tempo_execucao"].std()

# Exibição dos resultados
print(f"Média do tempo de execução: {media:.2f} segundos")
print(f"Desvio padrão do tempo de execução: {desvio:.2f} segundos")
