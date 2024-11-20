import sqlite3

from pathlib import Path
from flask import g

class DatabaseManager:
    def __init__(self, path_to_db: str | Path):
        self.db_path = path_to_db


    def get_db(self):
        self.db = getattr(g, '_database', None)
        if self.db is None:
            self.db = g._database = sqlite3.connect(self.db_path)
        self.db.row_factory = sqlite3.Row
        return self.db

    def query_db(self, query, args=(), one=False):
        cur = self.get_db(self.db_path).execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else none) if one else rv

    @classmethod
    def build_query(cls, column='*', condition:str='')-> str:
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


