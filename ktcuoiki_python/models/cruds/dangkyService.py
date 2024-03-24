# import sys
# sys.path.append("./models")
from ktcuoiki_python.models.db import database
connection = database.connect()
cursor = connection.cursor()

def getAll(masv):
    cursor.execute(f"Select * from dkhp where masv={masv}")
    rows = cursor.fetchall()
    connection.close()
    return rows
def insert(masv, mahp):
    cursor.execute(f"insert into dkhp (masv, mahp) values ({masv},{mahp})")
    connection.commit()
    connection.close()
# insert("'2401'","'003'")
def delete(masv, mahp):
    cursor.execute(f"delete from dkhp where masv={masv} and mahp={mahp}")
    connection.commit()
    connection.close()