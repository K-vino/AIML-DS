def calculate_mean(numbers):
    """
    Calculate the mean of a list of numbers.

    :param numbers: List of numbers.
    :return: Mean of the numbers.
    """
    return sum(numbers) / len(numbers)

def describe_student(name, *scores, grade="Unknown"):
    """
    Provide a summary of a student's performance.

    :param name: Student's name.
    :param scores: Variable-length list of student's scores.
    :param grade: Optional grade for the student (default is "Unknown").
    :return: Summary of the student's performance.
    """
    if not scores:
        return f"{name} has no scores to evaluate."

    mean_score = calculate_mean(scores)
    return (f"Student: {name}\n"
            f"Scores: {', '.join(map(str, scores))}\n"
            f"Mean Score: {mean_score:.2f}\n"
            f"Grade: {grade}")

def main():
    """
    Main function to run the student score analysis program.
    """
    students = [
        ("Alice", [85, 92, 78], "A"),
        ("Bob", [70, 80, 90], "B"),
        ("Charlie", [60, 65], "C"),
        ("Diana", [], "D")  # No scores for Diana
    ]

    for name, scores, grade in students:
        summary = describe_student(name, *scores, grade=grade)
        print(summary)
        print()  # Print an empty line for better readability

if __name__ == "__main__":
    main()
