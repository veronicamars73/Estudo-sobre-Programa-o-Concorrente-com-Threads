
import json
from threading import Thread
import requests
import time
import pandas as pd


def run_thread(url,headers,querystring):
    inicial = time.time()
    test = True
    response = requests.request("GET", url, headers=headers, params=querystring)
    time.sleep(.07)
    json_obj = json.loads(response.text)
    print("Temperatura atual é de {}ºC e a sensação térmica é de {}ºC.".format(json_obj['current']['temp_c'],json_obj['current']['feelslike_c']))
    final = time.time()
    return final-inicial

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"-5.79448, -35.211"}

headers = {
        "X-RapidAPI-Key": "e8a6292771msh67289abb8e0572fp1e1f25jsn551312caa50c",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
        'User-agent': 'Mozilla/5.0'
    }

cenarios = [10, 50, 100, 200, 500, 1000, 5000]

dados = {'num_execucao':[], 'n':[], 'tempo':[]}

for c in cenarios:
    N = c
    for v in range(20):
        thread = []
        inicial = time.time()
        for i in range(N):
            thread.append(Thread(target=run_thread,args=(url,headers,querystring)))
            thread[-1].start()
        for t in thread:
            t.join()
        dados['num_execucao'].append(v+1)
        dados['n'].append(N)
        final = time.time()
        dados['tempo'].append(final-inicial)

df = pd.DataFrame.from_dict(dados)
df.to_csv('out_c.csv')

