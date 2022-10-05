
import json
from logging import exception
from threading import Thread
import requests
import time
import pandas as pd
import contextlib
import io

def run_thread(url,headers,querystring):
    inicial = time.time()
    test = True
    try:
        with contextlib.redirect_stderr():
            response = requests.request("GET", url, headers=headers, params=querystring)
    except Exception as ex:
        try:
            with contextlib.redirect_stderr():
                response = requests.request("GET", url, headers=headers, params=querystring)
        except Exception as e:
            time.sleep(.5)
            with contextlib.redirect_stderr(io.StringIO()):
                response = requests.request("GET", url, headers=headers, params=querystring)
    json_obj = json.loads(response.text)
    print("Temperatura atual é de {}ºC e a sensação térmica é de {}ºC.".format(json_obj['current']['temp_c'],json_obj['current']['feelslike_c']))
    final = time.time()
    return final-inicial

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"-5.79448, -35.211"}

headers = {
        "X-RapidAPI-Key": "e17e1e7f59mshca729c8a42e65c6p16a703jsn7d1d2939ef7c",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
        'User-agent': 'Mozilla/5.0'
    }

cenarios = [10, 50, 100, 200, 500, 1000]
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

