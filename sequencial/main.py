import json
import requests
import time
import pandas as pd

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"-5.79448, -35.211"}

headers = {
        "X-RapidAPI-Key": "25f9949691msh37eee1b08b2ee1fp13101ajsn226f51c3e1a4",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

cenarios = [10, 50, 100, 200, 500, 1000]

dados = {'num_execucao':[], 'n':[], 'tempo':[]}

for c in cenarios:
    N = c
    print(N)
    for v in range(20):
        dados['num_execucao'].append(v+1)
        dados['n'].append(N)
        inicial = time.time()
        for i in range(N):
            response = requests.request("GET", url, headers=headers, params=querystring)
            json_obj = json.loads(response.text)
            print("Temperatura atual é de {}ºC e a sensação térmica é de {}ºC.".format(json_obj['current']['temp_c'],json_obj['current']['feelslike_c']))
        final = time.time()
        print(final-inicial)
        dados['tempo'].append(final-inicial)
    

df = pd.DataFrame.from_dict(dados)
df.to_csv('out.csv')