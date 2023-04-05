import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():

    return render_template('base.html',)

@app.route("/home")
def home():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template("index.html", users=users)

@app.route("/result", methods = ["POST", "GET"])
def result():
    
    output = request.form.to_dict()
    name = output["name"]
    city = request.form.get("city")
    
    return render_template("index.html", nme = name, shehr = city)

# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        userName = request.form['userName']
        city = request.form['city']

        if not userName:
            flash('User Name is required!')
        elif not city:
            flash('City is required!')
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO users (userName, city) VALUES (?, ?)",
                         (userName, city))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug= True, port = 5001)