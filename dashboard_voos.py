import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import psycopg2

# Conectar ao banco de dados PostgreSQL
def conectar_postgres():
    conexao = psycopg2.connect(
        host="localhost",  # Endereço do servidor
        database="voos_aeroporto",  # Nome do banco de dados
        user="postgres",  # Nome de usuário do PostgreSQL
        password="Gg84423289",  # Senha do PostgreSQL
        port="5432"  # Porta do PostgreSQL (padrão 5432)
    )
    return conexao

# Carregar os dados do PostgreSQL
def carregar_dados():
    conexao = conectar_postgres()
    consulta_sql = """
    SELECT ano, dia, janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro 
    FROM voos;
    """
    df = pd.read_sql(consulta_sql, conexao)
    conexao.close()
    return df

# Carregar os dados
df_voos = carregar_dados()

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout do Dashboard
app.layout = html.Div([
    html.H1("Dashboard Interativo de Voos - Aeroporto do Recife"),
    
    # Dropdown para selecionar o ano
    html.Label("Selecione o Ano:"),
    dcc.Dropdown(
        id='dropdown-ano',
        options=[{'label': str(ano), 'value': ano} for ano in df_voos['ano'].unique()],
        value=df_voos['ano'].min(),  # Ano inicial selecionado
        clearable=False
    ),

    # Gráfico interativo
    dcc.Graph(id='grafico-voos'),

    # Controle para alterar o tipo de gráfico
    html.Label("Selecione o Tipo de Gráfico:"),
    dcc.RadioItems(
        id='tipo-grafico',
        options=[
            {'label': 'Barras', 'value': 'bar'},
            {'label': 'Linhas', 'value': 'line'}
        ],
        value='bar',  # Tipo de gráfico inicial
        inline=True
    )
])

# Função de callback para atualizar o gráfico com base nas seleções do usuário
@app.callback(
    Output('grafico-voos', 'figure'),
    [Input('dropdown-ano', 'value'),
     Input('tipo-grafico', 'value')]
)
def atualizar_grafico(ano_selecionado, tipo_grafico):
    # Filtrar os dados pelo ano selecionado
    df_filtrado = df_voos[df_voos['ano'] == ano_selecionado]

    # Preparar os dados para o gráfico
    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    df_meses = df_filtrado[meses].sum().reset_index()
    df_meses.columns = ['Mes', 'Voos']

    # Criar o gráfico com Plotly
    if tipo_grafico == 'bar':
        fig = px.bar(df_meses, x='Mes', y='Voos', title=f'Número de Voos por Mês em {ano_selecionado}')
    else:
        fig = px.line(df_meses, x='Mes', y='Voos', title=f'Número de Voos por Mês em {ano_selecionado}')

    return fig

# Rodar o app
if __name__ == '__main__':
    app.run_server(debug=True)
