from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound

from authorize import auth
from db import db
from models import CarModel
from schemas.cars import GetCarSchema, CreateCarSchema

CAR_NOT_FOUND = 'Car not found. If you entered the URL manually please check your spelling and try again.'


class AllCars(Resource):
    def get(self):
        cars = CarModel.query.all()
        schema = GetCarSchema()
        return schema.dump(cars, many=True)


class MyCars(Resource):
    @auth.login_required
    def get(self):
        current_user = auth.current_user()
        cars = CarModel.query.filter_by(user_id=current_user.id).all()
        schema = GetCarSchema()
        return schema.dump(cars, many=True)


class CreateCar(Resource):
    @auth.login_required
    def post(self):
        car_create_schema = CreateCarSchema()
        json_data = request.get_json()
        try:
            data = car_create_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        current_user = auth.current_user()
        car = CarModel(current_user.id, data["brand"], data["description"], data["year"], data["image"], data["price"])
        db.session.add(car)
        db.session.commit()
        car_created_schema = GetCarSchema()
        return car_created_schema.dump(car)


class CarDetails(Resource):
    def get(self, car_id):
        car = CarModel.query.filter_by(id=car_id).first()
        if not car:
            raise NotFound(CAR_NOT_FOUND)
        schema = GetCarSchema()
        return schema.dump(car)


class CarEdit(Resource):
    @auth.login_required
    def put(self, car_id):
        current_user = auth.current_user()
        car = CarModel.query.filter_by(id=car_id).first()
        if not car:
            raise NotFound(CAR_NOT_FOUND)
        if not (current_user.role == 'ADMIN' or car.owner.id == current_user.id):
            return 'Permission denied', 403
        car_update_schema = CreateCarSchema()
        json_data = request.get_json()
        try:
            data = car_update_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        car.brand = data["brand"]
        car.description = data["description"]
        car.year = data["year"]
        car.image = data["image"]
        car.price = data["price"]
        db.session.commit()
        car_updated_schema = GetCarSchema()
        return car_updated_schema.dump(car)


class CarDelete(Resource):
    @auth.login_required
    def delete(self, car_id):
        current_user = auth.current_user()
        car = CarModel.query.filter_by(id=car_id).first()
        if not car:
            raise NotFound(CAR_NOT_FOUND)
        if not (current_user.role == 'ADMIN' or car.owner.id == current_user.id):
            return 'Permission denied', 403
        db.session.delete(car)
        db.session.commit()
        return 'Deleted', 200
