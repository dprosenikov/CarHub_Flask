from os import environ

import jwt
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models import CarHubUser
from schemas.profiles import RegisterSchema, LoginSchema


class RegisterUser(Resource):
    def post(self):
        register_schema = RegisterSchema()
        json_data = request.get_json()
        try:
            data = register_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        username, email, password = data["username"], data["email"], data["password"]
        password = generate_password_hash(password)
        user = CarHubUser(username, email, password)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            raise BadRequest("User with this email and/or username already exists.")
        return register_schema.dump(user), 201


class LoginUser(Resource):
    def post(self):
        login_schema = LoginSchema()
        json_data = request.get_json()
        try:
            data = login_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        user = CarHubUser.query.filter_by(username=data["username"]).first()
        if not user:
            raise BadRequest("Invalid user.")
        if not check_password_hash(user.password, data["password"]):
            raise BadRequest("Wrong password.")
        token = jwt.encode({"sub": user.id}, key=environ.get('JWT_SECRET_KEY'))
        return {"token": token}


