# Sample Data
data = [12, None, 45, 78, None, 34, 50, 25, 100]

# 1. Filtering Data: Only keep values greater than 50
filtered_data = []
for value in data:
    if value is not None and value > 50:
        filtered_data.append(value)

print("Filtered Data (values > 50):", filtered_data)

# 2. Handling Missing Values: Remove None values
cleaned_data = []
for value in data:
    if value is not None:
        cleaned_data.append(value)

print("Cleaned Data (no None values):", cleaned_data)

# 3. Categorizing Data: Assign categories based on value ranges
categories = []
for value in cleaned_data:
    if value < 50:
        categories.append('Low')
    elif value < 75:
        categories.append('Medium')
    else:
        categories.append('High')

print("Data Categories:", categories)

# 4. Conditional Aggregation: Sum values greater than 30
total_sum = 0
for value in cleaned_data:
    if value > 30:
        total_sum += value

print("Sum of values greater than 30:", total_sum)
