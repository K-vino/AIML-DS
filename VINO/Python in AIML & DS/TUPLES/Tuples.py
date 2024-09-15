# Comprehensive Program on Tuples in Data Science with Python

# 1. Introduction
# Creating tuples
my_tuple = (1, 2, 3, "a", "b", "c")
empty_tuple = ()
single_element_tuple = (1,)

print("My Tuple:", my_tuple)
print("Empty Tuple:", empty_tuple)
print("Single Element Tuple:", single_element_tuple)

# 2. Importance in Data Science
# Demonstrating tuples as dictionary keys
dataset = {
    ("Alice", 30): "Engineer",
    ("Bob", 25): "Data Scientist"
}
print("Tuple as Dictionary Key:", dataset)

# 3. Basic Operations
# Accessing elements
first_element = my_tuple[0]  # 1
last_element = my_tuple[-1]  # 'c'

print("First Element:", first_element)
print("Last Element:", last_element)

# Concatenation and slicing
new_tuple = my_tuple + (40, 50)
sliced_tuple = my_tuple[1:4]  # (2, 3, 'a')

print("Concatenated Tuple:", new_tuple)
print("Sliced Tuple:", sliced_tuple)

# Iterating through a tuple
print("Iterating through tuple:")
for item in my_tuple:
    print(item)

# 4. Tuple Methods and Functions
# Using index() and count()
index_of_3 = my_tuple.index(3)  # 2
count_of_a = my_tuple.count('a')  # 1

print("Index of 3:", index_of_3)
print("Count of 'a':", count_of_a)

# Converting list to tuple and vice versa
my_list = [1, 2, 3]
list_to_tuple = tuple(my_list)
tuple_to_list = list(my_tuple)

print("List to Tuple:", list_to_tuple)
print("Tuple to List:", tuple_to_list)

# 5. Advanced Usage
# Packing and unpacking
packed_tuple = (1, 'apple', 3.14)
a, b, c = packed_tuple

print("Packed Tuple:", packed_tuple)
print("Unpacked Values:", a, b, c)

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
nested_element = nested_tuple[1][0]  # 3

print("Nested Tuple:", nested_tuple)
print("Nested Element:", nested_element)

# Returning multiple values from a function
def min_max(numbers):
    return (min(numbers), max(numbers))

numbers = [3, 1, 4, 1, 5]
min_value, max_value = min_max(numbers)

print("Min and Max:", min_value, max_value)

# 6. Practical Examples
# Using tuples to handle datasets
record = ('Alice', 30, 'Engineer')
print("Record Tuple:", record)

# Tuples with Pandas
import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [30, 25]}
df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df)

# Tuples with NumPy
import numpy as np
np_array = np.array([(1, 2), (3, 4), (5, 6)])
print("NumPy Array:\n", np_array)
