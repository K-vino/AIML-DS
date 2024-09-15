import numpy as np

# Part 1: Find the First Number Greater Than 100

# List of numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# Initialize index
index = 0

# While loop to find the first number greater than 100
while index < len(numbers):
    if numbers[index] > 100:
        print("First number greater than 100 is:", numbers[index])
        break
    index += 1
else:
    print("No number greater than 100 was found.")

# Part 2: Iteratively Improve Parameters of a Machine Learning Model

# Define a function to simulate model performance
def model_performance(parameter):
    # Simulate performance: better performance as parameter approaches 10
    return -abs(parameter - 10) + 10

# Initialize parameters
current_parameter = 0
tolerance = 0.1  # Performance goal threshold
learning_rate = 0.5  # How much we adjust the parameter in each step
max_iterations = 100  # Maximum number of iterations
iteration = 0

# While loop to improve model parameters
while iteration < max_iterations:
    performance = model_performance(current_parameter)

    # Check if the performance is within the acceptable range
    if performance >= tolerance:
        print("Achieved desired performance with parameter:", current_parameter)
        break

    # Update the parameter (simple gradient ascent simulation)
    current_parameter += learning_rate

    # Print the current parameter and performance
    print(f"Iteration {iteration}: Parameter = {current_parameter}, Performance = {performance}")

    # Increment iteration counter
    iteration += 1

else:
    print("Maximum iterations reached without achieving desired performance.")
