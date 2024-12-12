from secrets import token_urlsafe

import werkzeug
from flask import Flask, g, redirect, render_template, Response
from flask_wtf import CSRFProtect

from DatabaseManager import get_db, query_db, build_query
import DatabaseManager
from forms import AddCafeForm

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
    all_rows = query_db("select * from cafe")
    for row in all_rows:
        print(row)
        for field in row:
            print(field)
    return render_template("index.html", rows=all_rows)

@app.route('/cafe/<int:cafe_id>')
def cafe(cafe_id: int) -> str:
    particular_cafe = query_db(f"select * from cafe where id=={cafe_id}")[0]
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

@app.route('/delete')
def delete_page() -> str:
    return render_template("delete.html")
