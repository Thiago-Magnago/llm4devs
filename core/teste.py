import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Defina sua chave secreta pessoal
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    'Authorization': f'Bearer {api_key}'
}

#'petrobras-ca-root.pem'

# Endpoint para listar os modelos
url = "https://api.openai.com/v1/models"

response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    models = response.json()['data']
    for model in models:
        print(model['id'])
else:
    print(f"Failed to fetch models: {response.status_code} - {response.text}")
