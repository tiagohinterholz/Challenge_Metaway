import requests, obtain_token

# URL da API e Token
API_URL = "http://127.0.0.1:8000/api/clientes/"
TOKEN = obtain_token.get_token()
  # Substitua pelo token obtido

# Headers com o Token
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# Requisição GET para listar os clientes
response = requests.get(API_URL, headers=headers)
if response.status_code == 200:
    print("Clientes:", response.json())
else:
    print(f"Erro: {response.status_code}, {response.json()}")

# Requisição POST para criar um cliente
data = {
    "nome": "Novo Cliente",
    "cpf": "123.456.789-00",
    "data_de_cadastro": "2024-11-29"
}
response = requests.post(API_URL, headers=headers, json=data)
if response.status_code == 201:
    print("Cliente criado com sucesso:", response.json())
else:
    print(f"Erro ao criar cliente: {response.status_code}, {response.json()}")
