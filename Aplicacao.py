# Construir API -- Flask
from flask import Flask, request
import joblib

# Instanciar o aplicativo
Aplicativo = Flask(__name__)

# Carregar o modelo treinado
modelo = joblib.load('modelo/Modelo_Floresta_Aleatoria_v1.pkl')

# Função para receber nossa API
@Aplicativo.route('/API_Preditivo/<area>;<rooms>;<bathroom>;<parking spaces>;<floor>;<animal>;<furniture>;<hoa (R$)>;<property tax (R$)>', methods=['GET'])
 
def Funcao_01( Parametro1 ):
    """ 
    Função pega os dados da url e faz as previsões
    params = parâmetros passados na url
    modelo.predict(params)
    return o valor da previsão 
    """
    try:
            previsao = modelo.predict()
            return {'Valor_Aluguel' : previsao }
    except:
            return {'Aviso' : 'Ocorreu um erro! Passe os parâmetros <area>;<rooms>;<bathroom>;<parking spaces>;<floor>;<animal>;<furniture>;<hoa (R$)>;<property tax (R$)>'}
    

if __name__ == '__main__':
    Aplicativo.run( debug=True )
