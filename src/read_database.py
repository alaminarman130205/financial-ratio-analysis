# from split_database import connect_to_database
# import pandas as pd

# def read_financial_data():

#     # Connect to PostgreSQL
#     engine = connect_to_database()

#     # Read original financial data
#     query = """
#         SELECT *
#         FROM real_financial_data
#         ORDER BY year;
#     """

#     financial_data_df = pd.read_sql(query, engine)

#     return financial_data_df


# def read_financial_ratios():

#     # Connect to PostgreSQL
#     engine = connect_to_database()

#     # Read calculated financial ratios
#     query = """
#         SELECT *
#         FROM financial_ratios
#         ORDER BY year;
#     """

#     financial_ratios_df = pd.read_sql(query, engine)

#     return financial_ratios_df


# if __name__ == "__main__":

#     financial_data_df = read_financial_data()
#     financial_ratios_df = read_financial_ratios()

#     print("\n========== REAL FINANCIAL DATA ==========")
#     print(financial_data_df)

#     print("\n========== FINANCIAL RATIOS ==========")
#     print(financial_ratios_df)



import pandas as pd
# from split_database import connect_to_database
from src.split_database import connect_to_database


def read_financial_data():

    engine = connect_to_database()

    query = """
    SELECT *
    FROM real_financial_data
    ORDER BY year;
    """

    df = pd.read_sql(query, engine)

    return df


def read_financial_ratios():

    engine = connect_to_database()

    query = """
    SELECT *
    FROM financial_ratios
    ORDER BY year;
    """

    df = pd.read_sql(query, engine)

    return df


if __name__ == "__main__":

    financial_data_df = read_financial_data()
    financial_ratios_df = read_financial_ratios()

    print("\n========== REAL FINANCIAL DATA ==========")
    print(financial_data_df)

    print("\n========== FINANCIAL RATIOS ==========")
    print(financial_ratios_df)