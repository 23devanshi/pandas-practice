# Exercises taken from : https://pynative.com/python-pandas-exercise/
import pandas as pd
import numpy as np

#pd.display
df = pd.read_csv('D:/Python tutorial/Pandas Exercises/1 Automobile Dataset/Automobile_data.csv')
df.shape

#: From given data set print first and last five rows
print(df.head())
print(df.tail())

#Question 2: Clean data and update the CSV file
#Replace all column values which contain ‘?’ and n.a with NaN.
df.replace(('?','n.a'), np.nan, inplace = True)
print(df)

#Question 3: Find the most expensive car company name
#Print most expensive car’s company name and price.
print(df.sort_values('price', ascending=False).loc[0, 'company'])

#Question 4: Print All Toyota Cars details
print(df[df.company == 'toyota'].describe())

#Question 5: Count total cars per company
df.company.value_counts()

#Question 6: Find each company’s Higesht price car
print(df[df.groupby('company').price.transform('max') == df.price])

#Question 7: Find the average mileage of each car making company
df.groupby('company')['average-mileage'].mean()

#Question 8: Sort all cars by Price column
print(df.sort_values('price', ascending=False))

#Question 9: Concatenate two data frames using the following conditions
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

cars = pd.concat([pd.DataFrame(GermanCars), pd.DataFrame(japaneseCars)], axis = 0) 
cars.Company = cars.Company.str.strip()
print(cars)

#Question 10: Merge two data frames using the following condition
#Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

meta = pd.DataFrame(Car_Price).merge(pd.DataFrame(car_Horsepower), left_on = 'Company', right_on = 'Company', how = 'inner')
print(meta)
