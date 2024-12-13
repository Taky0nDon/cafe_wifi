from flask import Blueprint, render_template, request, Flask, g


from forms import LoginForm
from DatabaseManager import get_db

auth = Blueprint('auth', __name__)
app = Flask("app")
with app.app_context():
    db = get_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@auth.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        print(request.form.get('username'), request.form.get('password'))
        statement = "INSERT INTO user VALUES (?, ?, ?)"
        c = db.cursor()
        user_id = c.execute("SELECT Count(*) FROM user").fetchall()[0][0]
        print(user_id)
        c.execute(statement,
                  [user_id, request.form.get('username'), request.form.get('password')]
                  )
        db.commit()
        db.close()


    return render_template("login.html", form=login_form)

@auth.route('/signup')
def signup():
    return 'Sigup'

@auth.route('/logout')
def logout():
    return 'Logout'
