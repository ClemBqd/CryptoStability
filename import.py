import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from mesa import Agent

cc=datetime(2019,5,1,tzinfo=None)
myString = cc.strftime("%d-%m-%Y")
print(myString)

df3 = pd.read_excel('pfebtc.xltx')  
#current_time = "28-01-2015"
print(df3.loc[df3['Date'] == myString]) #.index.item())
#a=df3['variation'][df3.loc[df3['Date'] == myString].index.item()]
#print(a)
#print(current_time==myString)
#print(myString)
print((df3['Date'][1400]).strftime("%d-%m-%Y"))