import sqlite3

from flask import Flask, g

app = Flask(__name__)

DATABASE = '/home/mike/code/100_days_of_code/final_projects/cafe_wifi/data/cafes.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def display_index():
    html = "<b>Welcome to the Cafe Site!</b>"
    cafe_names = query_db('select name from cafe')
    for name in cafe_names:
        html += f"\n check out {name}!"
    return html

