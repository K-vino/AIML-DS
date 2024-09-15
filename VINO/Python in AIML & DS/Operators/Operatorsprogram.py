import numpy as np
import pandas as pd

# Step 1: Arithmetic Operators
def arithmetic_operations():
    # Create a NumPy array
    data_array = np.array([10, 20, 30, 40, 50])

    # Perform arithmetic operations
    addition = data_array + 5
    subtraction = data_array - 5
    multiplication = data_array * 2
    division = data_array / 10
    floor_division = data_array // 7
    modulus = data_array % 6
    exponentiation = data_array ** 2

    print("Arithmetic Operations on NumPy Array:")
    print("Addition:\n", addition)
    print("Subtraction:\n", subtraction)
    print("Multiplication:\n", multiplication)
    print("Division:\n", division)
    print("Floor Division:\n", floor_division)
    print("Modulus:\n", modulus)
    print("Exponentiation:\n", exponentiation)

# Step 2: Comparison Operators
def comparison_operations():
    # Create a DataFrame
    data = {'Values': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)

    # Compare elements to filter rows
    filtered_df = df[df['Values'] > 25]

    print("\nFiltered DataFrame using Comparison Operators:")
    print(filtered_df)

# Step 3: Logical Operators
def logical_operations():
    # Create a DataFrame
    data = {'Values': [10, 20, 30, 40, 50],
            'Category': ['A', 'B', 'A', 'B', 'A']}
    df = pd.DataFrame(data)

    # Filter rows where 'Values' > 20 and 'Category' is 'A'
    filtered_df = df[(df['Values'] > 20) & (df['Category'] == 'A')]

    print("\nFiltered DataFrame using Logical Operators:")
    print(filtered_df)

# Step 4: Assignment Operators
def assignment_operations():
    # Create a DataFrame
    data = {'Values': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)

    # Use assignment operators to update DataFrame values
    df['Values'] += 10  # Increase each value by 10
    df['Values'] -= 5   # Decrease each value by 5

    print("\nDataFrame after Assignment Operations:")
    print(df)

# Step 5: Bitwise Operators
def bitwise_operations():
    # Bitwise AND operation
    a = 10  # 1010 in binary
    b = 4   # 0100 in binary
    bitwise_and = a & b

    print("\nBitwise AND of 10 and 4:", bitwise_and)

# Step 6: Practical Applications
def practical_applications():
    # Load a CSV file (example CSV file is assumed to be named 'data.csv')
    try:
        df = pd.read_csv('data.csv')

        # Display the first few rows
        print("\nInitial DataFrame:\n", df.head())

        # Drop rows with missing values
        df.dropna(inplace=True)

        # Replace negative values in a specific column with 0
        df['Column'] = df['Column'].apply(lambda x: x if x >= 0 else 0)

        # Calculate basic statistics
        mean_value = df['Column'].mean()
        std_dev = df['Column'].std()

        print("\nCleaned DataFrame:\n", df)
        print("Mean Value of Column:", mean_value)
        print("Standard Deviation of Column:", std_dev)

    except FileNotFoundError:
        print("The file 'data.csv' was not found. Please provide a valid file path.")

# Execute all functions
arithmetic_operations()
comparison_operations()
logical_operations()
assignment_operations()
bitwise_operations()
practical_applications()
