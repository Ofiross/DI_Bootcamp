from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    street = db.Column(db.String(20))
    city = db.Column(db.String(20))
    zipcode = db.Column(db.String(8))