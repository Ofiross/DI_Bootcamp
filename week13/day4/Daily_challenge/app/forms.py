from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length

class Search_person(FlaskForm):
    name = StringField("Name", validators=[Length(min=3, message="Too Short, Enter a valid name")])
    submit = SubmitField("Submit")
    
class Search_number(FlaskForm):
    phone_number = StringField("Name", validators=[Length(min=3, message="Too Short, Enter a valid name")])
    submit = SubmitField("Submit")