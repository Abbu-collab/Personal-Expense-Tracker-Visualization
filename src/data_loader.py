import pandas as pd

def load_data(file_path):
    """
    Load expense CSV file
    """

    df = pd.read_csv(file_path)

    print("\nDataset Loaded Successfully!")

    return df