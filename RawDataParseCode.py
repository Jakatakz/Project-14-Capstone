
# coding: utf-8

# In[1]:


from io import StringIO
import pandas as pd
import os

os.chdir('/home/hrgroup1/data')
print(os.getcwd())

# fileJson = open('endomondoHR_small.json', 'r')
fileJson = open('endomondoHR.json', 'r')

Lines = fileJson.readlines()

for line in Lines:
    line = line.replace("'", "\"")
    csvHeader = ['speed', 'altitude', 'gender', 'heart_rate', 'id', 'userId', 'timestamp', 'latitude','longitude', 'sport']
    dataframe = pd.read_json(StringIO(line))
  
    # print(dataframe.columns)
    # print(dataframe.head(4))
    # print(dataframe)
    # input()
    
    if 'speed' in dataframe.columns:
        dataframe.to_csv('output.csv', mode='a', sep='|', encoding='utf-8', index=False, columns=csvHeader, header=False)
        #print(df)
        #input()
    else:
        dataframe.insert(loc=0, column='speed',value='')
        dataframe.to_csv('output.csv', mode='a', sep='|', encoding='utf-8', index=False, columns=csvHeader, header=False)
    
print('All data is parsed.')

