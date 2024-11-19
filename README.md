Testar o código com o Request:

#request.py:

import requests

# URL da sua API onde a view de login está exposta
url = 'http://127.0.0.1:8000/login/'  

data = {
    'username': 'usuario_teste',
    'password': 'senha123'
}


response = requests.post(url, data=data)


if response.status_code == 200:
    print("Acesso concedido!")
    tokens = response.json() 
    print("Access Token:", tokens['access'])
    print("Refresh Token:", tokens['refresh'])
else:
    print(f"Erro: {response.status_code}")
    print(response.json())
