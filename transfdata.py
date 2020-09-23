import pandas as pd
import numpy as np 
import json
import csv

# Opening JSON file 
f = open('intel.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
#print(data)

information = data['Meta Data']['1. Information']
#print(information)
symbol = data['Meta Data']['2. Symbol']
#print(symbol)
last_ref = data['Meta Data']['3. Last Refreshed']
#print(last_ref)
output_size = data['Meta Data']['4. Output Size']
#print(output_size)
timezone = data['Meta Data']['5. Time Zone']
#print(timezone)

time_series_daily = data['Time Series (Daily)']['2020-09-08']['1. open']
#print(time_series_daily)
    
nvidia_actions_df = {'Meta Data': ["information", "symbol", "last_refreshed", "output_size", "timezone"],
                    'value': [information, symbol, last_ref, output_size, timezone]}

#print(nvidia_actions_df)


op = data['Time Series (Daily)']['2020-09-08']['1. open']
high = data['Time Series (Daily)']['2020-09-08']["2. high"]
low = data['Time Series (Daily)']['2020-09-08']["3. low"]
clos = data['Time Series (Daily)']['2020-09-08']["4. close"]
volu = data['Time Series (Daily)']['2020-09-08']["5. volume"]

nvidia_values = {"2009-09-08": ["open", "high", "low", "close", "volume"], 
                "value": [op, high, low, clos, volu]}

#print(nvidia_values)
daily = data['Time Series (Daily)']
list_daily = []
for date, value in daily.items():
    d = {}
    d['Company'] = symbol
    d['Date'] = date
    d['Open'] = value['1. open']
    d['High'] = value['2. high']
    d['Low'] = value['3. low']
    d['Close'] = value['4. close']
    d['Volume'] = value['5. volume']
    list_daily.append(d)

print(list_daily)

pd.DataFrame(list_daily).to_csv('intel.csv', index=False, header=True)

#df = pd.DataFrame(salary)
#df.to_csv('file2.csv', index=False, header=False)


