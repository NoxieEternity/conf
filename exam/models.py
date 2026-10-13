from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(128), nullable=False)


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(64), nullable=False)
    room = db.Column(db.String(128), nullable=False)
    date = db.Column(db.String(16), nullable=False)
    payment = db.Column(db.String(64), nullable=False)
    status = db.Column(db.String(64), default='Новая')
    feedback = db.Column(db.String(512), default='')