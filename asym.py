#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv('New_Processed.csv')

df = df.drop(['Unnamed: 0'], axis=1).reset_index()
df.drop('index', axis =1, inplace= True)

Rxy = pd.DataFrame()
Rxx = pd.DataFrame()


#Calculating Rxy (Subtracting)
n=0
r = df[df.columns[1::2]]
f = df[df.columns[0::2]]
for column in r:
   
    #Row Count
    total_rows = r.iloc[:,n:n+1].count().astype(int)
    total_rows = int(total_rows)
    halfrows= int(total_rows/2)

    #for columns in r:
    rx1 = r.iloc[:halfrows,n:n+1]
    rx2 = r.iloc[halfrows:total_rows,n:n+1].reset_index()
    rx2.drop('index', axis =1, inplace= True)

    #Antisymmetrization
    up = rx1.subtract(rx2, fill_value=0)
    down = rx2.subtract(rx1, fill_value=0)
    
    resistance = pd.concat([up, down], axis=0, ignore_index=True)
    field = f.iloc[:,n:n+1]
    
    processed = pd.concat([field, resistance], axis=1)
    Rxy = pd.concat([Rxy, processed], axis=1)
    n=n+1
    
#Calculating Rxx (Adding)
n=0
r = df[df.columns[1::2]]
f = df[df.columns[0::2]]
for column in r:
   
    #Row Count
    total_rows = r.iloc[:,n:n+1].count().astype(int)
    total_rows = int(total_rows)
    halfrows= int(total_rows/2)

    #for columns in r:
    rx1 = r.iloc[:halfrows,n:n+1]
    rx2 = r.iloc[halfrows:total_rows,n:n+1].reset_index()
    rx2.drop('index', axis =1, inplace= True)

    #Antisymmetrization
    up = rx1.add(rx2, fill_value=0)
    down = rx2.add(rx1, fill_value=0)
    
    resistance = pd.concat([up, down], axis=0, ignore_index=True)
    field = f.iloc[:,n:n+1]
    
    processed = pd.concat([field, resistance], axis=1)
    Rxx = pd.concat([Rxx, processed], axis=1)
    n=n+1


# In[97]:

Rxx.to_csv('Rxx.csv')
Rxy.to_csv('Rxy.csv')

