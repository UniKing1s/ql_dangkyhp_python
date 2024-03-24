from ktcuoiki_python.models.db import database
conn = database.connect()
cursor = conn.cursor()
def checkLogin(msv, pwd):
    try:
        cursor.execute(f"Select * from taikhoan where masv = {msv} and pwd = {pwd}")
        vav = cursor.fetchall()
        return vav
    except:
        return []
# print(checkLogin("2401","1234567"))