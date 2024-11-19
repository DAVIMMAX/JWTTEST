import requests

# URL da sua API onde a view de login está exposta
url = 'http://127.0.0.1:8000/login/'  # Altere conforme necessário

# Dados para autenticação
data = {
    'username': 'usuario_teste',
    'password': 'senha123'
}

# Enviando a requisição POST
response = requests.post(url, data=data)

# Verificando a resposta
if response.status_code == 200:
    print("Acesso concedido!")
    tokens = response.json()  # Recebe os tokens JWT
    print("Access Token:", tokens['access'])
    print("Refresh Token:", tokens['refresh'])
else:
    print(f"Erro: {response.status_code}")
    print(response.json())
