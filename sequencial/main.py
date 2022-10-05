import requests
import time
import pandas as pd

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"-5.79448, -35.211"}

headers = {
        "X-RapidAPI-Key": "110980b324msh3d97138e8e21e8bp157743jsn63b875223f54",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
        'User-agent': 'Mozilla/5.0'
    }

cenarios = [10, 50, 100, 200, 500, 1000]

dados = {'num_execucao':[], 'n':[], 'tempo':[]}

for c in cenarios:
    N = c

    for v in range(20):
        dados['num_execucao'].append(v+1)
        dados['n'].append(N)
        inicial = time.time()
        for i in range(N):
            response = requests.request("GET", url, headers=headers, params=querystring)

        final = time.time()
        dados['tempo'].append(final-inicial)
        print(final-inicial)

df = pd.DataFrame.from_dict(dados)
df.to_csv('out.csv')