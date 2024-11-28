import sqlite3

from pathlib import Path
from flask import g

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
    return (rv[0] if rv else none) if one else rv

def build_query(column='*', condition:str='')-> str:
    if column not in ["id",
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
                      ]:
        raise ValueError("Invalid column provided.")
    query = f"SELECT {column} from cafes"
    return query

def insert(row: dict, table: str, db: sqlite3.Connection) -> None:
    db.execute('insert into cafe values (30, "test", "test", "test", "test", 1, 1, 1, 1, 10, 10)')
    db.commit()
    
    pass

def remove(id: int, table: str, db: sqlite3.Connection) -> None:
    db.execute('delete from cafe where id = 30')
    db.commit()
