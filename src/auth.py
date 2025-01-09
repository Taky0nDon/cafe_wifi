import flask_login
from flask import Blueprint, render_template, request, Flask, g, request, redirect, url_for, abort
from functools import wraps


from forms import LoginForm
from DatabaseManager import get_db
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


@auth.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        username = request.form["username"]
        users = get_users()
        if username in users and request.form["password"] == users[username]["pw_hash"]:
            print(f"Creating a user objext in login")
            user = User()
            user.id = username
            flask_login.login_user(user)
            return redirect(url_for("admin_welcome"))
        return "BAD LOGIN"
    return render_template("login.html", form=login_form)

