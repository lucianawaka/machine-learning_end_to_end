# Construir API -- Flask
from flask import Flask, request
import joblib

# Instanciar o aplicativo
Aplicativo = Flask(__name__)

# Carregar o modelo treinado
modelo = joblib.load('modelo/Modelo_Floresta_Aleatoria_v1.pkl')

# Função para receber nossa API
@Aplicativo.route('/API_Preditivo/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods=['GET'])
#@Aplicativo.route('/API_Preditivo', methods=['GET'])
#def Funcao_01( area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax ):
def Funcao_01( area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax ):
    """ 
    Função pega os dados da url e faz as previsões
    inputs = parâmetros passados na url
    modelo.predict(params)
    return o valor da previsão 
    """
    Lista = [
        float(area), float(rooms), float(bathroom), float(parking_spaces), 
        float(floor), float(animal), float(furniture), float(hoa), float(property_tax)
    ]
    
    try:
        previsao = modelo.predict( [Lista] )
        return {'Valor_Aluguel' : str(previsao) }
    except:
            return {'Aviso' : 'Ocorreu um erro! Passe os parâmetros <area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>>'}
    

if __name__ == '__main__':
    Aplicativo.run( debug=True )
