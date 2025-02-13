import flask_login
from flask import Blueprint, render_template, request, Flask, g, request, redirect, url_for, abort
from functools import wraps


from forms import LoginForm
from DatabaseManager import get_db, insert
from UserManager import get_users, User, user_is_admin

auth = Blueprint('auth', __name__)
app = Flask("app")
with app.app_context():
    db = get_db()

def admin_only(function):  # This is a decorator.
    @wraps(function)
    def view(*args, **kwargs):
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
        users = get_users()
        print(users)
        if username in users and request.form["password"] == users[username]["pw_hash"]:
            flask_login.login_user(create_user_object(username))
            return redirect(url_for("admin_welcome"))
        return "BAD LOGIN"
    return render_template("login.html", form=login_form)

@auth.route('/register', methods=['GET', 'POST'])
def register_user():
    registration_form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        if  username in get_users():
            return "That name is not available."
        new_user = create_user_object(username)
        user_dict = {
               'id': len(get_users()) or 0,
               'username': request.form['username'],
               'password': request.form['password']
                }
        flask_login.login_user(new_user)
        insert(user_dict, db=db, table='user')

    return render_template("register.html")
