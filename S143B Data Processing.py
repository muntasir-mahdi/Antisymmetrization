#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np

# In[3]:


df = pd.read_csv('S143B_Raw.csv')


# In[7]:
#Removing first 2 rows (Unit and Comments)
df = df.drop([0,1]).reset_index()
df.drop('index', axis =1, inplace= True)


# In[63]:


#df_avgd = df.rolling(min_periods=4).mean()


# In[14]:

#indexer = pd.api.indexers.FixedForwardWindowIndexer(window_size=4)
#df_avgd = df.rolling(window=indexer, min_periods=1).mean()

# In[22]:

df = df.astype(float)

# In[20]:
#Number of points 4 means loc[0:3]
for row in df.iterrows():
    df2 = df.loc[:3].mean().to_frame().T

# In[24]:
#Number of points to avg = n (len(df)// n)
df2 = df.groupby(np.arange(len(df)) // 4).mean()

# In[26]:

df2.to_csv('New_Processed.csv')

