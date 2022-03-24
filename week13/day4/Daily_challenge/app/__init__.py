from faker import Faker
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config



app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
faker = Faker()


from app.models import Person, Phonenumber
""" def add_people():
    for i in range(100):
        new_person = Person(name=faker.name(),
                            email=faker.email(),
                            address=faker.address())
        human = Person.query.filter(Person.id == i).first()                    
        new_phone = Phonenumber(number=faker.phone_number(), person=human)

        db.session.add(new_person)
        db.session.add(new_phone)
        db.session.commit()
add_people() """

from app import routes, error_handlers, models
db.create_all()
