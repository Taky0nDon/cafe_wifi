import sqlite3

from pathlib import Path
from flask import g

DATABASE = '/home/mike/code/100_days_of_code/final_projects/cafe_wifi/data/cafes.db'
COLUMNS =  [
        "name",
        "map_url",
        "img_url",
        "location",
        "has_sockets",
        "has_toilet",
        "has_wifi",
        "can_take_calls",
        "seats",
        "coffee_price" 
        ]


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE, check_same_thread=False)
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else none) if one else rv

def build_query(column='*', condition:str='')-> str:
    if column not in ["id"] + COLUMNS:
        raise ValueError("Invalid column provided.")
    query = f"SELECT {column} from cafes"
    return query

def insert(row: dict, db: sqlite3.Connection, table: str="cafe") -> None:
    initial_rows = query_db("SELECT Count(*) FROM cafe")[0]
    print(initial_rows.keys())
    c = db.cursor()
    statement = f'insert into cafe values ({"?, "*len(row) +"?"})'
    c.execute(statement, [initial_rows[0]+1] + [r for r in row.values()]
               )
    db.commit()
    db.close()
    
    pass

def remove(id: int, table: str, db: sqlite3.Connection) -> None:
    db.execute('delete from cafe where id = 30')
    db.commit()
