import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


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


@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


if __name__ == '__main__':
    app.run(debug= True, port = 5001)