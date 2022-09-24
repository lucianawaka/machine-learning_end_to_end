# Construir API -- Flask
from flask import Flask, request

# Instanciar o aplicativo
Aplicativo = Flask(__name__)

# Função para receber nossa API
@Aplicativo.route('/API_Preditivo/<Parametro1>', methods=['GET'])

def Funcao_01( Parametro1 ):
    return {'Retorno': f'{Parametro1}'}

if __name__ == '__main__':
    Aplicativo.run( debug=True )
