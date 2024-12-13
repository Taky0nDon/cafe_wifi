from secrets import token_urlsafe

import werkzeug
from flask import Flask, g, redirect, render_template, request
from flask_wtf import CSRFProtect

from auth import auth as auth_blueprint
from DatabaseManager import get_db, query_db, get_all_cafes, remove
import DatabaseManager
from forms import AddCafeForm, DeleteCafeForm

PROPERTIES = [
                "has_sockets",
                "has_toilet",
                "has_wifi",
                "cake_take_calls",
                "seats",
                "coffee_price"
             ]

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
        }


app = Flask(__name__)
app.register_blueprint(auth_blueprint)

app.secret_key = token_urlsafe(16)
csrf = CSRFProtect(app)

with app.app_context():
    db = get_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home() -> str:
    all_rows = get_all_cafes()
    return render_template("index.html", rows=all_rows)

@app.route('/cafe/<int:cafe_id>')
def cafe(cafe_id: int) -> str:
    particular_cafe = query_db(f"SELECT * FROM cafe WHERE id = {cafe_id}")[0]
    return render_template("cafe.html", this_cafe=particular_cafe)

@app.route('/add', methods=["GET", "POST"])
def add_page() -> str | werkzeug.wrappers.response.Response:
    add_cafe_form = AddCafeForm()
    print(dir(add_cafe_form))
    if add_cafe_form.validate_on_submit():
        for field in new_cafe:
            new_cafe[field] = getattr(add_cafe_form, field).data
        DatabaseManager.insert(new_cafe, db=db)
        return redirect('/')
    return render_template("add.html", form=add_cafe_form, cafe_data = new_cafe)

@app.route('/delete', methods=["GET", "POST"])
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
