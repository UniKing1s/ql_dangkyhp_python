from ktcuoiki_python.models.db import database
from ktcuoiki_python.models.objects.sinhvien import Sinhvien
# import pandas as pd
# import asyncio
connection = database.connect()
cursor = connection.cursor()
def getAll():
    lst = []    # query = "Select * from sinhvien order by masv asc"
    cursor = connection.cursor()
    cursor.execute("Select * from sinhvien order by masv asc")
    rows = cursor.fetchall()
    for row in rows:
        sv = Sinhvien(row[0],row [1], row[2], row [3], row[4],row[5],row[6])
        #  masv, hodem, ten, ngaysinh, gioitinh, noisinh, malop
        lst.append(sv)
    return lst
def getAllSVByMasv(masv):
    cursor.execute(f"Select * from sinhvien where masv = {masv}")
    rows = cursor.fetchall()
    return rows
def insert(sv):
    cursor.execute(f"insert into sinhvien values({sv.masv},{sv.hodem},{sv.ten},{sv.ngaysinh},{sv.gioitinh},{sv.noisinh},{sv.malop})")
def update(sv):
    cursor.execute(f"update sinhvien set hodem={sv.hodem}, ten={sv.ten}, ngaysinh={sv.ngaysinh}, gioitinh ={sv.gioitinh}, noisinh = {sv.noisinh}, malop = {sv.malop} where masv = {sv.masv}")
def delete(masv):
    cursor.execute(f"delete from sinhvien where masv={masv}")
# for i in getAll():
#     print(i.showInfo())