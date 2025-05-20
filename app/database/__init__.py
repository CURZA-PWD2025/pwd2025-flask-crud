import mysql.connector 
import os
from dotenv import load_dotenv

load_dotenv()

class ConectBD:
    
    @staticmethod
    def get_connect():
        try:
            conn = mysql.connector.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                host=os.getenv("DB_HOST", "localhost"),
                port=os.getenv("DB_PORT", 3306)                
            )
            return conn
        except Exception as ex:
          print(f'An exception occurred {ex}')
        