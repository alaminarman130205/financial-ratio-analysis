from sqlalchemy import create_engine, text
from financial_ratios import calculate_financial_ratios

# postgresql connection configuration parameters
USERNAME = "postgres"
PASSWORD = "password123"
HOST = "localhost"
PORT = "5432"

DATABASE_NAME = "financial_health_db"

def create_database():
    # connect to default postgres database to create a new database
    engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}"f"@{HOST}:{PORT}/postgres", isolation_level="AUTOCOMMIT")

    with engine.connect() as connection:

        # check if the database already exists or not
        result = connection.execute(
            text(
                "SELECT 1 FROM pg_database "
                "WHERE datname = :database_name"
            ),
            {"database_name": DATABASE_NAME}
        )       
    
        database_exists = result.fetchone()
        if database_exists:
            print(f"Database '{DATABASE_NAME}' already exists")
        else: 
            # create the database 
            connection.execute(text(f"CREATE DATABASE {DATABASE_NAME}"))
            print(f"Database '{DATABASE_NAME}' created successfully")


def connect_to_database():
    database_url = (f"postgresql+psycopg2://{USERNAME}:{PASSWORD}"f"@{HOST}:{PORT}/{DATABASE_NAME}")
    engine = create_engine(database_url)
    return engine

def upload_financial_data():
    # get final financial dataframe from fianancial ratios
    financial_df = calculate_financial_ratios()

    # connect to our database
    engine = connect_to_database()
    financial_df.to_sql(name="financial_data", con=engine, if_exists = "replace", index=False)
    # print("Financial data uploaded successfully to the database")

if __name__ == "__main__":
    # step 1: create the database
    create_database()

    # step 2: upload financial data to the database
    upload_financial_data()

