
# coding: utf-8

# In[2]:


from geopy.geocoders import Nominatim
import time
import csv
import os

geolocator = Nominatim(user_agent="SecretAgentMan")

os.chdir('/home/hrgroup1/data')
print(os.getcwd())

csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('raw_GEO_DATA.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
#         print(row)
#         print(row[2])
#         print(row[3])
#         input()

        if (row[2] != 'LATITUDE'):
            USER_ID = row[0]
            WORKOUT_ID = row[1]
            LATITUDE = row[2]
            LONGITUDE = row[3]

            time.sleep(1)
            location = geolocator.reverse(LATITUDE+","+LONGITUDE)

            geoAddress = location.raw['address']

            CITY = geoAddress.get('city', '')
            STATE = geoAddress.get('state', '')
            ZIPCODE = geoAddress.get('postcode')
#             print('CITY : ',CITY)
#             print('STATE : ',STATE)
#             print('ZIPCODE : ', ZIPCODE)

            csv_variable = (USER_ID, WORKOUT_ID, CITY, STATE, ZIPCODE)
            
            with open('PARSED_GEO_DATA.csv', 'a', newline = '') as csvfile:
                my_writer = csv.writer(csvfile, delimiter = '|')
                my_writer.writerow(csv_variable)

