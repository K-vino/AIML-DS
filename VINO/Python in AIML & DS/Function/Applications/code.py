import pandas as pd

def normalize_column(df, column_name):
    """
    Normalize a column in a pandas DataFrame using min-max scaling.

    :param df: Pandas DataFrame.
    :param column_name: Name of the column to normalize.
    :return: Pandas DataFrame with normalized column.
    """
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Get the minimum and maximum values of the specified column
    min_val = df[column_name].min()
    max_val = df[column_name].max()

    # Apply min-max scaling to normalize the column
    df[column_name] = (df[column_name] - min_val) / (max_val - min_val)

    return df

# Example usage
if __name__ == "__main__":
    # Create a DataFrame with sample data
    df = pd.DataFrame({
        "Values": [10, 20, 30, 40, 50]
    })

    # Print the DataFrame before normalization
    print("Original DataFrame:")
    print(df)

    # Normalize the 'Values' column
    df = normalize_column(df, "Values")

    # Print the DataFrame after normalization
    print("\nDataFrame after normalization:")
    print(df)
