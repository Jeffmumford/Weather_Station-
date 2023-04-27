import pandas as pd


#create the data frame
#returns a new data frame
def create_data_frame(csv_file_name):
    df = pd.read_csv(csv_file_name)
    return df

#create a new data frame within a date range
#returns a new data frame
def select_by_date_range(start_date, end_date, data_frame):
    begin = start_date
    end = end_date
    df2 = data_frame.loc[data_frame['Date'].between(begin, end)]
    return df2


    