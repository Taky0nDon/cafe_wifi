from flask_login.utils import LocalProxy
from DatabaseManager import query_db, get_db
from flask import Flask
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_row):
        self.username = user_row[0]["username"]
        self.password = user_row[0]["password"]
        self.id = user_row[0]["id"]
        self.is_admin = user_is_admin(self)
    def get_id(self):
        return str(self.id)

app = Flask("app")
USER_DB_PATH = "/home/mike/code/100_days_of_code/final_projects/cafe_wifi/data/cafes.db"

with app.app_context():
    user_db = get_db(USER_DB_PATH)
    user_rows = query_db("SELECT * FROM user")

def get_users() -> dict:
    if user_rows is None:
        raise ValueError("No users found")
    users = {row["username"]: {key:row[key] for key in row.keys()} for row in user_rows
            }

    if users is not None:
        return users
    else:
        return {}

def user_is_admin(user: User | LocalProxy) -> bool:
    if user.id == 0:
        return True
    return False
