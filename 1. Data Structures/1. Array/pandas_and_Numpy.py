# Practicing pandas and numpy arrays for data manipulation purposes only for now
# as it helps performance and ease of use for data manipulation
# Pandas is a library that provides data structures and data analysis tools for Python programming language
# and data manipulation tools for data analysis tasks.
# it helps in Data structures like Series and DataFrame objects that are built on top of NumPy.

# Using numpy for numerical operations
import numpy as np
import pandas as pd

# Creating a sample dataframe
numbers = [1, 2, 3, 4, 5, 5]
array = np.array(numbers)
print(array)
mean = np.mean(array)
print(mean)
sum = np.sum(array)
print(sum)
std = np.std(array)
squared = np.square(array)
print(squared)
unique = np.unique(array)
print(unique)

print(np.sort(unique))


# Pandas 

# Creating a Series
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
series = pd.Series(data)
print(series)

# Creating a sample dataframe
data = {'Name': [ 'David','Solomon', 'Peter', 'Paul', 'James'], 'Age': [69, 36, 45, 77, 67]}
df = pd.DataFrame(data)
print(df)

# Accessing the elements of a dataframe
names = df['Name']
print(names)
ages = df['Age']

#Accessing the elements of a dataframe using loc and iloc
first_row = df.iloc[[0]] #First row
print(first_row) 
ages = df.iloc[0:2]  # Accessing the first two rows
print(ages)

#Filtering the dataframe
filtered_df = df[df['Age'] > 50]
print(filtered_df)

# Adding the new columns
df['Country'] = ['USA', 'UK', 'Canada', 'Australia', 'India']
print(df)

#dropping a column
df = df.drop('Country', axis=1)

# Rename the column
df = df.rename(columns={'Name':'Full Name'})
print(df)

# Descriptive statistics
print(df.describe())

# Grouping the columns
group_df = df.groupby('Age').count()
# group_df_mean = df.groupby('Age').mean()
# print(group_df)


# Handling the missing values
data1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, np.nan]
df1 = pd.DataFrame(data1)

# Checking for missing values
isnull = df1.isnull()
print(isnull, "missing values")

data3 = {'Name': [ 'David','Solomon', 'Peter', 'Paul', 'James'], 'Age': [69, 36, 45, None, None]}
df3 = pd.DataFrame(data3)

print(df3.isnull())

# df_with_missing = df3.dropna()
# print(df_with_missing)
# df_fill = df3.fillna(method='ffill')
# print(df_fill)
df_fill = df3.fillna(np.mean(df3['Age']))
print(df_fill)

# Merging Dataframes
data1 = {'Name': [ 'David','Solomon', 'Peter', 'Paul', 'James'], 'Age': [69, 36, 45, 77, 67]}
data2 = {'Name': [ 'David','Solomon', 'Peter', 'Paul', 'James'], 'Country': ['USA', 'UK', 'Canada', 'Australia', 'India']}
df1= pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df1,df2, on='Name', how='inner')
print(merged_df)

# Concatenating DataFrames
data5 = {'Name': [ 'David','Solomon', 'Peter', 'Paul', 'James'], 'Age': [69, 36, 45, 77, 67], 'Country': [ 'USA', 'UK', 'Canada', 'Australia', 'India']}
df5 = pd.DataFrame(data5)
df6 = pd.DataFrame({'Name': ['Murgugan'], 'Age':[99], 'Country':['Jerusalem']})
concatenated_df5 = pd.concat([df5,df6], ignore_index=True)
print(concatenated_df5)

# Saving the DataFrame to a CSV file
concatenated_df5.to_csv('fact.csv',index=False)

# Reading DataFrame from CSV
df = pd.read_csv('fact.csv')
print(df)

# Applying function to the DataFrame
df['Age in 9 Years'] = df['Age'].apply(lambda x:x+9)
print(df)

# Sorting DataFrame
sorted_df =df.sort_values(by='Age', ascending=False)
print(sorted_df)

# Pivot Table
pivot_table = concatenated_df5.pivot_table(values = 'Age', index = 'Country', aggfunc = 'mean')
print(pivot_table)

# Time series data

import datetime
start_date = datetime.datetime(2025, 3, 1)
end_date = datetime.datetime(2025, 3, 30)
date_range = pd.date_range(start_date, end_date)
print(date_range)

date_range = pd.date_range(start='2025-03-14', periods=10, freq='D')
time_series = pd.DataFrame({'Date':date_range, 'Value':np.random.randint(0, 10, size=len(date_range))})
print(time_series)

# Setting the index of a DataFrame
df5.set_index('Country', inplace=True)
print(df5.index)

# Setting the index of a DataFrame