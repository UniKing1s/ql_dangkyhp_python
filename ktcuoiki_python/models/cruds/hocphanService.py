from ktcuoiki_python.models.db import database
from ktcuoiki_python.models.objects.hocphan import hocphan
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
    query = "Select * from hocphan order by hocky asc"
    lst = []
    # cursor = connection.cursor()
    cursor.execute("Select * from hocphan order by hocky asc")
    rows = cursor.fetchall()
    for row in rows:
        hp = hocphan(row[0], row[1], row[2], row[3])
        lst.append(hp)
    conn.close()
    return lst

    # df = pd.read_sql_query("Select * from hocphan order by hocky asc",connection)
    # lst = []
    # for row in df.itertuples():
    #     hp = hocphan(row[1], row[2], row[3], row[4])
    #     lst.append(hp)
    # connection.close()
    # return lst
def getAllHpBySV(masv):
    conn = open_connection()
    cursor.execute(f"Select * from hocphan where mahp not in (select mahp from dkhp where masv = '{masv}')")
    rows = cursor.fetchall()
    conn.close()
    lst = []
    for row in rows:
        lst.append(hocphan(row[0], row[1], row[2], row[3]))
    return lst

def insert(hocphan):
    maxMahp = (int(getMaxMasv()[0][0]) + 1)
    conn = open_connection()

    # print(maxMahp)
    if maxMahp < 100:
        mahp = '0'+str(maxMahp)
        # print(mahp)
    # print(mahp)
    cursor.execute(f"insert into hocphan values('{mahp}',N'{hocphan.tenhp}',{hocphan.stc},{hocphan.hk})")
    # try:
    #
    # except:
    #     print("Lỗi")

    conn.commit()
    conn.close()
def update(hocphan):
    conn = open_connection()
    cursor.execute(f"update hocphan set tenhp=N'{hocphan.tenhp}', stc={hocphan.stc}, hocky={hocphan.hk} where mahp='{hocphan.mahp}'")
    conn.commit()
    conn.close()
def delete(mahp):
    conn = open_connection()
    cursor.execute(f"delete from hocphan where mahp='{mahp}'")
    conn.commit()
    conn.close()
def getMaxMasv():
    conn = open_connection()
    cursor.execute("Select Max(mahp) from hocphan")
    rows = cursor.fetchall()
    conn.close()
    return rows
hp = hocphan('3131',"hp1",1,1)
# insert(hp)
# delete('8655')
# for i in getAll():
#     print(i.showInfo())
# insert(hp)
