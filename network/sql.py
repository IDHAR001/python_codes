import os
import pymssql

# AZURE_SQL_CONNECTIONSTRING='Driver={ODBC Driver 18 for SQL Server};Server=tcp:josafe.database.windows.net,1433;Database=jacob;UID=jacob;PWD=Password#1;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'

connection_string = os.environ["AZURE_SQL_CONNECTIONSTRING"]
conn = pymssql.connect("josafe.database.windows.net", "jacob", "Password#1", "jacob")

# cursor = conn.cursor()
# if cursor:
#     print("connected")

# sql1 = "CREATE TABLE Persons(id int)"

# sql2 = "SELECT * FROM Items"
# cursor.execute("CREATE SCHEMA python;")
# cursor.execute(sql1)
# cursor.execute("SELECT @@VERSION")
# data = cursor.fetchone()
# data = cursor.fetchall()
# print(data)
# print("done")