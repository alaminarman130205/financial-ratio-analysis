import pandas as pd
# from load_data import load_data
from src.load_data import load_data

def clean_data():

    # Original data
    df = load_data()
    # print("============ Original Data ============")
    # print(df.head())

    # check for missing values
    # print("missing values in each column: ", df.isnull().sum())

    # remove row with missing values
    df = df.dropna()

    # check for duplicates
    # print(" number of duplicates row in dataframe ", df.duplicated().sum())

    # check data types of each column 
    # print(" checking data types of each column", df.dtypes)

    numeric_columns = [
        "current_asset",
        "current_liabilities",
        "cash",
        "account_receivable",
        "cash_equivalents"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )   
    
    #  Check final data types
    # print(" checking data types of each column", df.dtypes)

    return df

if __name__ == "__main__":
    cleaned_df = clean_data()