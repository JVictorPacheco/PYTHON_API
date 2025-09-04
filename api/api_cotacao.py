import requests
import json


url = 'https://economia.awesomeapi.com.br/last/USD-BRL'



response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    cotacao_atual = float(data['USDBRL']['bid'])
    mensagem = f'U$ 1 dólar corresponde a R$ {cotacao_atual}'
    print(mensagem)
else:
    print(f'A requisição falhou com o código de status {response.status_code}')
    
    
    