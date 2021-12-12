from db import db
from models.enums import CarBrands


class CarModel(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    brand = db.Column(db.Enum(CarBrands), nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    complainer = db.relationship("CarHubUser")
