import requests
import json
import os
import re

def sanitize_filename(filename):
    """
    Sanitizes a string to be used as a filename by removing or replacing
    invalid characters.
    """
    # Replace spaces and apostrophes (standard and smart) with underscores
    filename = filename.replace(" ", "_").replace("'", "_").replace("’", "_")
    # Remove any remaining invalid characters
    sanitized = re.sub(r'[\\/*?:"<>|]',"", filename)
    return sanitized

def populate_data():
    """
    Fetches restaurant data from an API, processes it, and saves it into
    individual JSON files in the 'data/' directory.
    """
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    try:
        response = requests.get(url, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error making request to API: {e}")
        return

    try:
        dados_json = response.json()
    except json.JSONDecodeError:
        print("Error decoding JSON from API response.")
        return

    dados_restaurante = {}
    for item in dados_json:
        # Basic data validation
        if 'Company' not in item or 'Item' not in item:
            print(f"Skipping item due to missing expected keys: {item}")
            continue

        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item.get('Item'),
            "price": item.get('price'),
            "description": item.get('description')
        })

    # Ensure the data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    for nome_do_restaurante, dados in dados_restaurante.items():
        # Sanitize the filename and create the full path
        nome_do_arquivo_sanitizado = sanitize_filename(nome_do_restaurante)
        caminho_arquivo = os.path.join('data', f'{nome_do_arquivo_sanitizado}.json')

        try:
            # Use utf-8 encoding to support special characters in the content
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_restaurante:
                json.dump(dados, arquivo_restaurante, indent=4, ensure_ascii=False)
            print(f"Data for restaurant '{nome_do_restaurante}' saved to '{caminho_arquivo}'")
        except IOError as e:
            print(f"Error saving file for restaurant '{nome_do_restaurante}': {e}")

if __name__ == "__main__":
    populate_data()