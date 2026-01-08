from db import get_db_connection

db = get_db_connection()
print("Connected successfully")
db.close()
