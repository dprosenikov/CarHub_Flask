import os

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.cars import AllCars, MyCars, CreateCar, CarDetails, CarEdit, CarDelete, SearchCar, GoogleSearch
from resources.profiles import RegisterUser, LoginUser, DeleteProfile, ListAllUsers

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'CarsHubDB.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db, compare_type=True, render_as_batch=True)

api = Api(app)
api.add_resource(RegisterUser, "/register")
api.add_resource(LoginUser, "/login")
api.add_resource(AllCars, "/allcars")
api.add_resource(MyCars, "/mycars")
api.add_resource(CreateCar, "/car/create")
api.add_resource(CarDetails, "/car/details/<int:car_id>")
api.add_resource(CarEdit, "/car/edit/<int:car_id>")
api.add_resource(CarDelete, "/car/delete/<int:car_id>")
api.add_resource(DeleteProfile, "/profile/delete/<int:profile_id>")
api.add_resource(ListAllUsers, "/allprofiles")
api.add_resource(SearchCar, "/search/<search_by>")
api.add_resource(GoogleSearch, "/googlesearch/<search_by>")

if __name__ == "__main__":
    app.run(DEBUG=True)
