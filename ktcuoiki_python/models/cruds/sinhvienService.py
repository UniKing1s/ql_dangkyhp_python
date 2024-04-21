from ktcuoiki_python.models.db import database
from ktcuoiki_python.models.objects.sinhvien import Sinhvien
# import pandas as pd
# import asyncio
# connection = database.connect()
# cursor = connection.cursor()
def open_connection():
    connection = database.connect()
    global cursor
    cursor = connection.cursor()
    return connection
def getAll():
    conn = open_connection()
    lst = []    # query = "Select * from sinhvien order by masv asc"
    # cursor = connection.cursor()
    cursor.execute("Select * from sinhvien order by masv asc")
    rows = cursor.fetchall()
    for row in rows:
        sv = Sinhvien(row[0],row [1], row[2], row [3], row[4],row[5],row[6])
        #  masv, hodem, ten, ngaysinh, gioitinh, noisinh, malop
        lst.append(sv)
    conn.close()
    return lst
def getAllSVByMasv(masv):
    conn = open_connection()
    cursor.execute(f"Select * from sinhvien where masv = {masv}")
    rows = cursor.fetchall()
    conn.close()
    lst = []
    for row in rows:
        lst.append(Sinhvien(row[0],row [1], row[2], row [3], row[4],row[5],row[6]))
    return lst
def insert(sv):
    conn = open_connection()
    cursor.execute(f"insert into sinhvien values('{(int(getMaxMasv()[0][0]) + 1)}',N'{sv.hodem}',N'{sv.ten}','{sv.ngaysinh}',{sv.gioitinh},N'{sv.noisinh}','{sv.malop}')")
    conn.commit()
    conn.close()
def update(sv):
    conn = open_connection()
    cursor.execute(f"update sinhvien set hodem=N'{sv.hodem}', ten=N'{sv.ten}', ngaysinh='{sv.ngaysinh}', gioitinh ={sv.gioitinh}, noisinh = N'{sv.noisinh}', malop = '{sv.malop}' where masv = '{sv.masv}'")
    conn.commit()
    conn.close()
def delete(masv):
    conn = open_connection()
    cursor.execute(f"delete from sinhvien where masv='{masv}'")
    conn.commit()
    conn.close()
# for i in getAll():

def getMaxMasv():
    conn = open_connection()
    cursor.execute("Select Max(masv) from sinhvien")
    rows = cursor.fetchall()
    conn.close()
    return rows
# print(getMaxMasv()[0][0])
# sv = Sinhvien((int(getMaxMasv()[0][0])), "Võ Anh","Khôi", "2024-03-31", 1, "đáva", "DL24")
# delete('8656')
# print(getAllSVByMasv('2401'))