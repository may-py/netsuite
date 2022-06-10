import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from requests_oauthlib import OAuth1Session
import json


ck = "xxxx"
cs = "xxxx"
tk = "xxxx"
ts = "xxxx"

url = 'https://xxxxxxx.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=xxxx&deploy=2'  #replace account and script code xxxx

oauth = OAuth1Session(
    client_key=ck,
    client_secret=cs,
    resource_owner_key=tk,
    resource_owner_secret=ts,
    signature_method='HMAC-SHA256',
    realm='xxxxxxxx')  # replace account code xxxxx
    
payload = {}
resp = oauth.get(
    url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(payload),
)



data = resp.json()
df1 = pd.json_normalize(data['data'])

#Save data in csv 
df1.to_csv('data.csv',index=False)

#read csv
df = pd.read_csv('data.csv')

columns = [a,b,c,x,y,z]

dict(zip(df.columns,name))

columns = name
df.columns = columns

df.info()


