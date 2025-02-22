import flask_login
from flask import Blueprint, render_template, request, Flask, g, request, redirect, url_for, abort
from functools import wraps


import DatabaseManager
from forms import LoginForm, RegisterForm
from DatabaseManager import get_db, insert, query_db
from UserManager import get_users, User, user_is_admin

auth = Blueprint('auth', __name__)
app = Flask("app")
with app.app_context():
    db = get_db()

def admin_only(function):  # This is a decorator.
    @wraps(function)
    def view(*args, **kwargs):
        print(f"{flask_login.current_user.is_admin=}")
        if flask_login.current_user.is_admin:
            return function(*args, **kwargs)
        else:
            return abort(code=403)
    return view


def create_user_object(username: str) -> User:
            user = User()
            user.id = username
            return user


@auth.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        username = request.form["username"]
        user = User(DatabaseManager.query_db("select * from user where username=?;",
                                        args=[username]))
        print(f"{user.id=}")
        print(user)
        if not user.username or user.password != request.form["password"]:
            return "BAD LOGIN"
        flask_login.login_user(user)
        if flask_login.current_user.is_admin:
            return redirect(url_for("admin_welcome"))
        return f"thanks for logging in {user.username}"
    return render_template("login.html", form=login_form)

@auth.route('/register', methods=['GET', 'POST'])
def register_user():
    registration_form = RegisterForm()
    if request.method == 'POST':
        username = request.form['username']
        name_check = query_db("select * from user where username==?",
                     args=[username])
        if  name_check:
            return "That name is not available."
        new_user = create_user_object(username)
        user_dict = {
               'username': request.form['username'],
               'password': request.form['password']
                }
        flask_login.login_user(new_user)
        insert(user_dict, db=db, table='user')

    return render_template("login.html", form=registration_form)
