#%%
import datetime
import logging
import sys
import requests

url = 'https://api.coincap.io/v2/exchanges'
r = requests.get(url)
data = r.json().get('data',[])
print(data)
# %%
import pandas as pd
dataf = pd.DataFrame(data)

def exchange_etl():
    pass

print('how long will i love you')
# %%
