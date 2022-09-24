import sqlite3

# Criar o banco
# Caso exista faz a conexao caso contrário ele cria
conexao_banco = sqlite3.connect('Banco_dados_API.db')

# Apontar para o banco
cursor = conexao_banco.cursor()

# Query - Criar uma tabela

Query_criar_banco = '''
CREATE TABLE log_API(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    inputs TEXT,
    inicio TEXT,
    fim TEXT,
    processamento TEXT
)
'''

# Executando a Query
cursor.execute( Query_criar_banco )
