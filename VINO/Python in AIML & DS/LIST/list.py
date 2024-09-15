# Introduction to Lists
print("Introduction to Lists in Python")

# Creating Lists
my_list = [10, 20, 30, 'apple', 'banana']
print("Original List:", my_list)

# Accessing Elements
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])

# Adding and Removing Elements
my_list.append('cherry')  # Adding an element to the end
print("List after append:", my_list)

my_list.insert(2, 'orange')  # Inserting an element at index 2
print("List after insert:", my_list)

my_list.remove('banana')  # Removing the first occurrence of 'banana'
print("List after remove:", my_list)

removed_element = my_list.pop()  # Removing and returning the last element
print("Removed Element:", removed_element)
print("List after pop:", my_list)

# Slicing Lists
sub_list = my_list[1:4]  # Extracting elements from index 1 to 3
print("Sliced List (1:4):", sub_list)

# Iterating Through Lists
print("Iterating through List:")
for item in my_list:
    print(item)

# List Methods and Functions
print("\nList Methods and Functions")

# List methods
my_list.extend([40, 50])  # Extending the list with another list
print("List after extend:", my_list)

print("Index of 'apple':", my_list.index('apple'))  # Finding the index of 'apple'
print("Count of 30:", my_list.count(30))  # Counting occurrences of 30

my_list.sort()  # Sorting the list
print("List after sort:", my_list)

my_list.reverse()  # Reversing the list
print("List after reverse:", my_list)

# Advanced Usage - List Comprehensions
print("\nList Comprehensions")

# Basic List Comprehension
squares = [x**2 for x in range(10)]
print("Squares of numbers from 0 to 9:", squares)

# List Comprehension with Conditional Logic
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Squares of even numbers from 0 to 9:", even_squares)

# Nesting Lists
print("\nNesting Lists")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)

# Accessing elements in a nested list
element = matrix[1][2]  # Accessing element in the second row, third column
print("Element at matrix[1][2]:", element)

# Practical Examples
print("\nPractical Examples")

# Using Lists to Handle Datasets
data = [10, None, 30, None, 50]
cleaned_data = [x if x is not None else 0 for x in data]
print("Cleaned Data:", cleaned_data)

# Integrating Lists with Pandas
import pandas as pd

df = pd.DataFrame(cleaned_data, columns=['Values'])
print("DataFrame:")
print(df)

# Integrating Lists with NumPy
import numpy as np

np_array = np.array(cleaned_data)
print("NumPy Array:")
print(np_array)

print("\nProgram completed.")
