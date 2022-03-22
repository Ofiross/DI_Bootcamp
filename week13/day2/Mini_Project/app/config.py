import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '5441$f48760c3d5Tf9a18W31@ae0fd40'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'robots.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False