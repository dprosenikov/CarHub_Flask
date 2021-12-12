import os
from os import environ

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.cars import AllCars, MyCars
from resources.users import RegisterUser, LoginUser


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'CarsHubDB.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


migrate = Migrate(app, db)

api = Api(app)
api.add_resource(RegisterUser, "/register")
api.add_resource(LoginUser, "/login")
api.add_resource(AllCars, "/allcars")
api.add_resource(MyCars, "/mycars")


if __name__ == "__main__":
    app.run(DEBUG=True)
