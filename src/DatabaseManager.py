import sqlite3

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


def get_db(db_path=DATABASE):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_path, check_same_thread=False)
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_all_cafes() -> list[str] | None:
    return query_db("SELECT * FROM cafe")

def insert(row: dict, db: sqlite3.Connection, table: str="cafe") -> None:
    initial_rows = query_db(f"SELECT Count(*) FROM {table}")
    id = 0
    if initial_rows is not None:
        id = initial_rows[0][0]
    c = db.cursor()
    params = str("?, "*(len(row)+1)).rstrip(", ")
    statement = f'insert into {table} values ({params})'
    c.execute(statement, [id] + [r for r in row.values()]
               )
    db.commit()
    db.close()

def remove(id: int, db: sqlite3.Connection, table="cafe") -> None:
    db.execute(f'delete from {table} where id = {id}')
    db.commit()
    db.close()
