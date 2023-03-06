import logging
from flask import Flask, render_template, request
import pyodbc

logging.basicConfig()
logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contactus")
def contactus():
    return render_template("contactus.html")



@app.route("/top20")
def top20():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                          'DATABASE=Monitor;'
                          'UID=byltinsytesqladmin;'
                          'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
    cursor = conn.cursor()
    cursor.execute('SELECT TOP(21) id, job_id, event_trigger, event_description, trigger_time FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    row = cursor.fetchall()
    return render_template(f'top20.html', top20=row)


@app.route("/top50")
def top50():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                          'DATABASE=Monitor;'
                          'UID=byltinsytesqladmin;'
                          'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
    cursor = conn.cursor()
    cursor.execute('SELECT TOP(50) id, job_id, event_trigger, event_description, trigger_time FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    row = cursor.fetchall()
    return render_template(f'top50.html', top50=row)



@app.route("/top100")
def top100():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                          'DATABASE=Monitor;'
                          'UID=byltinsytesqladmin;'
                          'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
    cursor = conn.cursor()
    cursor.execute('SELECT TOP(100) id, job_id, event_trigger, event_description, trigger_time FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    row = cursor.fetchall()
    return render_template(f'top100.html', top100=row)


@app.route("/jobid")
def jobid():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                          'DATABASE=Monitor;'
                          'UID=byltinsytesqladmin;'
                          'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
    cursor = conn.cursor()
    cursor.execute('select * from dbo.logs2 where job_id = 23').fetchone()
    row = cursor.fetchall()
    return render_template(f'jobid.html', jobid=row)

@app.route("/hours24")
def hours24():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                          'DATABASE=Monitor;'
                          'UID=byltinsytesqladmin;'
                          'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
    cursor = conn.cursor()
    cursor.execute('SELECT  * FROM dbo.logs2 WHERE trigger_time >= DATEADD(day, -1, GETDATE())').fetchone()
    row = cursor.fetchall()
    return render_template(f'hours24.html', hours24=row)

@app.route("/lastweek")
def lastweek():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                          'DATABASE=Monitor;'
                          'UID=byltinsytesqladmin;'
                          'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
    cursor = conn.cursor()
    cursor.execute('SELECT  * FROM dbo.logs2 WHERE trigger_time > (SELECT DATEADD(WEEK, -1, GETDATE())) ORDER BY trigger_time DESC').fetchone()
    row = cursor.fetchall()
    return render_template(f'lastweek.html', lastweek=row)

# app.run()

if __name__ == "__main__":
    app.run(debug=True)

