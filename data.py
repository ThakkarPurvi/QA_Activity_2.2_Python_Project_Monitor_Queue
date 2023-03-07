import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                      'DATABASE=Monitor;'
                      'UID=byltinsytesqladmin;'
                      'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
cursor = conn.cursor()

print("\n----------------------- DESC -----------------------")
cursor.execute('select * from dbo.logs2 ORDER BY trigger_time DESC').fetchone()
row = cursor.fetchone()
print(f"Latest Queue = {row}")


print("\n----------------------- Datetime = 20 Queue -----------------------")
cursor.execute('SELECT TOP(21) id, job_id, event_trigger, event_description, trigger_time FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
row = cursor.fetchall()
count = 0
for i in row:
    count += 1
    print(f"Queue {count} = {i}")


print("\n----------------------- Time = 100 Queue -----------------------")
cursor.execute('SELECT TOP(101) [trigger_time] FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
row = cursor.fetchall()
index = 0
for i in row:
    index += 1
    for j in i:
        print(f"Queue {index} = {j}")

print("\n----------------------- APP TOP 20 -----------------------")

def top20():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                          'DATABASE=Monitor;'
                          'UID=byltinsytesqladmin;'
                          'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
    cursor = conn.cursor()

    cursor.execute('SELECT TOP(21) id, event_trigger, event_description, trigger_time FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    result = cursor.fetchall()
    count = 0
    for i in result:
        count += 1
        print(f"Queue {count} = {i}")
top20()

print("\n----------------------- APP TOP 100 -----------------------")


def top100():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                          'DATABASE=Monitor;'
                          'UID=byltinsytesqladmin;'
                          'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
    cursor = conn.cursor()
    cursor.execute('SELECT TOP(100) id, job_id, event_trigger, event_description, trigger_time FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    result = cursor.fetchall()
    count = 0
    for i in result:
        count += 1
        print(f"Queue {count} = {i}")
    # return render_template(f'top100.html', top100=result100)


top100()


# def jobid():
#     conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#                           'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
#                           'DATABASE=Monitor;'
#                           'UID=byltinsytesqladmin;'
#                           'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
#     cursor = conn.cursor()
#     id = int(input("Please choose a number (1-3): "))
#     job_id = id
#     cursor.execute('select * from dbo.logs2 where {{{job_id}}}').fetchone()
#     result = cursor.fetchall()
#     count = 0
#     for i in result:
#         count += 1
#         print(f"Queue {count} = {i}")
#


conn.close()

