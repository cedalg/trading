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
    return "data récupérés sous forme de fichiers json"

have_data(liste_entreprises)



