import sqlite3

connection = sqlite3.connect('database.db')


with open('users.sql') as con:
    connection.executescript(con.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (userName, city) VALUES (?, ?)",
            ('Sajeel', 'Bahawalpur')
            )

cur.execute("INSERT INTO users (userName, city) VALUES (?, ?)",
            ('AS', 'HR, BWP, LHR')
            )

connection.commit()
connection.close()