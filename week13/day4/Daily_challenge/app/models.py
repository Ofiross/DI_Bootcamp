from __future__ import unicode_literals
from enum import unique
from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(30), unique=True)
    phonenumbers = db.relationship('Phonenumber', backref='person', lazy='dynamic')
    address = db.Column(db.String(20))

class Phonenumber(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(20))
    master = db.Column(db.Integer, db.ForeignKey('person.id'))