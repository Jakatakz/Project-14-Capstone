
# coding: utf-8

# In[6]:


# import pandas as pd
import re
from datetime import datetime
from meteostat import Point, Hourly
import os
import csv

os.chdir('/home/hrgroup1/data')
print(os.getcwd())

csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('raw_WEATHER_DATA.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        if (row[2] != 'LATITUDE'):
            USER_ID = row[0]
            WORKOUT_ID = row[1]
            LATITUDE = float(row[2])
            LONGITUDE = float(row[3])
            TIMESTAMP = row[4]

            # breaking into list for format
            startdate = re.split('-|:| ', TIMESTAMP)
            clean_timestamp = startdate
            
            #start and end times
            if (int(clean_timestamp[3]) < 23):
                start = datetime(int(clean_timestamp[0]), int(clean_timestamp[1]), int(clean_timestamp[2]), int(clean_timestamp[3]))
                end = datetime(int(clean_timestamp[0]), int(clean_timestamp[1]), int(clean_timestamp[2]), int(clean_timestamp[3]) + 1, 0)
            else:
                start = datetime(int(clean_timestamp[0]), int(clean_timestamp[1]), int(clean_timestamp[2]), int(clean_timestamp[3]))
                end = datetime(int(clean_timestamp[0]), int(clean_timestamp[1]), int(clean_timestamp[2]), 0, 0)
                


            #create location based on coords
            location = Point(LATITUDE, LONGITUDE)
            #gather weather data
            data = Hourly(location, start, end)
            data = data.fetch()

#             print(data)
#             input()
            
            #create list of weather data
            if data.empty:
                TEMPERATURE = 0
                HUMIDITY = 0
                PRECIPITATION = 0
            else:
                TEMPERATURE = data['temp'].loc[data.index[0]]
                HUMIDITY = data['rhum'].loc[data.index[0]]
                PRECIPITATION = data['prcp'].loc[data.index[0]]

#             print('PRECIPITATION: ' + str(PRECIPITATION))
            if str(TEMPERATURE) == 'nan':
                TEMPERATURE = 0
            if str(HUMIDITY) == 'nan':
                HUMIDITY = 0
            if str(PRECIPITATION) == 'nan':
                PRECIPITATION = 0
#             print('Data: ')
#             print('TEMPERATURE: ' + str(TEMPERATURE))
#             print('HUMIDITY: ' + str(HUMIDITY))
                       
            csv_variable = (USER_ID, WORKOUT_ID, TEMPERATURE, HUMIDITY, PRECIPITATION)
            
            with open('PARSED_WEATHER_DATA.csv', 'a', newline = '') as csvfile:
                my_writer = csv.writer(csvfile, delimiter = '|')
                my_writer.writerow(csv_variable)

