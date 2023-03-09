from variable import cursor


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


def top100():
    cursor.execute('SELECT TOP(100) id, job_id, event_trigger, event_description, trigger_time FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    result = cursor.fetchall()
    count = 0
    for i in result:
        count += 1
        print(f"Queue {count} = {i}")


top100()


