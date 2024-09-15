# Sample dataset
data = [23, 45, 300, 50, 15, 200, 5, 60, 80, 120]

# Thresholds for outlier detection and categorization
outlier_threshold = 100
category_thresholds = [30, 60]  # Ranges for categorization

# Initialize lists for processed data
filtered_data = []
categories = []

# Filter out outliers and categorize remaining data
for value in data:
    # Check for outliers
    if value > outlier_threshold:
        print(f"Outlier detected: {value}")
    else:
        # Add valid value to filtered data
        filtered_data.append(value)

        # Categorize the value based on thresholds
        if value <= category_thresholds[0]:
            categories.append('Low')
        elif value <= category_thresholds[1]:
            categories.append('Medium')
        else:
            categories.append('High')

# Generate and print the summary report
print("\nFiltered Data:", filtered_data)
print("Categories:", categories)

# Count the number of occurrences in each category
low_count = categories.count('Low')
medium_count = categories.count('Medium')
high_count = categories.count('High')

# Print the summary report
print("\nSummary Report:")
print(f"Number of Low values: {low_count}")
print(f"Number of Medium values: {medium_count}")
print(f"Number of High values: {high_count}")

# Additional information
print("\nDetails of filtered data and their categories:")
for value, category in zip(filtered_data, categories):
    print(f"Value: {value}, Category: {category}")
