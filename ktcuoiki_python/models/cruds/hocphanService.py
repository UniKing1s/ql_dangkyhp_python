from ktcuoiki_python.models.db import database
from ktcuoiki_python.models.objects.hocphan import hocphan
# import pandas as pd
# import asyncio
connection = database.connect()
cursor = connection.cursor()
def getAll():
    query = "Select * from hocphan order by hocky asc"
    lst = []
    cursor = connection.cursor()
    cursor.execute("Select * from hocphan order by hocky asc")
    rows = cursor.fetchall()
    for row in rows:
        hp = hocphan(row[0], row[1], row[2], row[3])
        lst.append(hp)
    return lst

    # df = pd.read_sql_query("Select * from hocphan order by hocky asc",connection)
    # lst = []
    # for row in df.itertuples():
    #     hp = hocphan(row[1], row[2], row[3], row[4])
    #     lst.append(hp)
    # connection.close()
    # return lst
def getAllHpBySV(masv):
    cursor.execute(f"Select * from hocphan where mahp not in (select mahp from dkhp where masv = {masv})")
    rows = cursor.fetchall()
    return rows
def insert(hocphan):
    cursor.execute(f"insert into hocphan values({hocphan.mamh},{hocphan.tenhp},{hocphan.stc},{hocphan.hocky})")
def update(hocphan):
    cursor.execute(f"update hocphan set tenhp={hocphan.tenhp}, stc={hocphan.stc}, hocky={hocphan.hocky} where mamh={hocphan.mamh}")
def delete(mamh):
    cursor.execute(f"delete from hocphan where mamh={mamh}")
# for i in getAll():
#     print(i.showInfo())