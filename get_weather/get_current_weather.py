from helpers import *
from variables import *

#gathers all data on current weather based on city passed in
class CurrentWeather:
    def __init__(self, api_key, city):
        self.current_weather = get_weather_data(api_key, city)
        self.current_temp = self.current_weather["current"]["temp_c"]
        self.date_time_data = self.current_weather['location']['localtime'].split(" ")
        self.current_date = self.date_time_data[0]
        self.current_time = self.date_time_data[1]
        self.current_conditions = self.current_weather['current']['condition']['text']
      
    
    #print out all weather data
    def print_weather(self):
        print(self.current_weather)
    #prints current temp
    def print_temp(self):
        print(self.current_temp)
    #prints curretn date and time
    def print_date_time(self):
        print(self.current_date)
        print(self.current_time)
    #print the current condition
    def print_conditions(self):
        print(self.current_conditions)
  


