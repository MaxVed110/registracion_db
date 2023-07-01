from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    second_name = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return f'User №{User.id}: {User.first_name} {User.second_name}, email {User.email}'
