import requests

# Local da URL
url = 'http://127.0.0.1:5000/API_Preditivo'

consulta = requests.get( url )

res = consulta.json()
print(res)
