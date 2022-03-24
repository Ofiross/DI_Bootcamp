import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '0c3d5Ft9ae0fd48a18W31@5441$f4O76'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'phone_numbers.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False