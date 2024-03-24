import pypyodbc as odbc
# import pyodbc
def connect():
    connection = odbc.connect(
    "Driver={SQL Server};Server=MSI;Database=QLSV;UID=sa;PWD=khoivo99122;Trusted_Connection=Yes;"
    )
    return connection

    # connection = pyodbc.connect(
    #     "DRIVER={SQL Server};SERVER=MSI;DATABASE=QLSV;UID=sa;PWD=khoivo99122"
    # )
# connect()
