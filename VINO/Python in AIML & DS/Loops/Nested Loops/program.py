#1. Nested Loops with NumPy: Calculating Row and Column Sums

import numpy as np

# Create a 2D NumPy array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Initialize lists to store row and column sums
row_sums = []
col_sums = [0] * array_2d.shape[1]  # Initialize with zeros for each column

# Compute row sums using a nested loop
for row in range(array_2d.shape[0]):  # Outer loop: iterates over rows
    row_sum = 0
    for col in range(array_2d.shape[1]):  # Inner loop: iterates over columns
        row_sum += array_2d[row, col]
        col_sums[col] += array_2d[row, col]
    row_sums.append(row_sum)

print("Row sums:", row_sums)
print("Column sums:", col_sums)










#2. Nested Loops with pandas: Calculating Feature Correlations

import pandas as pd
import numpy as np

# Sample dataset with multiple features
data = {'Feature1': [1, 2, 3, 4],
        'Feature2': [4, 3, 2, 1],
        'Feature3': [2, 3, 4, 5]}
df = pd.DataFrame(data)

# Initialize a dictionary to store correlation values
correlation_matrix = {}

# Nested loops to compare each feature with every other feature
for feature1 in df.columns:
    correlation_matrix[feature1] = {}
    for feature2 in df.columns:
        if feature1 != feature2:
            # Compute correlation between feature1 and feature2
            correlation = np.corrcoef(df[feature1], df[feature2])[0, 1]
            correlation_matrix[feature1][feature2] = correlation

# Print the correlation matrix
print("Correlation Matrix:")
for feature1, comparisons in correlation_matrix.items():
    for feature2, corr in comparisons.items():
        print(f"Correlation between {feature1} and {feature2}: {corr:.2f}")
