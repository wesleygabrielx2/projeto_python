# AeroDados - Painel Interativo de Voos

## Descrição do Projeto

O **AeroDados** é um painel interativo desenvolvido com a biblioteca Dash que permite a visualização e análise de dados sobre voos em um aeroporto. Ele oferece funcionalidades como:

- Filtros para visualização por ano, mês e dia.
- Gráficos interativos em formato de barras e linhas.
- Conexão com um banco de dados PostgreSQL para dados atualizados.

## Funcionalidades

- **Filtros Interativos**:
  - Visualização por mês ou dia.
  - Escolha de ano e mês para análise.
  - Seleção entre gráficos de barras ou linhas.
- **Conexão com Banco de Dados**:
  - Dados carregados diretamente do PostgreSQL.
- **Interface Responsiva e Moderna**:
  - Uso do Bootstrap para um design estilizado.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.8+
- **Bibliotecas**:
  - `dash` e `dash-bootstrap-components` para a interface.
  - `plotly.express` para gráficos.
  - `pandas` para manipulação de dados.
  - `psycopg2` para conexão ao banco de dados.
- **Banco de Dados**: PostgreSQL.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

1. **Python 3.8 ou superior** instalado (verifique com `python --version`).
2. **PostgreSQL** configurado e rodando.

## Dependências

As seguintes bibliotecas Python devem ser instaladas. Use o comando abaixo para instalá-las:

`pip install dash dash-bootstrap-components pandas plotly psycopg2`

## Configuração do Banco de Dados

1. **Crie um banco de dados chamado `voos_aeroporto` no PostgreSQL.**

2. **Crie a tabela `voos` com o seguinte comando SQL:**
   ```sql
   CREATE TABLE voos (
       ano INT,
       dia INT,
       janeiro INT,
       fevereiro INT,
       marco INT,
       abril INT,
       maio INT,
       junho INT,
       julho INT,
       agosto INT,
       setembro INT,
       outubro INT,
       novembro INT,
       dezembro INT
   );

## Insira os dados necessários na tabela voos.

## Configure suas credenciais no arquivo dashboard.py, na função conectar_postgres:
~~~python
  def conectar_postgres():
    conexao = psycopg2.connect(
        host="localhost",
        database="voos_aeroporto",
        user="postgres",  
        password="SUA_SENHA_AQUI",  
        port="5432"
    )
    return conexao;
  ~~~
## Como Rodar o Projeto
Execute o arquivo ```dashboard.py```

### Acesse o painel no navegador, no endereço:
```http://127.0.0.1:8050/```
