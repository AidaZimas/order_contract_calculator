import cx_Oracle
from dotenv import load_dotenv
import os

class OracleDatabase:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Get the connection parameters from environment variables
        self.username = os.getenv("ORACLE_USERNAME")
        self.password = os.getenv("ORACLE_PASSWORD")
        self.dsn = os.getenv("ORACLE_DSN")
        self.connection = None
        self.cursor = None

    def connect(self):
        # Initialize the Oracle Client
        cx_Oracle.init_oracle_client(lib_dir=r"C:\\Users\\aida.zimas\\Downloads\\instantclient-basic-windows.x64-23.7.0.25.01\\instantclient_23_7")

        # Establish the connection
        self.connection = cx_Oracle.connect(user=self.username, password=self.password, dsn=self.dsn)
        # Create a cursor
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        # Execute a query
        self.cursor.execute(query)
        # Fetch the results
        return self.cursor.fetchall()

    def close(self):
        # Close the cursor and connection
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()