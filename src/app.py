from flask import Flask, g, render_template

from DatabaseManager import get_db, query_db, build_query

PROPERTIES = [
                "has_sockets",
                "has_toilet",
                "has_wifi",
                "cake_take_calls",
                "seats",
                "coffee_price"
             ]



app = Flask(__name__)

with app.app_context():
    db = get_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    all_rows = query_db("select * from cafe")
    for row in all_rows:
        print(row)
        for field in row:
            print(field)
    return render_template("index.html", rows=all_rows)

@app.route('/cafe/<int:cafe_id>')
def cafe(cafe_id):
    particular_cafe = query_db(f"select * from cafe where id=={cafe_id}")[0]
    return render_template("cafe.html", this_cafe=particular_cafe)
