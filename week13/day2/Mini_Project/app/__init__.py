import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.models import User
def populate():
    with open('./users.json', 'r') as f:
        data = json.load(f)
        for person in data:
            new_person = User(name=person['name'],
                            street=person['address']['street'],
                            city=person['address']['city'],
                            zipcode=person['address']['zipcode'])
            db.session.add(new_person)
            db.session.commit()
""" populate() """

from app import routes, error_handlers, models
db.create_all()