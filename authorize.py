from os import environ

import jwt
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import BadRequest

from models import CarHubUser

auth = HTTPTokenAuth()


@auth.verify_token
def verify_token(token):
    try:
        data = jwt.decode(token, key=environ.get('JWT_SECRET_KEY'), algorithms=["HS256"])
        user_id = data["sub"]
    except jwt.InvalidTokenError:
        raise BadRequest("Invalid token")
    user = CarHubUser.query.filter_by(id=user_id).first()
    return user
