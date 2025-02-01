from flask_wtf import FlaskForm
from wtforms import HiddenField, PasswordField, StringField, SubmitField, validators
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired

from DatabaseManager import get_all_cafes

class LoginForm(FlaskForm):
    username = StringField("Username: ",
                           validators=[DataRequired()])
    password = PasswordField("Password: ",
                             validators=[DataRequired()])
    submit = SubmitField("Login")

class AddCafeForm(FlaskForm):
    name = StringField("Name: ",
                            validators=[DataRequired()]
                            )
    map_url = StringField("Map URL: ",
                            validators=[DataRequired()]
                            )
    img_url = StringField("Image URL: ",
                            validators=[DataRequired()]
                            )
    location = StringField("Location: ",
                            validators=[DataRequired()]
                            )
    has_sockets = StringField("Sockets (Y/N): ",
                            validators=[DataRequired()]
                              )
    has_toilet = StringField("Toilet (Y/N): ",
                            validators=[DataRequired()]
                              )
    has_wifi = StringField("WiFi (Y/N): ",
                            validators=[DataRequired()]
                              )
    can_take_calls = StringField("Calls (Y/N): ",
                            validators=[DataRequired()]
                              )
    seats = StringField("Number of seats: ",
                            validators=[DataRequired()]
                              )
    coffee_price = StringField("Coffee Price: ",
                            validators=[DataRequired()]
                              )
    submit = SubmitField("Add Cafe")
    submitted_by_id = HiddenField("placeholder")

class DeleteCafeForm(FlaskForm):
    cafe_name = SelectField()
    submit = SubmitField("Remove this cafe")
