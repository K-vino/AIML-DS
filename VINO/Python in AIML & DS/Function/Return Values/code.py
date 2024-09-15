def calculate_statistics(numbers):
    """
    Calculate the mean and standard deviation of a list of numbers.

    :param numbers: List of numbers.
    :return: Tuple containing the mean and standard deviation.
    """
    # Compute the mean (average)
    mean = sum(numbers) / len(numbers)

    # Compute the variance using a generator expression
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

    # Standard deviation is the square root of the variance
    std_dev = variance ** 0.5

    return mean, std_dev

# Example usage:
numbers = [10, 20, 30, 40, 50]
mean, std_dev = calculate_statistics(numbers)
print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
