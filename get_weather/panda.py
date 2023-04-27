import pandas as pd
from helpers_panda import *
from variables import *


#FIXME NEED TO IMPORT THE CONSTANT FOR THE DATA.CSV FILE FROM GET_WEATHER.VARIABLES to use instead of actual file name
#creates the dataset
df = create_data_frame(WEATHER_DATA_CSV)

#print all data
print("All data")
print(df)

#print by date - commented out for now
#start_date = '2023-04-25'
#end_date = '2023-04-25'
#df2 = select_by_date_range(start_date, end_date, df)
#print(df2)


#create new data frame describing the one passed in as df
df3 = df.describe()
print(df3)