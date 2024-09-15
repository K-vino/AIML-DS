import numpy as np

def calculate_mean_ignore_values(numbers, ignore_values=None):
    """
    Calculate the mean of a list of numbers with an option to ignore specified values.

    :param numbers: List of numbers.
    :param ignore_values: List of values to ignore in the calculation (default is None).
    :return: Mean of the numbers excluding the specified values.
    """
    if ignore_values is not None:
        numbers = [x for x in numbers if x not in ignore_values]
    return sum(numbers) / len(numbers) if numbers else float('nan')

def analyze_grades(grades, threshold=60, ignore_failing=False):
    """
    Analyze student grades and provide a summary.

    :param grades: List of student grades.
    :param threshold: Minimum passing grade (default is 60).
    :param ignore_failing: Boolean flag to indicate whether to ignore grades below the threshold.
    :return: Summary of the grades.
    """
    if ignore_failing:
        grades = [grade for grade in grades if grade >= threshold]

    mean_grade = calculate_mean_ignore_values(grades)

    return (f"Grades: {', '.join(map(str, grades))}\n"
            f"Mean Grade: {mean_grade:.2f}\n"
            f"Number of Grades: {len(grades)}")

def main():
    """
    Main function to run the student grade analysis program.
    """
    grades = [75, 85, 92, 55, 60, 45, 88]

    print("Analysis including all grades:")
    print(analyze_grades(grades))
    print()  # Empty line for readability

    print("Analysis excluding failing grades (threshold 60):")
    print(analyze_grades(grades, threshold=60, ignore_failing=True))
    print()  # Empty line for readability

    print("Analysis excluding specific values [55, 45]:")
    print(calculate_mean_ignore_values(grades, ignore_values=[55, 45]))

if __name__ == "__main__":
    main()
