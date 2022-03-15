import flask


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'efd7@7d0910c6f277e56&94c01c7$f79'
from app import routes
