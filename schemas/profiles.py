from marshmallow import Schema, fields, validate, ValidationError, validates_schema

from schemas.cars import GetCarSchema
from schemas.validators import username_starts_with_capital_letter


class LoginSchema(Schema):
    class Meta:
        ordered = True

    username = fields.String(required=True,
                             validate=[validate.Length(min=6, max=255), username_starts_with_capital_letter])
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))


class RegisterSchema(Schema):
    class Meta:
        ordered = True

    username = fields.String(required=True,
                             validate=[validate.Length(min=6, max=255), username_starts_with_capital_letter])
    email = fields.Email(required=True, validate=validate.Length(min=6, max=255))
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))
    confirm_password = fields.String(required=True, validate=validate.Length(min=6, max=255))

    @validates_schema
    def password_check(self, data, **kwargs):
        if data["password"] != data["confirm_password"]:
            raise ValidationError('Passwords must match!')


class AllProfilesSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Integer()
    username = fields.String()
    cars = fields.Nested(GetCarSchema(only=("id", "brand", "description")), many=True)
