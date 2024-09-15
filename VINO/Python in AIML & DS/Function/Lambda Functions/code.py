# Define a list of tuples where each tuple contains an integer and a string
data = [(1, 'a'), (3, 'c'), (2, 'b')]

# Sort the list based on the second element of each tuple using a lambda function
sorted_data = sorted(data, key=lambda x: x[1])

# Print the sorted list
print("Sorted data based on second element:", sorted_data)
