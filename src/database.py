import cx_Oracle
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class OracleDatabase:
    def __init__(self):
        self.dsn = os.getenv("ORACLE_DSN")
        self.user = os.getenv("ORACLE_USERNAME")
        self.password = os.getenv("ORACLE_PASSWORD")
        self.connection = None

    def connect(self):
        self.connection = cx_Oracle.connect(self.user, self.password, self.dsn)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def close(self):
        if self.connection:
            self.connection.close()

    def fetch_data(self, order_id):
        cache_filename = f"{order_id}.json"
        if os.path.exists(cache_filename):
            print(f"Using cached data from {cache_filename}")
            with open(cache_filename, 'r') as cache_file:
                return json.load(cache_file)
        else:
            query = f"""
            SELECT a.NAME, a.TEXT_VALUE 
            FROM DOCUMENT d 
            INNER JOIN ATTRIBUTE a ON a.DOCUMENT_ID = d.DOCUMENT_ID 
            WHERE d.ORDER_ID = {order_id} 
            AND d.DOCUMENT_TYPE = 'PRIVATE_ORDER_CONTRACT' 
            ORDER BY NAME
            """
            results = self.execute_query(query)
            def lob_to_str(value):
                return value.read() if isinstance(value, cx_Oracle.LOB) else value

            data = [{"NAME": lob_to_str(row[0]), "TEXT_VALUE": lob_to_str(row[1])} for row in results]
            with open(cache_filename, 'w') as cache_file:
                json.dump(data, cache_file, indent=4)
            print(f"Data has been fetched and cached in {cache_filename}")
            return data