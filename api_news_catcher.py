import requests
import json
import pandas as pd

url = "https://newscatcher.p.rapidapi.com/v1/search_free"

querystring = {"media":"True","lang":"en","q":"nvidia"}

headers = {
    'x-rapidapi-host': "newscatcher.p.rapidapi.com",
    'x-rapidapi-key': "c50b32df37msh7ead6e376e04df4p171e26jsnd1c6e9f98d43"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
data = response.json()
print(data)

with open('nvidia_nc.json', 'w+') as f:
    f.write(response.text)


