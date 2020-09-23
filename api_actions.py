import requests
import json
import pandas as pd
import os
import pymongo


clé = "NS0DXT6JSFF36NAV"
liste_entreprises = ["NVDA", "AMD", "INTC"]

#Fonctions permettant la récolte des données via une api pour une liste d'entreprise qui sera enregistré dans un dossier nouvellement créé. Pour la liste 
#d'entreprises il faut que les noms coincident avec leurs indices par exemple "NVDA" pour "nvidia"...etc (yahoo finance permet de connaître les ticker)

def have_data(liste_entreprises):
    clé = "NS0DXT6JSFF36NAV"
    liste_entreprises = ["NVDA", "AMD", "INTC"]
    for entreprise in liste_entreprises:
        response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={entreprise}&apikey={clé}&outputsize=full")
        data = response.json()
        print(entreprise)
        #print(data)
        
        try:
            os.mkdir(f'{entreprise}')
            os.chdir(f'{entreprise}')
        except:    
            os.chdir(f'{entreprise}')
        
        print(os.getcwd())
        with open(f"{entreprise}.json", "w+") as f:
            f.write(response.text)
        os.chdir('..')
        print(os.getcwd())



#url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=INTC&apikey=NS0DXT6JSFF36NAV&outputsize=full"

#response = requests.get(url)
#data = response.json()

#with open('intel.json', 'w+') as f:
#    f.write(response.text)

have_data(liste_entreprises)

# Fonctions permettant la transformation des données brutes sous format csv (dataframe pandas)

def transfdata(liste_entreprises):
    for entreprise in liste_entreprises:
        os.chdir(f'{entreprise}')
        f = open(f'{entreprise}.json')
        data = json.load(f)
        print(data)
        daily = data['Time Series (Daily)']
        list_daily = []
        print(os.getcwd())
        for date, value in daily.items():
            d = {}
            d['Company'] = entreprise
            d['Date'] = date
            d['Open'] = value['1. open']
            d['High'] = value['2. high']
            d['Low'] = value['3. low']
            d['Close'] = value['4. close']
            d['Volume'] = value['5. volume']
            list_daily.append(d)
            
        print(list_daily)
        pd.DataFrame(list_daily).to_csv(f'{entreprise}.csv', index=False, header=True)
        print(os.getcwd())
        os.chdir("..")

transfdata(liste_entreprises)

  # Connexion à mongoDB pour le transfert des fichiers vers la base de donnée. 

