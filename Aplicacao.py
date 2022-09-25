# Construir a API --> Flask
from flask import Flask, request
# Lib para Datas
from datetime import datetime
# Lib para carregar o modelo
import joblib
# Lib para banco de dados
from conexao import Conecta_db as conexao


# Instanciar o aplicativo
Aplicativo = Flask(__name__)

# --------- CARREGANDO O MODELO ---------
# Carregar Modelo
Modelo = joblib.load('modelo/Modelo_Floresta_Aleatoria_v1.pkl')

# --------- FUNÇÃO DA API ---------
# Função para receber nossa API
@Aplicativo.route('/API_Preditivo/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods=['GET'])
def Funcao_01( area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax ):				
    # Abrindo a conexao
    con = conexao()
    cursor = con.conectando_db()
    # Data e hora de inicio
    Data_Inicio = datetime.now()

    # Recebendo os inputs da API
    Lista = [
        float(area), float(rooms), float(bathroom), float(parking_spaces), 
        float(floor), float(animal), float(furniture), float(hoa), float(property_tax)
    ]

    # Tentar a previsão
    try:

        # Predict
        Previsao = Modelo.predict( [Lista] )

        # Inserir o valor da Previsão
        Lista.append( str(Previsao) )

        # Concatenado a Lista
        Input = ''
        for Valor in Lista:
            Input = Input + ';' + str(Valor)

        # Termino do processo
        Data_Fim = datetime.now()
        Processamento = Data_Fim - Data_Inicio

        # --------- CONEXÃO BANCO DE DADOS ---------
        # Criar a conexão com o banco de dados

        # Query
        Query_Inserindo_Dados = f'''
            INSERT INTO log_API ( Inputs, Inicio, Fim, Processamento )
            VALUES ( '{Input}', '{Data_Inicio}', '{Data_Fim}', '{Processamento}' )
        '''

        # Execuar a Query
        cursor.execute( Query_Inserindo_Dados )
        con.conexao_banco.commit()

        # Fechar a conexão com o banco de dados
        cursor.close()

        # Retorno do Modelo
        return {'Valor_Aluguel' : str(Previsao) }

    except:
        return {'Aviso' : 'Deu algum erro!'}

if __name__ == '__main__':
    Aplicativo.run( debug=True )
