# Variables and Data Types in Data Science using Python

# Step 1: Declare variables of different data types
project_name = "Data Science Project"
version = 1.0            # Float type
num_observations = 100   # Integer type
is_active = True         # Boolean type

print("Project Info:")
print("Name:", project_name)
print("Version:", version)
print("Observations:", num_observations)
print("Active:", is_active)

# Step 2: Create a Python list
# Let's assume we're working with a small dataset of 5 observations.
data_list = [10, 20, 30, 40, 50]
print("\nData List:", data_list)

# Step 3: Convert the list to a NumPy array
import numpy as np
data_array = np.array(data_list)
print("\nNumPy Array:")
print(data_array)

# Demonstrating basic operations with NumPy array
print("\nOperations on NumPy Array:")
print("Sum:", np.sum(data_array))
print("Mean:", np.mean(data_array))
print("Standard Deviation:", np.std(data_array))

# Step 4: Convert the list to a pandas DataFrame
import pandas as pd
data_df = pd.DataFrame(data_list, columns=['Values'])
print("\npandas DataFrame:")
print(data_df)

# Demonstrating basic DataFrame operations
print("\nDataFrame Operations:")
print("Summary Statistics:")
print(data_df.describe())

# Step 5: Adding new columns to the DataFrame
data_df['Squared Values'] = data_df['Values'] ** 2
print("\nDataFrame with New Column (Squared Values):")
print(data_df)

# Step 6: Displaying data types of each column in the DataFrame
print("\nData Types in the DataFrame:")
print(data_df.dtypes)
