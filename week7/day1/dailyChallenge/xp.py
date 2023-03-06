import numpy as np   
# def create_array(start,length,stop): 
#     return np.arange(start,stop, (stop-start)/(length-1))

# #creating an numpy array of length 100, starting from 6 and has a step of 4 between consecutive numbers
# res = create_array(6,100,206)
# a = np.array([1,2,3,np.nan,5,6,7,np.nan])
# print(a)

# arr = np.random.randint(1,101, (5,6))  # random array of integers between 1 and 100, with shape (5, 6)
# print("Array: \n", arr)
# max_rows = [max(row) for row in arr] # list comprehension to find maximum int for each row in array 
# print("Max Integer per Row: \n", max_rows)

import pandas as pd

# # series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# # unique_values_freq = series.value_counts()

# # print(unique_values_freq)

# series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
# date_series = pd.to_datetime(series)
# # # Get day of month
# series_day_of_month = date_series.dt.day
# print('Day of Month: ', series_day_of_month)

# # # Get week number
# series_week_number = date_series.dt.weekofyear
# print('Week Number: ', series_week_number)

# # # Get day of year 
# series_day_of_year = date_series.dt.dayofyear
# print('Day of Year: ', series_day_of_year)

# # # Get day of week
# series_day_of_week = date_series.dt.dayofweek
# print('Day of Week: ', series_day_of_week)

# from dateutil.parser import parse
# date_series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
# print("Original Series:")
# print(date_series)
# date_series = date_series.map(lambda x: parse(x))
# print("Day of month:")
# print(date_series.dt.day.tolist())
# print("Day of year:")
# print(date_series.dt.dayofyear.tolist())

# print("Day of week:")
# print(date_series.dt.day_of_week.tolist())


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# print(df.dtypes)
# df.rename(columns={'Type':'TypeOfCar'},inplace=True)
# print(df.head())

print(df.isna())

print (df.isnull().sum().sum())