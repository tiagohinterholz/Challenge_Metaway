import requests

def get_token():
    TOKEN_URL = "http://127.0.0.1:8000/api"
    CREDENTIALS = {"username": "seu_usuario", "password": "sua_senha"}

    response = requests.post(TOKEN_URL, data=CREDENTIALS)
    if response.status_code == 200:
        return response.json().get("access")
    else:
        print(f"Erro ao obter token: {response.status_code}, {response.json()}")
        exit()

if __name__ == "__main__":
    get_token()
