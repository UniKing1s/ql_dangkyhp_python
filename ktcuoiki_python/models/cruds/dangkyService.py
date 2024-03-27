# import sys
# sys.path.append("./models")
from ktcuoiki_python.models.db import database
from ktcuoiki_python.models.objects.dkhp import dkhp
def open_connection():
    connection = database.connect()
    global cursor
    cursor = connection.cursor()
    return connection
def getAll():
    connection = open_connection()
    lst = []
    cursor.execute(f"Select * from dkhp order by masv asc")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        dk_hp = dkhp(row[0], row[1], row[2], row[3],row[4])
        lst.append(dk_hp)
    return lst
def getAllByMasv(masv):
    connection = open_connection()
    lst = []
    cursor.execute(f"Select * from dkhp where masv = {masv}")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        dk_hp = dkhp(row[0], row[1], row[2], row[3], row[4])
        lst.append(dk_hp)
    return lst
def insert(masv, mahp):
    connection = open_connection()
    cursor.execute(f"insert into dkhp (masv, mahp) values ('{masv}','{mahp}')")
    connection.commit()
    connection.close()
# insert("'2401'","'003'")
def delete(masv, mahp):
    connection = open_connection()
    cursor.execute(f"delete from dkhp where masv={masv} and mahp={mahp}")
    connection.commit()
    connection.close()
# for i in getAll("2402"):
#     print(i.showInfo())
# for i in getAll("2402"):
#     print(i.showInfo())