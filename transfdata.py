import pandas as pd
import numpy as np 
import json
import csv

# Opening JSON file 
f = open('intel.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 

liste_entreprises = ["NVDA, INTC", "AMD"]

def transfdata(data, liste_entreprises):
    for entreprise in liste_entreprises:
        os.chdir(f'{entreprise}')
        daily = data['Time Series (Daily)']
        list_daily = []
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
            pd.DataFrame(list_daily).to_csv(f'{entreprise}.csv', index=False, header=True))


json_to_csv(data, liste_entreprises)

#df = pd.DataFrame(salary)
#df.to_csv('file2.csv', index=False, header=False)


