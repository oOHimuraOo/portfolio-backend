import psycopg2
from decouple import config

try:
    connection = psycopg2.connect(
        dbname=config("DB_NAME"),
        user=config("DB_USER"),
        password=config("DB_PASSWORD"),
        host=config("DB_HOST"),
        port=config("DB_PORT")
    )
    print("Conexão bem-sucedida com o PostgreSQL!")
except Exception as e:
    print(f"Erro na conexão: {e}")
