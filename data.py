from variable import cursor, conn, connection
from datetime import datetime
timestamp = 1625309472.357246

date_time = datetime.fromtimestamp(timestamp)
str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
print("Current timestamp", str_date_time)

cursor.execute("INSERT INTO dbo.logs2 (job_id, event_trigger, event_description, trigger_time) VALUES (3, 'trigger', 'inserting') str_date_time")
conn.commit()

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
    cursor.execute('SELECT TOP(21) id, event_trigger, event_description, trigger_time FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    result = cursor.fetchall()
    count = 0
    for i in result:
        count += 1
        print(f"Queue {count} = {i}")
top20()

print("\n----------------------- APP TOP 100 -----------------------")
print(f"Latest Queue = {r}")

def top100():
    cursor.execute('SELECT TOP(100) id, job_id, event_trigger, event_description, trigger_time FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    result = cursor.fetchall()
    count = 0
    for i in result:
        count += 1
        print(f"Queue {count} = {i}")

top100()

