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
group_df_mean = df.groupby('Age').mean()
print(group_df)