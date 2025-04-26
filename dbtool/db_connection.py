import psycopg2
from psycopg2 import OperationalError
import mysql.connector
from mysql.connector import Error

def get_connection(db_type, host, port, username, password, dbname):
    if db_type == "postgres":
        try:
            conn = psycopg2.connect(
                host=host,
                port=port,
                user=username,
                password=password,
                dbname=dbname
            )
            return conn
        except OperationalError as e:
            raise RuntimeError(f"Database connection failed: {e}")
    elif db_type == "mysql":
        try:
             conn = mysql.connector.connect(
            host=host,
            port=port,  # default MySQL port
            user=username,
            password=password,
            database=dbname
            )
             if conn.is_connected():
                return conn
        except Error as e:
            print(f"Error: {e}")
            return None