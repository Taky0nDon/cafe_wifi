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

def build_query(column='*', table: str='cafes', condition:str='')-> str:
    query = f"SELECT {column} from {table}"
    return query


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else none) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def display_index():
    html = "<b>welcome to the cafe site!</b><br>"
    cafe_name_rows = query_db(build_query("name", "cafe"))
    for cafe_row in cafe_name_rows:
        name = cafe_row['name']
        print(type(cafe_row))
        html += f"check out {name}<br>"
    return html

