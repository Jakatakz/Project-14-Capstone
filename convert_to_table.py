
# coding: utf-8

# In[ ]:


# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context


# import pandas module
import pandas as pd
import geopy.geocoders
from geopy.geocoders import Nominatim
from datetime import datetime
from meteostat import Point, Hourly
import re

import os

os.chdir('/home/hrgroup1/alexcode')
print(os.getcwd())

city = []
zip = []
state = []
percipation = []
humidity = []
tempature = []
clean_timestamp = []
lat=8
long=7
row = 0


geolocator = Nominatim(user_agent="geoapiExercises")


# creating a data frame
df = pd.read_csv("Clean_csv_1.csv")

#main loop
#for x in range(1,len(df-2)):
for x in range(1,2500):

    #convert long and lat to str for geopy
    Latitude = str(df.iloc[row,lat])
    Longitude = str(df.iloc[row,long])

    #run in geopy and gather data
    location = geolocator.reverse(Latitude + "," + Longitude, timeout=60)
    address = location.raw['address']
    city.append(address.get('city', ''))
    state.append(address.get('state', ''))
    zip.append(address.get('postcode'))

    #gather weather data
    timestamp = str(df.iloc[row,6]) #start timestamp

    # breaking into list for format
    startdate = re.split('-|:| ', timestamp)

    i=0
    for x in range(0, len(startdate)):
        clean_timestamp.append(int(startdate[i]))
        i = i + 1


    #start and end times
    start = datetime(clean_timestamp[0], clean_timestamp[1], clean_timestamp[2], clean_timestamp[3], clean_timestamp[4],clean_timestamp[5])
    end = datetime(clean_timestamp[0], clean_timestamp[1], clean_timestamp[2], clean_timestamp[3] + 1, 0, 0)

    #create location based on coords
    location = Point(float(Latitude),float(Longitude))
    #gather weather data
    data = Hourly(location, start, end)
    data = data.fetch()

    #create list of weather data
    tempature.append(data['temp'].loc[data.index[0]])
    humidity.append(data['rhum'].loc[data.index[0]])
    percip = data['prcp'].loc[data.index[0]]

    row = row+1


#add all data to datafram
df.insert(10, "Zipcode", zip)
df.insert(11, "City", city)
df.insert(12, "State", state)
df.insert(13, "Temperature", tempature)
df.insert(14, "Humidity", humidity)
df.insert(15, "Precipitation", percipation)


#output frame to CSV
df.to_csv('finaldata.csv')




#data['temp'].loc[data.index[0]] -- temp
#data['rhum'].loc[data.index[0]]  -- humiditiy
#data['prcp'].loc[data.index[0]] -- percip

