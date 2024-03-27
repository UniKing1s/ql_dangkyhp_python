import pypyodbc as odbc
# import os
# from dotenv import load_dotenv
#
# load_dotenv('../../env.env')
def connect():
    # driver = os.getenv('driver')
    # server = os.getenv('serverName')
    # db = os.getenv('db')
    # user = os.getenv('user')
    # pwd = os.getenv('pwd')
    connection = odbc.connect("Driver={SQL Server};Server=MSI;Database=QLSV;Trusted_Connection=Yes;")
    return connection
# print(connect())
