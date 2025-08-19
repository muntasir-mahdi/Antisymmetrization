import pandas as pd
import numpy as np

df = pd.read_csv('77K_IP.csv')

#Removing first 2 rows (Unit and Comments)
df = df.drop([0,1]).reset_index()
df.drop('index', axis =1, inplace= True)

df = df.astype(float)

# In[20]:
#Number of points 21 means loc[0:20]
for row in df.iterrows():
    df2 = df.loc[:20].mean().to_frame().T

# In[24]:
#Number of points to avg = n (len(df)// n)
df2 = df.groupby(np.arange(len(df)) // 21).mean()

df2.to_csv('New_Processed.csv')

