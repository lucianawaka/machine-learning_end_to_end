import sqlite3


class Conecta_db():
    
    def __init__(self):
        self.conexao_banco = sqlite3.connect('Banco_dados_API.db')
    
    def conectando_db(self):
        # Criar o banco
        # Caso exista faz a conexao caso contrário ele cria

        # Apontar para o banco
        cursor = self.conexao_banco.cursor()
        
        return cursor