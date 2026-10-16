# from clean_data import clean_data
from src.clean_data import clean_data

def calculate_financial_ratios():

    df = clean_data()

    # calculate current ratio
    df["current_ratio"] = df["current_asset"] / df["current_liabilities"]

    # calculate quick ratio
    df["quick_ratio"] = (df["cash"] + df["account_receivable"]) / df["current_liabilities"]

    # calculate cash ratio
    df["cash_ratio"] = ( df["cash_equivalents"] + df["cash"] ) / df["current_liabilities"]

    # calculate working capital 
    df["working_capital"] = df["current_asset"] - df["current_liabilities"]

    ratio_columns = [
            "current_ratio",
            "quick_ratio",
            "cash_ratio"
        ]

    df[ratio_columns] = df[ratio_columns].round(2)
    return df

if __name__ == "__main__":
    financial_df = calculate_financial_ratios()

    # print(" =========== Financial Ratios ============")
    # print(financial_df.head())

