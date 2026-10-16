from pathlib import Path
import pandas as pd


def load_data():

    # get to the main project directory
    project_root = Path(__file__).resolve().parent.parent

    #create the path to the csv file
    file_path = project_root / "data" / "sample_data.csv"

    #load csv into dataframe
    df = pd.read_csv(file_path)

    return df

# Run this section only when load_data.py is executed directly
if __name__ == "__main__":

    df = load_data()

    print(df.head())

