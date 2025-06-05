import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as erro:
        print("❌ Erro ao conectar ao banco de dados:", erro)
        return None
