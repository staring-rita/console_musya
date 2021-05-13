import requests

url = "https://openweathermap.org/data/2.5/weather"
api_key = "6755c93a2383e85e725d3907481596ba"

params = {'APPID': api_key, "q": "Novosibirsk", "units": "metric", "lang": "ru"}
result = requests.get(url, params=params)
it = result.json()