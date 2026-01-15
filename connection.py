import pymysql
import os
from dotenv import load_dotenv
load_dotenv()


host=os.getenv("ho"),
user="root",
password="Anas,.1122",
database="business_data",
charset="4utf8mb",

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Anas,.1122",
        database="business_data",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor  # ✅ this makes all cursors return dicts
    )
