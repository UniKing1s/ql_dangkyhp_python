# import sys
# sys.path.append("./models")
from ktcuoiki_python.models.db import database
from ktcuoiki_python.models.objects.giatinchi import giatinchi
def open_connection():
    connection = database.connect()
    global cursor
    cursor = connection.cursor()
    return connection
def getAll():
    connection = open_connection()
    lst = []
    cursor.execute(f"Select * from giatinchi order by namhoc asc")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        gia_tinchi = giatinchi(row[0], row[1])
        lst.append(gia_tinchi)
    return lst
def getGiaTinChiTheoNam(nam):
    connection = open_connection()
    lst = []
    cursor.execute(f"Select * from giatinchi where namhoc = {nam}")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        gia_tinchi = giatinchi(row[0], row[1])
        lst.append(gia_tinchi)
    return lst
def insert(gia, nam):
    connection = open_connection()
    cursor.execute(f"insert into giatinchi values ({gia},{nam})")
    connection.commit()
    connection.close()
def update(gia, nam):
    connection = open_connection()
    cursor.execute(f"update giatinchi set gia = {gia} where namhoc = {nam}")
    connection.commit()
    connection.close()
def delete(nam):
    connection = open_connection()
    cursor.execute(f"delete from giatinchi where namhoc = {nam}")
    connection.commit()
    connection.close()
# for i in getAll():
#     print(i.showInfo())
# for i in getAll():
#     print(i.showInfo())
# update(2000000,2022)