import pyodbc
import os

print(os.environ['PWD'])

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                      'DATABASE=Monitor;'
                      'UID=byltinsytesqladmin;'
                      'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')

cursor = conn.cursor()

print("\n----------------------- DESC -----------------------")
cursor.execute('select * from dbo.logs ORDER BY trigger_time DESC').fetchone()
row = cursor.fetchone()
print(f"Latest Queue = {row}")


print("\n----------------------- Datetime = 20 Queue -----------------------")
cursor.execute('SELECT TOP(21) id, trigger_time FROM dbo.logs ORDER BY trigger_time DESC').fetchone()
row = cursor.fetchall()
count = 1
for i in row:
    print(f"Queue {count} = {i}")
    count += 1


print("\n----------------------- Time = 20 Queue -----------------------")
cursor.execute('SELECT TOP(21) [trigger_time] FROM dbo.logs ORDER BY trigger_time DESC').fetchone()
row = cursor.fetchall()
index = 0
for i in row:
    index += 1
    for j in i:
        print(f"Queue {index} = {j}")
conn.close()

# SELECT TOP(20) [trigger_time] FROM dbo.logs ORDER BY trigger_time DESC
