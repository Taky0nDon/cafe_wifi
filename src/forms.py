from flask_wtf import FlaskForm
from wtforms import HiddenField, PasswordField, RadioField, StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField(label="Login", name="submit")

class RegisterForm(LoginForm):
    submit = SubmitField("Sign up")

#TODO booleans should be radio fields
class AddCafeForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    map_url = StringField("Map URL: ", validators=[DataRequired()])
    img_url = StringField("Image URL: ", validators=[DataRequired()])
    location = StringField("Location: ", validators=[DataRequired()])
    has_sockets = StringField("Sockets (Y/N): ", validators=[DataRequired()])
    has_toilet = StringField("Toilet (Y/N): ", validators=[DataRequired()])
    has_wifi = StringField("WiFi (Y/N): ", validators=[DataRequired()])
    can_take_calls = StringField("Calls (Y/N): ", validators=[DataRequired()])
    seats = StringField("Number of seats: ", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price: ", validators=[DataRequired()])
    submit = SubmitField("Add Cafe", name="submit")

class DeleteCafeForm(FlaskForm):
    cafe_name = SelectField()
    submit = SubmitField("Remove this cafe", name="submit")

class PendingCafeForm(FlaskForm):
    choices = {
                "accept": ["Accept"],
                "reject": ["Reject"],
                "postpone": ["Postpone"]
               }
    sub_id = HiddenField()
    decision = RadioField(label="Decision: ", choices=(choices))
    submit = SubmitField("Submit", name="submit")
