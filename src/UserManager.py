from DatabaseManager import query_db, get_db
from flask import Flask
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self):
        self.is_admin = False
        self.index = None

app = Flask("app")
USER_DB_PATH = "/home/mike/code/100_days_of_code/final_projects/cafe_wifi/data/cafes.db"

with app.app_context():
    user_db = get_db(USER_DB_PATH)
    user_rows = query_db("SELECT * FROM user")

def get_users() -> dict:
    print(f"{user_rows=}")
    users = {row["username"]: {key:row[key] for key in row.keys()} for row in user_rows
            }

    if users is not None:
        return users
    else:
        return {}

def user_is_admin(user: User) -> bool:
    if user.index == 0:
        return True
    return False
