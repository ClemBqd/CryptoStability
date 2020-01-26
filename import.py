import numpy as np
import pandas as pd

df3 = pd.read_csv('pfebtc.csv',sep = ',')  
print(df3) 
current_time="28/1/2015"
print(df3.loc[df3['Date'] == current_time].index.item())
print(df3['cours'][2])
