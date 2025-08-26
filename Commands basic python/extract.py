import requests

def extract_data():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
