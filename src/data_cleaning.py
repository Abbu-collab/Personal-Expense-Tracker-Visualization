import pandas as pd

def clean_data(df):

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Remove missing values
    df.dropna(inplace=True)

    # Create Month Column
    df["Month"] = df["Date"].dt.strftime("%B")

    print("\nData Cleaning Completed!")

    return df