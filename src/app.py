from secrets import token_urlsafe
from os import environ

import flask_wtf
import werkzeug
import flask_login
from flask import Flask, g, redirect, render_template, request
from flask_wtf import CSRFProtect
from dotenv import load_dotenv

from auth import auth as auth_blueprint, admin_only 
from DatabaseManager import get_db, query_db, get_all_cafes, remove
import DatabaseManager
from forms import AddCafeForm, DeleteCafeForm
from UserManager import get_users, User, user_is_admin
from MailHandler import submit_request, Message

load_dotenv(".env")
PW = environ["PW"]
EMAIL = environ["EMAIL"]
SERVER = environ["SERVER"]
test_message = Message("Hello world", "Please add my cafe to your website").message


app = Flask(__name__)
app.secret_key = token_urlsafe(16)
csrf = CSRFProtect(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

app.register_blueprint(auth_blueprint)
with app.app_context():
    db = get_db()

users = get_users()

@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    print(f"Creating a user object in user_loader")
    user = User()
    user.index = users[username]["id"]
    user.id = username
    if user_is_admin(user):
        user.is_admin = True
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in users:
        return
    print(f"Creating a User object in request_loader")
    user = User()
    user.id = username
    return user


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/")
def home() -> str:
    all_rows = get_all_cafes()
    return render_template("index.html", rows=all_rows)


@app.route("/cafe/<int:cafe_id>")
def cafe(cafe_id: int) -> str:
    particular_cafe = query_db(f"SELECT * FROM cafe WHERE id = {cafe_id}")[0]
    return render_template("cafe.html", this_cafe=particular_cafe)


@app.route("/add", methods=["GET", "POST"])
def add_page() -> str | werkzeug.wrappers.response.Response:
    new_cafe = {
        "name": None,
        "map_url": None,
        "img_url": None,
        "location": None,
        "has_sockets": None,
        "has_toilet": None,
        "has_wifi": None,
        "can_take_calls": None,
        "seats": None,
        "coffee_price": None,
        "submitted_by_id": "666"
    }
    add_cafe_form = AddCafeForm()
    if add_cafe_form.validate_on_submit():
        for field in new_cafe:
            new_cafe[field] = getattr(add_cafe_form, field).data

        if flask_login.current_user.is_authenticated and user_is_admin(flask_login.current_user):
            DatabaseManager.insert(new_cafe, db=db)
        else:
            DatabaseManager.insert(new_cafe, db=db, table="submission")
        return redirect("/")
    return render_template("add.html", form=add_cafe_form, cafe_data=new_cafe)


#TODO: submitted by string is not being inserted into table
@app.route("/view-pending", methods=["GET"])
def view_pending_submissions() -> str:
    pending_cafes = query_db("select * from submission")
    return render_template("pending.html", submitted_cafes=pending_cafes)


@app.route("/delete", methods=["GET", "POST"])
def delete_page() -> str | werkzeug.Response:
    delete_cafe_form = DeleteCafeForm()
    current_cafes = get_all_cafes()
    if request.method == "POST":
        print("posting")
        cafe_id = request.form.get("cafe_id_to_delete")
        if cafe_id is not None:
            cafe_id = int(cafe_id)
            remove(cafe_id, db)
        return redirect("/")
    else:
        print("method", request.method)
    return render_template("delete.html", form=delete_cafe_form, data=current_cafes)

@app.route('/admin-welcome')
@admin_only
def admin_welcome():
    return render_template("admin-welcome.html")
