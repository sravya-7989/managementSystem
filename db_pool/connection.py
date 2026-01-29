from mysql import connector
from dotenv import load_dotenv
import os

connect=connector.connect(
    user='root',
   # password=os.getenv('DATABASE_PW'),
    password='root',
    host='localhost',
    database='management_db'   
)


cursor=connect.cursor()