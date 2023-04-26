

from helpers import *
from variables import *
from get_current_weather import *


  
#Create the CurrentWeather class for Guelph
#holds all the weather data
guelph = CurrentWeather(API_KEY,GUELPH)  

#checks for file and creates in not there
check_for_file(WEATHER_DATA_CSV)

#Write all data to file
write_to_file(guelph.current_date, guelph.current_time, guelph.current_temp, guelph.current_conditions)



    

