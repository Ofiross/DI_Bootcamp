from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class New_user(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(min=3, message="Too Short, Enter a valid name")])
    street = StringField("Street", validators=[InputRequired(), Length(min=2, message="Too Short, Enter a valid street name")])
    city = StringField("City", validators=[InputRequired(), Length(min=2, message="Too Short, Enter a valid city name")])
    zipcode = StringField("Zipcode", validators=[InputRequired(), Length(min=5, message="Too Short, Enter a valid zipcode")])
    submit = SubmitField("Submit")

class Login(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(min=3, message="Too Short, Enter a valid name")])
    city = StringField("City", validators=[InputRequired(), Length(min=2, message="Too Short, Enter a valid city name")])
    submit = SubmitField("Submit")