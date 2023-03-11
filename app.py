""" IMPORT FLASK , RENDER TEMPLATE AND REQUEST """
from flask import Flask, render_template, request
from variable import cursor

app = Flask(__name__)

@app.route("/")
def home():
    """ Home page function"""
    return render_template("home.html")


@app.route("/about")
def about():
    """ About page function"""
    return render_template("about.html")


@app.route("/contactus")
def contactus():
    """ Contact page function"""
    return render_template("contactus.html")


@app.route("/top20")
def top20():
    """ Top 20 page function"""
    cursor.execute('SELECT TOP(21) id, job_id, event_trigger, event_description, trigger_time '
                   'FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    row = cursor.fetchall()
    return render_template('top20.html', top20=row)

@app.route("/top50")
def top50():
    """ Top 50 page function"""
    cursor.execute('SELECT TOP(50) id, job_id, event_trigger, event_description, trigger_time '
                   'FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    row = cursor.fetchall()
    return render_template('top50.html', top50=row)


@app.route("/top100")
def top100():
    """ Top 100 page function"""
    cursor.execute('SELECT TOP(100) id, job_id, event_trigger, event_description, trigger_time '
                   'FROM dbo.logs2 ORDER BY trigger_time DESC').fetchone()
    row = cursor.fetchall()
    return render_template('top100.html', top100=row)


@app.route("/jobid", methods=['GET'])
def jobid():
    """ Job id function using GET method"""
    return render_template('jobid.html')


@app.route("/jobid", methods=['POST'])
def getjob():
    """ Job id function using POST method"""
    id_ = request.form.get("job_id")
    cursor.execute(f"select * from dbo.logs2 "
                   f"where job_id={id_} ORDER BY trigger_time DESC").fetchone()
    row = cursor.fetchall()
    return render_template('jobid.html', jobid=row)


@app.route("/hours24")
def hours24():
    """ Hours 24 function """
    cursor.execute('SELECT  * FROM dbo.logs2 WHERE trigger_time >= DATEADD'
                   '(day, -1, GETDATE()) ORDER BY trigger_time DESC').fetchone()
    row = cursor.fetchall()
    return render_template('hours24.html', hours24=row)


@app.route("/lastweek")
def lastweek():
    """ Last week function """
    cursor.execute('SELECT  * FROM dbo.logs2 WHERE trigger_time > (SELECT DATEADD'
                   '(WEEK, -1, GETDATE())) ORDER BY trigger_time DESC').fetchone()
    row = cursor.fetchall()
    return render_template('lastweek.html', lastweek=row)

if __name__ == "__main__":
    app.run(debug=True)

print("Thank you")
