import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"-5.79448, -35.211 "}

headers = {
	"X-RapidAPI-Key": "e8a6292771msh67289abb8e0572fp1e1f25jsn551312caa50c",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)