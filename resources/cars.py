from flask_restful import Resource

from authorize import auth
from models import CarModel
from schemas.cars import GetCarSchema


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
