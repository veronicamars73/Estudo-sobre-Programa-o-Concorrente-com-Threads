import requests
import json

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"-5.79448, -35.211 "}

headers = {
	"X-RapidAPI-Key": "e8a6292771msh67289abb8e0572fp1e1f25jsn551312caa50c",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

json_obj = json.loads(response.text)
print("Temperatura atual é de {}, e a sensação térmica é de {}.".format(json_obj['current']['temp_c'],json_obj['current']['feelslike_c']))