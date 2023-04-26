import requests 
import csv
import os
from variables import *



#function to get API info
def get_weather_data(api_key, city):  
    api_url = "http://api.weatherapi.com/v1/current.json"  
    params = {  
       
        "q": city,
        "key": api_key  
    }  
    response = requests.get(api_url, params=params)  
    data = response.json()  
    return data  

#function to see if data file is created if not set it up
def check_for_file(csv_file):
    check_file = os.path.isfile(csv_file)
    
    if not check_file:
        #create the headers 
        headers = ['Date', 'Time', 'Temperature', 'Condition']
        file = open(csv_file, 'a')
        writer = csv.writer(file)
        writer.writerow(headers)
        file.close()



#function to write data to csv file
def write_to_file(current_date, current_time, current_temp, current_condition):
    #open the file to store data
    file = open(WEATHER_DATA_CSV, 'a')

    writer = csv.writer(file)

    #write temp and date to file
    current_data = [current_date, current_time, current_temp, current_condition]
    writer.writerow(current_data)

    #close the file
    file.close()

    