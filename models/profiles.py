from db import db


class CarHubUser(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), default='GUEST', nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
