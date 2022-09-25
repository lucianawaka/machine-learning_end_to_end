from conexao import Conecta_db as conexao

# Apontar para o banco
con = conexao()
cursor = con.conectando_db()

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
# cursor.execute( Query_criar_banco )

# Query de consulta

Query_consulta = '''
SELECT * FROM log_API
'''

# Executando a Query
print(cursor.execute( Query_consulta ).fetchall())

# Query de insert

Query_insert = '''
INSERT INTO log_API ( inputs, inicio, fim, processamento)
VALUES ('25;1;1;0;0;0;0;0;84', '01/01/2022 19:01', '01/01/2022', '00:01' )

'''
cursor.execute( Query_insert )

# Commit para inserir as informações no banco de dados
#con.conexao_banco.commit()
cursor.close()