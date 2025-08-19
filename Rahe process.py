#Processed RAHE data

import pandas as pd

df = pd.read_csv('ETONew.csv')

#df.head(10)
df = df.dropna()
df = df.drop([0]).reset_index()
df.drop('index', axis =1, inplace= True)
#df.head()

df = df.astype(float)
#df.info()
rahe = (df.max()-df.min())/2
R_AHE= rahe.to_frame()
R_AHE.to_csv('S117_Rahe.csv')

