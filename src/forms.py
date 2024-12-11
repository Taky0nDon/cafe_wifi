from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

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
