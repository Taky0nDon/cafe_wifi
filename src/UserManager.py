from DatabaseManager import query_db, get_db
from flask import Flask
from flask_login import UserMixin


class User(UserMixin):
    pass

app = Flask("app")
USER_DB_PATH = "/home/mike/code/100_days_of_code/final_projects/cafe_wifi/data/users.db"

with app.app_context():
    user_db = get_db()
    user_rows = query_db("SELECT * FROM user")

def get_users() -> dict:
    users = {row["username"]: {key:row[key] for key in row.keys()} for row in user_rows
            }

    if users is not None:
        return users
    else:
        return {}

