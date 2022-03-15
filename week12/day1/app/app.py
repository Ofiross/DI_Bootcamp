import flask_wtf
import wtforms

app.config['SECRET_KEY'] = '#fkjek3t44`$fellf@'


class Form(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name")
    lastName = wtforms.PasswordField("Password")
    age = wtforms.StringField("Bio")
