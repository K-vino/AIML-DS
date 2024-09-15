import pandas as pd
import numpy as np

# Part 1: Calculate Squares of Numbers

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Initialize an empty list to store the squares
squares = []

# Use a for loop to calculate the square of each number
for number in numbers:
    square = number ** 2
    squares.append(square)

# Print the results
print("Squares of the numbers:", squares)

# Part 2: Data Cleansing in a pandas DataFrame

# Create a DataFrame with some missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, np.nan],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("\nOriginal DataFrame:")
print(df)

# Use a for loop to iterate over rows and fill missing values
for index, row in df.iterrows():
    if pd.isna(row['Age']):
        df.at[index, 'Age'] = 0  # Replace missing age with 0

# Print the DataFrame after cleansing
print("\nDataFrame after data cleansing:")
print(df)
