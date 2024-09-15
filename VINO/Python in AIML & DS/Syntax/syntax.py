# Python Syntax for Data Science

# Indentation: Python uses indentation to define code blocks
for i in range(5):
    print(f"Loop iteration: {i}")  # This is part of the loop block

# Case Sensitivity: Python treats 'Data', 'data', and 'DATA' as different variables
Data = 10
data = 20
DATA = 30

print("\nCase Sensitivity Example:")
print(f"Data: {Data}, data: {data}, DATA: {DATA}")  # Outputs 10, 20, 30

# Comments: Comments help explain your code and are ignored by the interpreter
x = 42  # Setting the value of x

# Simple Hello World Program
def hello_world():
    print("\nHello, World!")  # Prints Hello, World!

hello_world()

# Importing necessary libraries for data analysis
import pandas as pd  # Pandas for data manipulation
import numpy as np  # NumPy for numerical computations

# Creating a sample dataset using a Pandas DataFrame
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'Score': [88, 75, 90, 95, 85]
})

# Printing the dataset
print("\nDataset Head:")
print(data.head())  # Displaying the first 5 rows of the dataset

# Basic Data Analysis: Calculate average age and score
average_age = data['Age'].mean()
average_score = data['Score'].mean()

print("\nAverage Age:", average_age)
print("Average Score:", average_score)

# Filtering data: Find individuals with scores greater than 85
high_scorers = data[data['Score'] > 85]
print("\nHigh Scorers (Score > 85):")
print(high_scorers)

# Creating a NumPy array and performing a simple operation
numbers = np.array([1, 2, 3, 4, 5])
squared_numbers = numbers ** 2  # Squaring each element in the array

print("\nNumPy Array Example:")
print(f"Original Numbers: {numbers}")
print(f"Squared Numbers: {squared_numbers}")
