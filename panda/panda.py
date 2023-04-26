import pandas as pd
import matplotlib.pyplot as plt

#creates the dataset
df = pd.read_csv('data.csv')

#print all data
print(df)




#plots a graph - NOT CURRENTLY USED
#df.plot()
#plt.show()

#print by date
#start_date = '2023-04-20'
#end_date = '2023-04-21'
#df2 = df.loc[df['Date'].between(start_date,end_date)]

#create new data frame describing the one passed in as df

#print(df2)

df3 = df.describe()
print(df3)