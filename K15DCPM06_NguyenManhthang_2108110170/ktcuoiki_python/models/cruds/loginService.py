from ktcuoiki_python.models.db import database
# conn = database.connect()
# cursor = conn.cursor()
def open_connection():
    connection = database.connect()
    global cursor
    cursor = connection.cursor()
    return connection
def checkLogin(msv, pwd):
    conn = open_connection()
    try:
        cursor.execute(f"Select * from taikhoan where masv = {msv} and pwd = {pwd}")
        vav = cursor.fetchall()
        conn.close()
        return vav
    except:
        conn.close()
        return []
# print(checkLogin("2401","1234567"))