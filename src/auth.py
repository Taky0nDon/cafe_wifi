import flask_login
from flask import Blueprint, render_template, request, Flask, g, request, redirect, url_for, abort
from functools import wraps


from forms import LoginForm
from DatabaseManager import get_db
from UserManager import get_users, User

auth = Blueprint('auth', __name__)
app = Flask("app")
with app.app_context():
    db = get_db()

def admin_only(function):
    @wraps(function)
    def view(*args, **kwargs):
        if flask_login.current_user.is_anonymous or flask_login.current_user.id != "ser03":
            return abort(code=403)
        else:
            return function(*args, **kwargs)
    return view


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@auth.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=login_form)

    username = request.form["username"]
    users = get_users()
    if username in users and request.form["password"] == users[username]["pw_hash"]:
        user = User()
        user.id = username
        flask_login.login_user(user)
        return redirect(url_for("admin_welcome"))

    return "BAD LOGIN"
