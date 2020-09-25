import os
import json
import pandas as pd

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
