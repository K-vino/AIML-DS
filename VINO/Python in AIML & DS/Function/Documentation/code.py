import statistics

def calculate_mean(numbers):
    """
    Calculate the mean of a list of numbers.

    :param numbers: List of numbers (list of int or float).
    :return: Mean of the numbers (float).
    """
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.

    :param numbers: List of numbers (list of int or float).
    :return: Median of the numbers (float or int).
    """
    return statistics.median(numbers)

def calculate_std_dev(numbers):
    """
    Calculate the standard deviation of a list of numbers.

    :param numbers: List of numbers (list of int or float).
    :return: Standard deviation of the numbers (float).
    """
    return statistics.stdev(numbers)

def main():
    """
    Main function to demonstrate the use of statistical functions.
    """
    numbers = [10, 20, 30, 40, 50]

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    std_dev = calculate_std_dev(numbers)

    print("Numbers:", numbers)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)

if __name__ == "__main__":
    main()
