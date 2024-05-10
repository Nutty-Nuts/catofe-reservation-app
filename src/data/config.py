from dotenv import load_dotenv, dotenv_values
import mysql.connector
import os

load_dotenv()

user = mysql.connector.connect(
    host="localhost",
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
)

query = "CREATE DATABASE IF NOT EXISTS {}"
query = query.format(os.getenv("DATABASE_SCHEMA"))
user.cursor().execute(query)
user.close()

db = mysql.connector.connect(
    host="localhost",
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    database=os.getenv("DATABASE_SCHEMA")
)
cursor = db.cursor()
