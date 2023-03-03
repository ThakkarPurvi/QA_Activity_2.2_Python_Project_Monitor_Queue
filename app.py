from flask import Flask, render_template, request
import pyodbc


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

app.run()

if __name__ == "__main__":
    app.run(debug=True)