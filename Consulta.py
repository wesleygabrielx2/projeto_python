import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conexão com o banco de dados PostgreSQL
conexao = psycopg2.connect(
    host="localhost",       # Endereço do servidor
    database="voos_aeroporto",  # Nome do banco de dados
    user="postgres",     # Nome de usuário do PostgreSQL
    password="Gg84423289",   # Senha do PostgreSQL
    port="5432"             # Porta do PostgreSQL (padrão 5432)
)

# Consulta SQL para buscar os dados
consulta_sql = """
SELECT dia, janeiro, fevereiro, marco 
FROM voos
WHERE ano = 2023;
"""

# Carregar os dados em um DataFrame usando Pandas
df = pd.read_sql(consulta_sql, conexao)

# Fechar a conexão com o banco de dados
conexao.close()

# Exibir as primeiras linhas dos dados
print(df.head())

# Gerar um gráfico de barras para o número de voos em janeiro de 2023
plt.figure(figsize=(10, 6))
sns.barplot(x='dia', y='janeiro', data=df)
plt.title('Número de Voos em Janeiro de 2023 por Dia')
plt.xlabel('Dia')
plt.ylabel('Voos em Janeiro')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gerar gráfico de linhas comparando janeiro, fevereiro e março
plt.figure(figsize=(10, 6))
plt.plot(df['dia'], df['janeiro'], label='Janeiro')
plt.plot(df['dia'], df['fevereiro'], label='Fevereiro')
plt.plot(df['dia'], df['marco'], label='Março')
plt.title('Comparação de Voos em 2023 (Janeiro, Fevereiro e Março)')
plt.xlabel('Dia')
plt.ylabel('Número de Voos')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
