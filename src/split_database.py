from sqlalchemy import create_engine, text, URL
# from financial_ratios import calculate_financial_ratios
from src.financial_ratios import calculate_financial_ratios
import os
from dotenv import load_dotenv

# PostgreSQL configuration
# USERNAME = "postgres"
# PASSWORD = "password123"
# HOST = "localhost"
# PORT = "5432"


# # TEMPORARY LOCAL TEST
# DB_USER = "postgres.cyiudiojmghwxwkpeqcd"
# DB_PASSWORD = "Bang(*_Bang"
# DB_HOST = "aws-0-ap-northeast-1.pooler.supabase.com"
# DB_PORT = 5432
# DB_NAME = "postgres"


load_dotenv()


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


DATABASE_NAME = "financial_health_db"


# # Connect to existing database
# def connect_to_database():

#     database_url = (
#         f"postgresql+psycopg2://{USERNAME}:{PASSWORD}"
#         f"@{HOST}:{PORT}/{DATABASE_NAME}"
#     )

#     engine = create_engine(database_url)

#     return engine


# supabase connection

# def connect_to_database():

#     database_url = URL.create(
#         drivername="postgresql+psycopg2",
#         username=DB_USER,
#         password=DB_PASSWORD,
#         host=DB_HOST,
#         port=DB_PORT,
#         database=DB_NAME
#     )

#     engine = create_engine(
#         database_url,
#         connect_args={
#             "sslmode": "require"
#         }
#     )

#     return engine


def connect_to_database():

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "postgres")

    database_url = URL.create(
        drivername="postgresql+psycopg2",
        username=db_user,
        password=db_password,
        host=db_host,
        port=int(db_port),
        database=db_name
    )

    engine = create_engine(
        database_url,
        connect_args={
            "sslmode": "require"
        }
    )

    return engine


# Split the dataframe
def split_financial_data():
    # get the final dataframe 
    df = calculate_financial_ratios()


    # create first table for original financial data
    financial_data_df = df[["year", "current_asset", "current_liabilities", "cash", "account_receivable", "cash_equivalents"]].copy()

    # create second table for financial ratios
    financial_ratios_df = df[["year", "current_ratio", "quick_ratio", "cash_ratio", "working_capital"]].copy()

    return financial_data_df, financial_ratios_df

# upload both table into the database
def upload_split_data():
    # connect to postgresql database
    engine = connect_to_database()

    # get the two dataframe
    financial_data_df, financial_ratios_df = split_financial_data()

    # upload the first table into the database
    financial_data_df.to_sql(name="real_financial_data", con=engine, if_exists="replace", index=False)
    print("Financial data uploaded successfully to the database")

    # upload the second table into the database
    financial_ratios_df.to_sql(name="financial_ratios", con=engine, if_exists="replace", index=False)
    print("Financial ratios uploaded successfully to the database")

    return engine


# add primary keys to both tables

def add_primary_keys(engine):
    with engine.begin() as connection:
        # financial key for real_financial_data table
        connection.execute(
            text(
                """ ALTER TABLE real_financial_data 
                ADD PRIMARY KEY (year)"""
            )
        )
        # primary ky for financial ratios table
        connection.execute(
            text(
                """
                ALTER TABLE financial_ratios
                ADD PRIMARY KEY (year);
                """
            )
        )
    print("Primary key added successfully to both tables")



if __name__ == "__main__":
    engine = upload_split_data()
    add_primary_keys(engine)
    print("\n Database split completed successfully, and primary keys added to both table")
