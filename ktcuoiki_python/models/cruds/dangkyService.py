# import sys
# sys.path.append("./models")
from ktcuoiki_python.models.db import database
from ktcuoiki_python.models.objects.dkhp import dkhp
from datetime import date, datetime
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
    cursor.execute(f"Select * from dkhp where masv = '{masv}'")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        dk_hp = dkhp(row[0], row[1], row[2], row[3], row[4])
        lst.append(dk_hp)
    return lst
def getAllByMasvHaveMoney(masv):
    connection = open_connection()
    lst = []
    cursor.execute(f"Select sinhvien.masv, dkhp.mahp, ngaydangky, "
                   f"ngaydongphi, dathanhtoan, (hocphan.stc * giatinchi.gia) "
                   f"from dkhp join hocphan ON hocphan.mahp = dkhp.mahp "
                   f"JOIN sinhvien on sinhvien.masv = dkhp.masv "
                   f"join lop on lop.malop = sinhvien.malop "
                   f"join giatinchi on giatinchi.namhoc = lop.nam where dkhp.masv = '{masv}'")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        dk_hp = dkhp(row[0], row[1], row[2], row[3], row[4])
        dk_hp.setTongTien(row[5])
        lst.append(dk_hp)
    return lst
def insert(masv, mahp):
    connection = open_connection()
    cursor.execute(f"insert into dkhp (masv, mahp) values ('{masv}','{mahp}')")
    connection.commit()
    connection.close()
def update(dkhp):
    connection = open_connection()
    # if dkhp.dadongphi == 1:
    #     try:
    #         today = datetime.now()
    #         ngaydongphi = today.strftime("%Y-%m-%d")
    #         # print(ngaydongphi)
    #         cursor.execute(
    #             f"update dkhp set dathanhtoan  = {dkhp.dadongphi}, ngaydongphi = '{str(ngaydongphi)}' where masv = '{dkhp.masv}' and mahp = '{dkhp.mahp}'")
    #     except:
    #         # print(ExceptionType1)
    #         print("Lỗi: đổi ngày đóng phí")
    # else:
    #     cursor.execute(
    #         f"update dkhp set dathanhtoan  = {dkhp.dadongphi} where masv = '{dkhp.masv}' and mahp = '{dkhp.mahp}'")
    cursor.execute(
        f"update dkhp set dathanhtoan  = {dkhp.dadongphi} where masv = '{dkhp.masv}' and mahp = '{dkhp.mahp}'")
    connection.commit()
    connection.close()
def delete(masv, mahp):
    connection = open_connection()
    cursor.execute(f"delete from dkhp where masv='{masv}' and mahp='{mahp}'")
    connection.commit()
    connection.close()
# for i in getAll("2402"):
#     print(i.showInfo())
# for i in getAll("2402"):
#     print(i.showInfo())
# insert('2401','005')
# for i in getAllByMasvHaveMoney('2401'):
#
#     print(i.showInfoWithTong())