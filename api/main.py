from fastapi import FastAPI, Query, HTTPException
import os
import json
import re

app = FastAPI()

def sanitize_filename(filename):
    """
    Sanitizes a string to be used as a filename. Must be identical to the
    one used in the data populator script.
    """
    sanitized = re.sub(r'[\\/*?:"<>|]',"", filename)
    sanitized = sanitized.replace(" ", "_").replace("'", "_")
    return sanitized

@app.get('/api/hello')
def hello_world():
    """
    Endpoint que exibe uma mensagem de "Olá, Mundo!".
    """
    return {'message': 'Hello World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para ver os cardápios dos restaurantes.
    - Se nenhum restaurante for especificado, retorna o cardápio de todos.
    - Se um restaurante for especificado, retorna o cardápio daquele restaurante.
    - A busca por restaurante não diferencia maiúsculas de minúsculas.
    """
    data_dir = 'data'

    if restaurante is None:
        # Return all data from all restaurant files
        all_data = []
        try:
            for filename in os.listdir(data_dir):
                if filename.endswith('.json'):
                    filepath = os.path.join(data_dir, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        # To make the output cleaner, let's associate the data with the restaurant name
                        restaurant_name = filename.replace('.json', '').replace('_', ' ')
                        all_data.append({restaurant_name: json.load(f)})
            return {'Dados': all_data}
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="Diretório de dados não encontrado. Execute o script de popular dados primeiro.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro interno ao ler os dados: {e}")

    # Search for a specific restaurant (case-insensitive)
    sanitized_input = sanitize_filename(restaurante)
    try:
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                # Case-insensitive comparison
                if sanitized_input.lower() == filename.replace('.json', '').lower():
                    filepath = os.path.join(data_dir, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        return {'Restaurante': restaurante, 'Cardapio': data}
    except FileNotFoundError:
         raise HTTPException(status_code=404, detail="Diretório de dados não encontrado. Execute o script de popular dados primeiro.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno ao processar sua requisição: {e}")

    # If no match was found after checking all files
    raise HTTPException(status_code=404, detail=f"Restaurante '{restaurante}' não encontrado.")