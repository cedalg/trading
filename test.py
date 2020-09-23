import os
import pandas as pd
import json
import pymongo

try:
    dfcsv = pd.read_csv('NVDA.csv')
    print("dfcsv créé")
except:
    print("échec")


myclient = pymongo.MongoClient('mongodb+srv://cedric:Casablanca1@cluster0.e1ph3.gcp.mongodb.net/test')

try:
    mydb = myclient["Trading"]
    print("base de donnée trading créée")
except:
    print("erreur dans la création de la base de donnée")

try:
    mycol = mydb["nvidia"]
    print("collection créée")
except:
    print("collection pas créée")

try:
    data = dfcsv.to_dict(orient = 'records')  # Here's our added param..
    mycol.insert_many(data)
    print('ok')
except:
    print("échec")